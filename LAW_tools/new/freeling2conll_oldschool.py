#!/bin/python2
# coding:utf-8

import sys

counter = 0
for line in sys.stdin:
    res = line.strip().split()
    if len(res) == 4:
	(token,lemma,tag,prob) = res
	counter += 1
    else:
	print ''
	counter = 0
	continue
    if tag.startswith('F'):
	tag = lemma
    print counter,'\t',token.strip()+'\t'+lemma.strip()+'\t'+tag.strip()+'\t'+tag.strip()+'\t'+'_'+'\t'+prob.strip()
