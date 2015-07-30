# coding: utf-8
# author: liza
from lemmatizer import lemmatizer
import codecs

def morpho(tkn):
    position = 1
    tkn = codecs.open(tkn, 'r', 'utf-8')
    spans = []
    tokens = ''
    for line in tkn.readlines():
	tokens += line.split('\t')[1] + ' '
	spans.append(line.strip().split('\t')[2])
    morpho_ann = u''
    lemmas = lemmatizer(tokens)
    for l in range(len(lemmas)):
	morpho_ann += 'T' + str(position) + '\tpos_' + lemmas[l][2] + ' ' + spans[l] + '\t' + '\n' + '#' + str(position) +\
		  '\tAnnotatorNotes T' + str(position) + '\t' + 'lemma = \'' + lemmas[l][1] + '\'\n'
	position += 1
    return morpho_ann