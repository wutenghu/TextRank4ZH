import codecs
text = codecs.open('./doc/01.txt', 'r', 'utf-8', 'ignore').read()
print(type(text))