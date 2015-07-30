#coding: utf-8
"""generates .ann-file with marked typos.
   note: language weight and typo causes not included
"""

import codecs, re, subprocess as sup

text = codecs.open('Burdukova_blog.txt', 'r', 'utf-8')
tkn = [i.split() for i in codecs.open('Burdukova_blog.tkn', 'r', 'utf-8').readlines()]
ann = codecs.open('Burdukova_blog.ann', 'w', 'utf-8')

counter = 1
for i in range(len(tkn)):
    correction = re.findall(': (.*?),', sup.Popen([u'aspell', '-a', '-l', 'en'], stdin=sup.PIPE, stdout=sup.PIPE).communicate(tkn[i][0].encode('utf-8'))[0])
    if correction != []:
	ann.write('T%s	Word_choice %s %s	%s\n#%s	Annotator_notes T%s	%s\n' % (counter, tkn[i][1], tkn[i][2], tkn[i][0], counter, counter, correction[0]))
	counter += 1
ann.close()