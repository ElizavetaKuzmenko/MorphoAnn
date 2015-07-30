#!/bin/sh

echo 'Tokenizing and lemmatizing...'
for i in *.txt
do
cat $i | analyzer_client 40005 | python freeling2conll.py > $i.conll
done

echo 'Converting to standoff...'

for i in *.conll
do
python conllXtostandoff.py -o test2/ $i
done

rm *.txt.conll

cd test2/

echo 'Extracting tokens...'

for i in *.ann
do
cat $i | cut -f 1,3 > $i.tkn
done

echo 'Spellchecking...'

for i in *.ann
do
python /var/www/learner_preprocess/LAW_tools/aspell.py $i
done

rm *.tkn

rename .txt.conll. . *

echo 'Cleaning annotations...'

sed -i -e 's/PRP\$/PRP_/' *.ann
sed -i -e 's/_question_/question/' *.ann
sed -i -e 's/\t,/\tcomma/' *.ann
sed -i -e 's/\t(/\tprnts1/' *.ann
sed -i -e 's/\t)/\tprnts2/' *.ann
sed -i -e 's/\t’/\tapostrophe/' *.ann
sed -i -e 's/_period_/period/' *.ann
sed -i -e 's/_colon_/colon/' *.ann
sed -i -e 's/_amp_/amp/' *.ann
sed -i -e 's/_exclamation_/exclamation/' *.ann
sed -i -e 's/\t-/\tdash/' *.ann
sed -i -e 's/\t…/\tdots/' *.ann

echo 'Done!'