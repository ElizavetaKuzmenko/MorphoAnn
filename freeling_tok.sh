#!/bin/sh
for i in *.txt
do
cat $i | analyzer_client 40005 | cut -d ' ' -f 1 > $i.tok
done