import codecs, sys, re, random

ann1 = sys.argv[1]
ann2 = '/var/www/realec/data/' + ann1[:-4] + '.ann'
#ann1 = '/var/www/syntax/data/REALEC/disfluency/' + ann1
ann1lines = codecs.open(ann1, 'r', 'utf-8').readlines()
ann1errors = [line.strip() for line in ann1lines if re.search('^A[0-9]+\tSpelling_error', line) is not None and 'lemma' not in line]
#ann1spans = [line.strip().split('\t')[1].split(' ')[1:] for line in ann1lines if re.search('^T[0-9]+\t', line) is not None and re.search('T[0-9]+', line).group(0) in ann1errors]

ann2lines = codecs.open(ann2, 'r', 'utf-8').readlines()
ann2errors = [line.strip() for line in ann2lines if re.search('^T[0-9]+\t', line) is not None  and 'pos' not in line and 'lemma' not in line]

#ann2spans = [line.strip().split('\t')[1].split(' ')[1:] for line in ann2lines if re.search('^T[0-9]+\t', line) is not None and 'Spelling' not in line and  re.search('T[0-9]+', line).group(0) in ann2errors]

rel_retr = 0
#first = [int(span[0]) for span in ann2spans]
#second = [int(span[1]) for span in ann2spans]
#for span in ann1spans:
#    if int(span[0]) in first or int(span[1]) in second:
#	coincide += 1
#    else:
#	for s in range(len(first)):
#	    if int(span[0]) >= first[s] and int(span[1]) < second[s]:
#		coincide += 1
#print str(coincide) + '\t' + str(len(ann1spans)) + '\t' + str(len(ann2spans))
#precision = float(coincide)/len(ann1spans)
#recall = float(coincide)/len(ann2spans)

ann2texts = [line.strip().split('\t')[2] for line in ann2lines if 'pos' not in line and line.strip() in ann2errors]
ann1texts = [line.strip().split('\t')[2] for line in ann2lines if re.search('^T[0-9]+\t', line) is not None  and re.search('T[0-9]+', line).group(0) in ann1errors]
ann1sents = codecs.open(ann1[:-4] + '.txt.snt', 'r', 'utf-8').readlines()

arr = [0, 1]
retrieved = 0
for sent in ann1sents:
    r_error = random.choice(arr)
    for text in ann2texts:
	if text in sent and r_error == 1:
	    rel_retr += 1
	break
    if r_error == 1:
	retrieved += 1
#ann2sents = codecs.open(ann1 + '.orig.snt', 'r', 'utf-8').readlines()
##print ann1texts, ann2texts
##s1 = set()
##s2 = set()
##for text in ann1texts:
##    for sent in range(len(ann1sents)):
##	if text in ann1sents[sent]:
##	    s1.add(text)
##for text in ann2texts:
##    for sent in range(len(ann1sents)):
##	if text in ann1sents[sent]:
##	    s2.add(text)
##for el in s1:
##    if el in s2:
##	coincide += 1

print str(rel_retr) + '\t' + str(retrieved) + '\t' + str(len(ann2errors))