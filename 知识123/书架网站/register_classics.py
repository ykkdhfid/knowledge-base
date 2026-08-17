# -*- coding: utf-8 -*-
"""把四大名著注册进 books.json（读 _manifest.json，可重复运行自动去重）"""
import json
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
BJ = os.path.join(HERE, '书库', 'books.json')
MF = json.load(open(os.path.join(HERE, '书库', '古典名著', '_manifest.json'), encoding='utf-8'))

META = {
    '西游记': {
        'id': 'xiyouji',
        'cover': 'linear-gradient(135deg,#f83600 0%,#f9d423 100%)',
        'tags': ['公版全文', '神魔小说', '四大名著', '可整本阅读'],
        'desc': '四大名著之一，吴承恩著。石猴出世、大闹天宫、九九八十一难——公有领域版本全文 100 回，已在书架内完整可读。',
    },
    '三国演义': {
        'id': 'sanguo',
        'cover': 'linear-gradient(135deg,#4b1248 0%,#f0c27b 100%)',
        'tags': ['公版全文', '历史演义', '四大名著', '可整本阅读'],
        'desc': '四大名著之一，罗贯中著。桃园结义到三分归晋，公有领域版本全文 120 回，已在书架内完整可读。',
    },
    '水浒传': {
        'id': 'shuihu',
        'cover': 'linear-gradient(135deg,#232526 0%,#414345 100%)',
        'tags': ['公版全文', '英雄传奇', '四大名著', '可整本阅读'],
        'desc': '四大名著之一，施耐庵著。一百单八将逼上梁山，公有领域版本全文 120 回，已在书架内完整可读。',
    },
    '红楼梦': {
        'id': 'honglou',
        'cover': 'linear-gradient(135deg,#ee9ca7 0%,#ffdde1 100%)',
        'tags': ['公版全文', '世情小说', '四大名著', '可整本阅读'],
        'desc': '四大名著之首，曹雪芹、高鹗著。大观园的兴衰与宝黛之情，公有领域版本全文 120 回，已在书架内完整可读。',
    },
}

books = json.load(open(BJ, encoding='utf-8'))
shutil.copy(BJ, BJ + '.bak')
ids = {b['id'] for b in books}
added = 0
for name, info in MF.items():
    if 'error' in info:
        print('skip', name, info['error'])
        continue
    meta = META[name]
    if meta['id'] in ids:
        continue
    books.append({
        'id': meta['id'],
        'title': name,
        'author': info['author'] + '（公版）',
        'category': '古典名著',
        'tags': meta['tags'],
        'desc': meta['desc'],
        'cover': meta['cover'],
        'chapters': [{'title': c['title'][:40], 'file': '古典名著/%s/%s' % (name, c['file'])}
                     for c in info['chapters']],
    })
    added += 1
    ids.add(meta['id'])

with open(BJ, 'w', encoding='utf-8') as f:
    json.dump(books, f, ensure_ascii=False, indent=2)
print('新增 %d 本，现共 %d 本' % (added, len(books)))
