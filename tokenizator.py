__author__ = 'liza55'

import codecs, os
#from nltk.tokenize.util import regexp_span_tokenize as sp
cd = os.getcwd()
txt = [t for t in os.listdir(cd) if t.endswith('.txt')]
txt = ['Burdukova_blog.txt']
for t in txt:
    tokens = []
    spans = []
    source = codecs.open(t, 'r', 'utf-8')
    stri = source.read()
    new = codecs.open(t[:-4] + '.tok', 'w', 'utf-8')
    ann = codecs.open(t[:-4] + '.ann', 'w', 'utf-8')
    token_f = codecs.open(t + '.tok', 'r', 'utf-8')
    for line in token_f.readlines():
	tokens.append(line.strip().replace('_', ' '))
    for token in tokens:
	try:
	    span = (stri.index(token), stri.index(token) + len(token))
	    stri = stri[:span[0]] + ' '*(span[1] - span[0]) + stri[span[1]:]
	    spans.append(span)
	except:
	    spans.append(())
    #spans = [(stri.index(token), stri.index(token) + len(token)) for token in tok]
    iden = 1
    for i in range(len(tokens)):
        new.write(str(iden) + '\t' + tokens[i] + '\t' + str(spans[i][0]) + ' ' + str(spans[i][1]) + '\n')
        ann.write('T' + str(iden) + '\t' + 'suggestion ' + str(spans[i][0]) + ' ' + str(spans[i][1]) +
                  '\t' + tokens[i] + '\n' + '#' + str(iden) + '\t' + 'AnnotatorNotes T' + str(iden) + '\thahaha!' + '\n')
        iden += 1
    new.close()
    ann.close()
    #spans = list(sp(stri, '\s+|[.,?;!]+(?![.,?;!])'))