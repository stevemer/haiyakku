
def check575(haiku, app, wordcounts):
    index = 0
    count = 0
    while count < 5:
        if index < len(haiku):
            count += wordcounts[haiku[index]]
            index += 1
        else:
            return False
    if count > 5: return False
    while count < 12:
        if index < len(haiku):
            count += wordcounts[haiku[index]]
            index += 1
        else:
            return False
    if count > 12: return False
    while count < 17:
        if index < len(haiku):
            count += wordcounts[haiku[index]]
            index += 1
        else:
            return False
    if count > 17: return False
    if index < len(haiku) - 1: return False
    else: return True 

def is_haiku(msg, app, wordcounts):
    missing = open("missing_words.txt", "a")
    words = msg.split(' ')
    count = 0
    bad_count = 0
    w = []
    haiku_msg = list()
    for word in words:
        # Strip out all weird characters and whitespace.
        word = ''.join([c for c in word.lower().strip() if c.isalnum()])
        # If there's nothing left after stripping that garbage, just skip right over the word.
        if not len(word): continue
        # Check if the word is in our dictionary already.
        if word in wordcounts:
            # Add the count to our running syllable count
            count += wordcounts[word]
            haiku_msg.append(word)
        else: 
            # We can't find the word in our dictionary.
            bad_count += 1
            missing.write(word + "\n")
    if bad_count: return "No haiku found!"
    # Here we begin our logic    

    app.logger.warning("Starting parsing: {}".format(haiku_msg))
    if count == 17 and check575(haiku_msg, app, wordcounts):
        return haiku_msg
    elif count > 17:
        # make copy first
        haikulist = []
        for hword in haiku_msg:
            haikulist.append(hword)
        stopwords = [x.strip() for x in open("stopwords.txt", "rU").readlines()]
        stopword_index = 0
        countcopy = count
        message_index = 0
        while count > 17 and stopword_index < len(stopwords):
            while message_index < len(haikulist):
                if haikulist[message_index] == stopwords[stopword_index]:
                    haikulist.pop(message_index)
                    try:
                        count -= wordcounts[stopwords[stopword_index]]
                    except KeyError:
                        count -= 1
                    if count == 17 and check575(haikulist, app, wordcounts):
                        return haikulist
                message_index += 1
            stopword_index += 1

        count = countcopy 
        while count > 17:
            last_word = haiku_msg.pop()
            count -= wordcounts[last_word]
            if count == 17 and check575(haiku_msg, app, wordcounts):
                return haiku_msg 
    elif count < 17 and count >= 12:
        for i in range(17 - count):
            haiku_msg.append("ha")
        if check575(haiku_msg, app, wordcounts): 
            return haiku_msg
    return "No haiku found!"
                        
