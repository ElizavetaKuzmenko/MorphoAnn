#coding: utf-8
"""makeshift .tkn-file generator for testing purposes"""

import codecs
_in = [word.strip('.,') for word in codecs.open('Burdukova_blog.txt', 'r', 'utf-8').read().split()]
_out = codecs.open('Burdukova_blog.tkn', 'w', 'utf-8')

count = 0
for i in _in:
    _out.write('%s %s %s' % (i, count, count + len(i)) + '\n')
    count += (len(i) + 1)
_out.close()