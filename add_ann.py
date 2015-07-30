__author__ = 'liza55'

import re, codecs, os


def writing(f, link):
    spans = []
    ann_file = codecs.open(link + f, 'r', 'utf-8')
    ann = ann_file.read()
    ann_file.close()
    ann_again = codecs.open(link + f, 'r', 'utf-8')
    for line in ann_again.readlines():
        try:
            core = line.split('\t')[1]
            span = core.split(' ')[1] + ' ' + core.split(' ')[2]
            spans.append(span)
        except IndexError:
            continue
    last_T = re.findall('\nT([0-9]+)', ann, flags=re.U)
    if last_T == []:
        t = 1
    else:
        t = int(last_T[-1]) + 1
    additions = codecs.open('/home/lizaku/Experimental_annotation/' + f, 'r', 'utf-8')
    ann_file = codecs.open(link + f, 'w', 'utf-8')
    ann_file.write(ann)
    for line in additions.readlines():
        corr = line.split('\t', 1)[1]
        core = corr.split('\t')[0]
        span = core.split(' ')[1] + ' ' + core.split(' ')[2]
        if span not in spans:
            ann_file.write('T' + str(t) + '\t' + corr)
            t += 1
    ann_file.close()

#fs = os.listdir('/var/www/realec/data/Experiment_agreement/Andrey/')
#anns = [f for f in fs if f.endswith('.ann')]
link = '/var/www/realec/data/Experiment_agreement/NChukicheva/'
f_to_rewrite = ['1.ann', '10.ann', '11.ann', '12.ann', '13.ann', '14.ann', '2.ann', '20.ann', '21.ann', '22.ann', '23.ann',\
		'24.ann', '15.ann', '16.ann', '17.ann', '18.ann', '19.ann', '27.ann', '25.ann', '26.ann']
for f in f_to_rewrite:
    print f
    writing(f, link)