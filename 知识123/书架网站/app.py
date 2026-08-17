# -*- coding: utf-8 -*-
"""
本地书架网站（Flask）
====================
功能：书架展示 / 分类筛选 / 搜索 / 章节阅读 / 字号调节 / 阅读进度记忆 / 深色模式
内容：3 部原创轻小说 + 通信工程知识库 + 毕业论文指南

运行：在 PyCharm 中直接右键 Run，或命令行  python app.py
然后浏览器打开  http://127.0.0.1:5000
"""
import os
import re
import json
from flask import Flask, render_template, abort, request, send_from_directory, url_for

BASE_DIR = os.path.dirname(os.path.abspath(__file__))     # 书架网站/
ROOT_DIR = os.path.dirname(BASE_DIR)                      # E:\知识123\
LIB_DIR = os.path.join(BASE_DIR, '书库')
KB_IMAGE_DIR = os.path.join(ROOT_DIR, '通信工程知识库', 'images')

app = Flask(__name__)

# 尽量用 markdown 库渲染知识库讲义；没装也能跑（纯文本降级）
try:
    import markdown as _md
    HAS_MD = True
except ImportError:
    HAS_MD = False


def load_books():
    with open(os.path.join(LIB_DIR, 'books.json'), encoding='utf-8') as f:
        return json.load(f)


BOOKS = load_books()
BOOK_MAP = {b['id']: b for b in BOOKS}


def read_chapter(book, index):
    """读取一章内容。file 以 @/ 开头表示相对知识库根目录（markdown 讲义）"""
    ch = book['chapters'][index]
    path = ch['file']
    if path.startswith('@/'):
        full = os.path.join(ROOT_DIR, path[2:])
    else:
        full = os.path.join(LIB_DIR, path)
    if not os.path.isfile(full):
        abort(404)
    with open(full, encoding='utf-8') as f:
        text = f.read()
    if full.endswith('.md'):
        if HAS_MD:
            html = _md.markdown(text, extensions=['fenced_code', 'tables'])
            # 把讲义里的相对图片路径改写为本站路由
            html = re.sub(r'src="([^"]*?images/)([^"/]+)"',
                          r'src="/kb_image/\2"', html)
            return html, ch['title']
        text = text.replace('<', '&lt;')
        return '<pre style="white-space:pre-wrap">%s</pre>' % text, ch['title']
    # 纯文本小说：按空行分段
    paras = ['<p>%s</p>' % p.strip().replace('\n', '<br>') for p in text.split('\n\n') if p.strip()]
    return '\n'.join(paras), ch['title']


# ---------------- 路由 ----------------

@app.route('/')
def index():
    q = request.args.get('q', '').strip()
    cat = request.args.get('cat', '全部')
    books = BOOKS
    if cat != '全部':
        books = [b for b in books if b['category'] == cat]
    if q:
        books = [b for b in books
                 if q in b['title'] or q in b.get('author', '')
                 or any(q in t for t in b.get('tags', []))
                 or q in b.get('desc', '')]
    cats = ['全部'] + sorted({b['category'] for b in BOOKS})
    return render_template('index.html', books=books, cats=cats, cur_cat=cat, q=q)


@app.route('/book/<bid>')
def book(bid):
    b = BOOK_MAP.get(bid)
    if not b:
        abort(404)
    return render_template('book.html', b=b)


@app.route('/read/<bid>/<int:idx>')
def read(bid, idx):
    b = BOOK_MAP.get(bid)
    if not b or not (0 <= idx < len(b['chapters'])):
        abort(404)
    html, title = read_chapter(b, idx)
    return render_template('read.html', b=b, idx=idx, title=title, content=html,
                           total=len(b['chapters']))


@app.route('/kb_image/<path:filename>')
def kb_image(filename):
    return send_from_directory(KB_IMAGE_DIR, filename)


@app.route('/mindmap')
def mindmap():
    """知识导图：导图里的科目节点链接回本站对应章节，双向打通"""
    return send_from_directory(os.path.join(ROOT_DIR, '知识导图'),
                               '通信工程知识导图.html')


if __name__ == '__main__':
    print('书架已启动，浏览器打开 http://127.0.0.1:5000')
    app.run(debug=True, port=5000)
