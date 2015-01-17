def is_haiku(msg, wordcounts):
    missing = open("missing_words.txt", "a")
    words = msg.split(' ')
    count = 0
    w = []
    for word in words:
        word = ''.join([c for c in word.lower().strip() if c.isalnum()])
        if not len(word): continue
        #word = ''.join([x for x in word.lower() if isalpha(x)])
        if word in wordcounts:
            print (word + " " + str(wordcounts[word]))
            count += wordcounts[word]
            w.append("{0}: {1}".format(word, wordcounts[word]))
        else: 
            count += 1
            w.append("{0}: {1}".format(word, "ONE"))
            missing.write(word + "\n")
    w = '<p>' + '</p><p>'.join(w) + '</p>'
    msg = msg + w
    missing.close()
    return msg, count
