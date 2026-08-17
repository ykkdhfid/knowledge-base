# -*- coding: utf-8 -*-
"""把三秋缒分类的 7 个条目注册进 books.json（可重复运行，自动去重）"""
import json
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
BJ = os.path.join(HERE, '书库', 'books.json')

D = '（本条目为原创导读，不含正文；可在文件夹中放入自己的合法文本阅读）'

BOOKS = [
    {
        'id': 'miaki-3days',
        'title': '三日间的幸福',
        'author': '三秋缒（导读为原创）',
        'category': '三秋缒',
        'tags': ['轻文学', '寿命', '代表作', '入门首选'],
        'desc': '三秋缒最出圈的作品：把寿命卖掉，一年只值一万日元。最后三个月里，卖寿命的青年与监视员宫城互相成为彼此的救赎。「人生的价值由什么决定」——奇想设定即主题。' + D,
        'cover': 'linear-gradient(135deg,#a8c0ff 0%,#3f2b96 100%)',
        'chapters': [
            {'title': '导读：档案·梗概·看点·串联', 'file': '三秋缒/三日间的幸福/01.txt'},
        ],
    },
    {
        'id': 'miaki-itai',
        'title': '不哭不哭，痛痛飞走吧',
        'author': '三秋缒（导读为原创）',
        'category': '三秋缒',
        'tags': ['轻文学', '暗色', '疼痛', '能力设定'],
        'desc': '三秋缒最暗最疼的一本：获得支配他人身体能力的青年「清洁工」，与一位想让身体「飞走」的失明少女。哄孩子的咒语，成了两个大人互相止疼的救命稻草。' + D,
        'cover': 'linear-gradient(135deg,#ff9a9e 0%,#fecfef 100%)',
        'chapters': [
            {'title': '导读：档案·梗概·看点·串联', 'file': '三秋缒/不哭不哭痛痛飞走吧/01.txt'},
        ],
    },
    {
        'id': 'miaki-summer-call',
        'title': '那年夏天，你打来的电话',
        'author': '三秋缒（导读为原创）',
        'category': '三秋缒',
        'tags': ['轻文学', '夏日', '赌局', '双部曲'],
        'desc': '脸带胎记的自卑少年，接到公共电话里神秘女子提出的赌局：去掉胎记、让初恋喜欢他，输了则要付出代价。夏日奇想双部曲·上卷，真相藏在续作《那年夏天，我拨去的电话》。' + D,
        'cover': 'linear-gradient(135deg,#f6d365 0%,#fda085 100%)',
        'chapters': [
            {'title': '导读：档案·梗概·看点·串联', 'file': '三秋缒/那年夏天你打来的电话/01.txt'},
        ],
    },
    {
        'id': 'miaki-parasite',
        'title': '恋爱寄生虫',
        'author': '三秋缒（导读为原创）',
        'category': '三秋缒',
        'tags': ['轻文学', '校园', '契约恋爱', '糖分最高'],
        'desc': '有洁癖的少年与融不进教室的少女达成「假装恋爱」的协议——把恋爱当作让彼此留在人类社会的寄生虫。糖分最高的入门甜口之作，亦有漫画改编。' + D,
        'cover': 'linear-gradient(135deg,#093028 0%,#237a57 100%)',
        'chapters': [
            {'title': '导读：档案·梗概·看点·串联', 'file': '三秋缒/恋爱寄生虫/01.txt'},
        ],
    },
    {
        'id': 'miaki-gioku',
        'title': '义忆',
        'author': '三秋缒（导读为原创）',
        'category': '三秋缒',
        'tags': ['轻文学', '近未来', '虚构记忆', '催泪'],
        'desc': '「义忆」技术可以植入以假乱真的虚构记忆。冷漠青年千寻误植入一段架空青春，虚构记忆里的青梅竹马夏凪灯花却出现在眼前。「正因是谎言，一切才更加温柔」——公认其代表作之一。' + D,
        'cover': 'linear-gradient(135deg,#4e54c8 0%,#8f94fb 100%)',
        'chapters': [
            {'title': '导读：档案·梗概·看点·串联', 'file': '三秋缒/义忆/01.txt'},
        ],
    },
    {
        'id': 'miaki-starting',
        'title': 'Starting Over 重启人生',
        'author': '三秋缒（导读为原创）',
        'category': '三秋缒',
        'tags': ['轻文学', '出道作', '青春', '谱系起点'],
        'desc': '三秋缒的网络连载成书出道作：围绕「如果能重新来过，青春会不会不一样」展开。观察「三秋缒之前的三秋缒」的必读样本，所有母题的原型手感。' + D,
        'cover': 'linear-gradient(135deg,#c79081 0%,#dfa579 100%)',
        'chapters': [
            {'title': '导读：档案·梗概·看点·串联', 'file': '三秋缒/Starting Over/01.txt'},
        ],
    },
    {
        'id': 'miaki-guide',
        'title': '三秋缒入门导读（读我）',
        'author': '三秋缒（导读为原创）',
        'category': '三秋缒',
        'tags': ['导读', '阅读路线', '正版指南'],
        'desc': '为三秋缒书架配套的导航书：作者与文风关键词、六部作品的阅读路线建议、正版获取方式与自助上架方法。建议从这本读起。' + D,
        'cover': 'linear-gradient(135deg,#e0eafc 0%,#cfdef3 100%)',
        'chapters': [
            {'title': '第一章 三秋缒与他的世界', 'file': '三秋缒/三秋缒导读/01.txt'},
            {'title': '第二章 推荐阅读路线', 'file': '三秋缒/三秋缒导读/02.txt'},
            {'title': '第三章 正版获取与书架使用说明', 'file': '三秋缒/三秋缒导读/03.txt'},
        ],
    },
]


def main():
    with open(BJ, encoding='utf-8') as f:
        books = json.load(f)
    shutil.copy(BJ, BJ + '.bak')
    ids = {b['id'] for b in books}
    added = 0
    for item in BOOKS:
        if item['id'] in ids:
            continue
        books.append(item)
        added += 1
    with open(BJ, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=2)
    print('新增 %d 本，现共 %d 本' % (added, len(books)))


if __name__ == '__main__':
    main()
