#!/bin/sh

echo 'Tokenizing and lemmatizing...'
for i in *.txt
    do
	cat $i | analyzer_client 30000 | python freeling2conll.py > $i.conll1
	cat $i | analyzer_client 40005 | cut -d ' ' -f 4 > $i.conll2
	paste $i.conll1 $i.conll2 > $i.conll
	rm $i.conll1
	rm $i.conll2
    done
