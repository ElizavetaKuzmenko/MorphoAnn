#!/bin/sh

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