from nltk.corpus import cmudict
import os

def nsyl(word):
  return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]

d = cmudict.dict()
missing_words = set()
missingwordslist = open("missing_words.txt", "rU").readlines()
wordslist = open("REALsyllables.txt", "a")

for word in missingwordslist:
    word = word.strip()
    missing_words.add(word)

for word in missing_words: 
    print word
    try: count = nsyl(word)
    except: continue
    word_rep = ["syl"] * count
    word_rep = '-'.join(word_rep)
    total = word + "=" + word_rep
    wordslist.write(total + "\n")

os.system("rm missing_words.txt") 

