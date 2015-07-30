# coding: utf-8
# author: liza
''' takes a text and generates a stream of tokens and their spans, which is written to a .tkn file. '''
import codecs, re, sys

def token(txt):
    from lemmatizer import lemmatizer
    import re

    dic = {'will': '\'ll', 'are': '\'re', 'am': '\'m', 'is': '\'s', 'not': 'n\'t'}
    expr = []
    t = txt.replace(u'’', u'\'')
    tkn = u''
    for c in dic.values():
        if c in t:
	    expr += re.findall('\\s+([^\\s]*)' + c, t, flags=re.U)
    n = 0
    lemmas = lemmatizer(t)
    for l in range(len(lemmas)):
	w = lemmas[l][0]
	if w in dic.keys() and lemmas[l - 1][0] in expr:
	    w = dic[w]#.replace('\'', u'’')
	try:
	    span = (t.index(w), t.index(w) + len(w))
	except ValueError:
	    if '_' in w:
		w = w.replace('_', ' ')
		span = (t.index(w), t.index(w) + len(w))
	t = t[:span[0]] + ' '* len(w) +  t[span[1]:]
	tkn += str(n) + '\t' + w + '\t' + str(span[0]) + ' ' + str(span[1]) + '\n'
	n += 1
    return tkn

#d = sys.argv[1]
#txt = codecs.open(d, 'r', 'utf-8').read()
#print tkn_gen(txt)