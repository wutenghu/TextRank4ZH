import jieba.posseg as pseg
words = pseg.cut("我爱北京天安门.。；‘你的#")
for w in words:
    # print(w.word)
    print('{0} {1}'.format(w.word, w.flag))
    print(type(w.word))  # in py2 is unicode, py3 is str

