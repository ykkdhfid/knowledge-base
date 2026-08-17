# -*- coding: utf-8 -*-
"""从 GitHub 公版仓库下载四大名著 txt，按「第X回」分章写入书库，生成清单。

- 原始全文缓存在 书库\\古典名著\\_raw\\（第二次运行不再联网）
- 章节选取用「顺序跟踪法」：从第 1 回开始按 1,2,3...顺序认章，
  自动跳过正文里偶发的「第X回」字样，比单纯去重更稳
- 可重复运行：每次全量重新生成
"""
import json
import os
import re
import ssl
import time
import urllib.request

CTX = ssl._create_unverified_context()
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(HERE, '书库', '古典名著')
RAW = os.path.join(LIB, '_raw')
os.makedirs(RAW, exist_ok=True)

BOOKS = [
    {'name': '西游记', 'author': '吴承恩', 'expect': 100},
    {'name': '三国演义', 'author': '罗贯中', 'expect': 120},
    {'name': '水浒传', 'author': '施耐庵', 'expect': 120},
    {'name': '红楼梦', 'author': '曹雪芹、高鹗', 'expect': 120},
]
REPOS = [
    ('tennessine/corpus', 'master'),
    ('Jiasheng-Shi/Dream-of-the-Red-Chamber', 'main'),
    ('Jiasheng-Shi/Dream-of-the-Red-Chamber', 'master'),
    ('weiyinfu/SiDaMingZhu', 'master'),
]
JUNK = re.compile(r'(更多精彩|www\.|http://|https://|\.com|\.net|本书来自|免费下载|电子书下载)')

CN_DIGIT = {'零': 0, '〇': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4,
            '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}
CN_UNIT = {'十': 10, '百': 100, '千': 1000}
HEAD = re.compile(r'^第([零〇一二三四五六七八九十百千两\d]{1,8})[回卷]\s*\S')


def cn2int(s):
    if s.isdigit():
        return int(s)
    total, num = 0, 0
    for c in s:
        if c in CN_DIGIT:
            num = num * 10 + CN_DIGIT[c]
        elif c in CN_UNIT:
            total += (num or 1) * CN_UNIT[c]
            num = 0
        else:
            return None
    return total + num


def fetch_raw(name):
    cache = os.path.join(RAW, name + '.txt')
    if os.path.exists(cache) and os.path.getsize(cache) > 100000:
        return open(cache, 'rb').read()
    quoted = urllib.request.quote(name) + '.txt'
    for repo, branch in REPOS:
        for host in ('https://raw.githubusercontent.com/%s/%s/' % (repo, branch),
                     'https://mirrors.bfsu.edu.cn/github-raw/%s/%s/' % (repo, branch)):
            try:
                req = urllib.request.Request(host + quoted, headers=UA)
                with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
                    raw = r.read()
            except Exception:
                continue
            if len(raw) > 100000:
                with open(cache, 'wb') as f:
                    f.write(raw)
                print('  downloaded %s from %s (%d KB)' % (name, repo, len(raw) // 1024))
                return raw
    return None


def split_chapters(lines):
    """顺序跟踪：找到第1回后，每次向后找编号恰好 +1 的标题行（允许跳号容错）"""
    marks = []
    for i, ln in enumerate(lines):
        if 4 <= len(ln) <= 60:
            m = HEAD.match(ln)
            if m:
                n = cn2int(m.group(1))
                if n and 1 <= n <= 200:
                    marks.append((i, n, ln))
    if not marks:
        return None
    seq, target, pos = [], 1, 0
    while pos < len(marks):
        # 从 pos 起找第一个编号 == target 的标题
        pick = None
        for k in range(pos, len(marks)):
            if marks[k][1] == target:
                pick = k
                break
            if marks[k][1] > target + 1:   # 编号大幅超前，说明本书缺 target 回
                break
        if pick is None:
            # 容错：跳过缺失编号
            nxt = [m for m in marks[pos:] if m[1] > target]
            if not nxt:
                break
            target = nxt[0][1]
            continue
        seq.append(marks[pick])
        target += 1
        pos = pick + 1
        if target > 200:
            break
    return seq


def main():
    manifest = {}
    for b in BOOKS:
        name = b['name']
        print('processing', name)
        raw = fetch_raw(name)
        if not raw:
            manifest[name] = {'error': 'download failed'}
            print('  FAILED download')
            continue
        try:
            text = raw.decode('utf-8')
        except UnicodeDecodeError:
            text = raw.decode('gb18030')
        lines = [ln.strip() for ln in text.replace('\r\n', '\n').replace('\r', '\n').split('\n')]
        seq = split_chapters(lines)
        if not seq or len(seq) < b['expect'] - 2:
            manifest[name] = {'error': 'split failed: %d' % (len(seq) if seq else 0)}
            print('  FAILED split (%d chapters, expect %d)' % (len(seq) if seq else 0, b['expect']))
            continue
        d = os.path.join(LIB, name)
        os.makedirs(d, exist_ok=True)
        for old in os.listdir(d):
            if old.endswith('.txt'):
                os.remove(os.path.join(d, old))
        items, chars = [], 0
        for k, (i, n, title) in enumerate(seq):
            end = seq[k + 1][0] if k + 1 < len(seq) else len(lines)
            paras = [p for p in lines[i + 1:end] if p and not JUNK.search(p)]
            fn = '%03d.txt' % (k + 1)
            with open(os.path.join(d, fn), 'w', encoding='utf-8') as f:
                f.write(title + '\n\n' + '\n\n'.join(paras) + '\n')
            chars += sum(len(p) for p in paras)
            items.append({'file': fn, 'title': title, 'paras': len(paras)})
        manifest[name] = {'author': b['author'], 'chapters': items, 'n': len(items),
                          'first': items[0]['title'][:22], 'last': items[-1]['title'][:22],
                          'approx_chars': chars}
        print('  %d chapters ~%dk chars | %s ... %s'
              % (len(items), chars // 1000, items[0]['title'][:16], items[-1]['title'][:16]))
        time.sleep(0.3)
    with open(os.path.join(LIB, '_manifest.json'), 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    print('manifest saved')


if __name__ == '__main__':
    main()
