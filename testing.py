import wikipedia
import nltk
from pprint import pprint
from collections import Counter

def getposdict(term):

    searchresults=wikipedia.search(term, results=5)
    newlistoftup = []
    pos_dict = {}
    for sr in searchresults:
        article1 = wikipedia.page(sr)
        text = nltk.word_tokenize(article1.content)
        listoftup = nltk.pos_tag(text)

        for tup in listoftup:
            if tup[1] not in pos_dict.keys():
                pos_dict[tup[1]]=[tup[0]]
            else:
                pos_dict[tup[1]].append(tup[0])

    for k in pos_dict.keys():
        wordskey = zip(Counter(pos_dict[k]).keys(), Counter(pos_dict[k]).values())

        pos_dict[k] = sorted(wordskey ,key=lambda pair: pair[1], reverse=True)
    # pprint(pos_dict['JJ'])
    return pos_dict

pos_dict = getposdict("Harry Potter")


topsixlst = []
for i in pos_dict['JJ'][:6]:
    topsixlst.append(i[0])

print topsixlst