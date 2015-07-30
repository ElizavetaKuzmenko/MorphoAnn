#!/bin/python2
# coding:utf-8

import sys
from itertools import izip_longest

counter = 0
for line in sys.stdin:
    res = line.strip().split()
    if len(res) > 1:
	token = res[0]
	variants = res[1:]
    else:
	print ''
	counter = 0
	continue
    counter += 1
    variants2 = list(izip_longest(*[iter(variants)]*3))
    tags = []
    probs = []
    for i in variants2:
	if len(i) == 3:
	    (lemma,tag,prob) = i
	    if tag.startswith('F'):
		tag = lemma
	    tags.append(tag)
	    probs.append(prob)
    
    print counter,'\t',token.strip()+'\t'+lemma.strip()+'\t'+' '.join(tags)+'\t'+' '.join(tags)+'\t'+'_'+'\t'+' '.join(probs)
