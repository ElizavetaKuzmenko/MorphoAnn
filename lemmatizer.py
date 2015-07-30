#!/bin/python
# coding: utf-8
# Extracting lemmas of words with Freeling
# author: Andrey Kutuzov
# GPL v 3.0
from __future__ import division
import subprocess as sp

def lemmatizer(x):
	lemmas = []
	tagged = sp.Popen([u'analyzer_client', u'40005'], stdin=sp.PIPE, stdout=sp.PIPE).communicate(x.encode('utf-8'))[0]
	tagged = tagged.strip().split('\n')
	#print tagged
	for word in tagged:
		word = word.split()
		if word:
		# and word[0] != ',' and word[0] != '.' and word[0] != '?' and word[0] != '!':
			lemmas.append(word[:-1])
	return lemmas
