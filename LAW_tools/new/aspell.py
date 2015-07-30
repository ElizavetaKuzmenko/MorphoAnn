#coding: utf-8
"""augment .ann-file with marked typos
"""

import codecs, re, subprocess as sup, sys

def correction(string):
    return re.findall(': (.*?),', sup.Popen([u'aspell', '-a', '-l', 'en'], stdin=sup.PIPE,\
    stdout=sup.PIPE).communicate(string.encode('utf-8'))[0])

def generate_ann(filename, strict = 'non-strict'):
    print filename
    ann = codecs.open(filename, 'a', 'utf-8')
    tkn = [tok.split() for tok in codecs.open(filename + '.tkn', 'r', 'utf-8').readlines() if tok.split() != []]
    tkn = [t for t in tkn if not t[0].startswith('#')]
    # strict mode stops aspell from checking some tokens:
    if strict == 'strict':
        tkn = [tok for tok in tkn if not re.match('[A-Z][a-z]+?', tok[0]) and not tok.startswith(u'#')]
    # applying aspell:
    for i in range(len(tkn)):
	try: 
	    local_correction = correction(tkn[i][1])
    	    if local_correction != []:
		line = 'A' + tkn[i][0][1:] + '\tSpelling_error ' + tkn[i][0] + '\n' + '#' + tkn[i][0][1:] + '\tAnnotatorNotes ' + tkn[i][0] + '\t' +  local_correction[0] + '\n'
		ann.write(line)
	except IndexError:
	    pass
    ann.close()

if __name__ == '__main__':
    generate_ann(*sys.argv[1:])