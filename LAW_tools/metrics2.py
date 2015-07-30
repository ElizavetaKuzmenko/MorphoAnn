import sys, codecs

coincide = 0
ann1spans = 0
ann2spans = 0
result = codecs.open(sys.argv[1], 'r', 'utf-8')
for line in result.readlines():
    line = line.strip()
    rel_retr, retr, rel = line.split('\t')
    coincide += int(rel_retr)
    ann1spans += int(retr)
    ann2spans += int(rel)

precision = float(coincide)/ann2spans
recall = float(coincide)/ann1spans

print 'precision', precision
print 'recall', recall