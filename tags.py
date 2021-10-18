from itertools import permutations
import spacy

nlp = spacy.load("en_core_web_lg")
doc = nlp("apple pear banana fruit clean service")

feats = '\t\t'.join(list(map(str, doc.doc)))
print(f"\t\t{feats}")
for a in doc:
    print(f"{a} -> \t(", end='')
    tup = ',\t\t'.join(map(str, map(lambda x: a.similarity(x) > 0.3, doc)))
    print(tup, ')')
