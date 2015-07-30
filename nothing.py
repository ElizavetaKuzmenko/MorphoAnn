from no_matter import token
from morpho_ann import morpho
import codecs

with open('Burdukova.tkn', 'w') as tkn_file:
    tkn_stream = token(codecs.open('Burdukova_blog.txt', 'r', 'utf-8').read())
    tkn_file.write(tkn_stream)

with open('Burdukova.ann', 'w') as ann_file:
    morpho_stream = morpho('Burdukova.tkn')
    ann_file.write(morpho_stream)