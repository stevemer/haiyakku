import os
from flask import Flask
from YikYak import *
from haiku import is_haiku
from htmls import htmls

app = Flask(__name__)
# log to stderr
# log to stderr
import logging
from logging import StreamHandler
file_handler = StreamHandler()
app.logger.setLevel(logging.DEBUG)  # set the desired logging level here
app.logger.addHandler(file_handler)

HTML_MESSAGE = \
    """\
    <html>
      <head></head>
      <body>
        <h2>Hello Mary Douglass!</h2>
        <p>Here is your awesome haiyakku of the day<br>
        <p>{0}</p>
        </p>
      </body>
    </html>
    """

@app.route('/')
def hello():
    app.logger.warning("HELLO WORLD WHAT IS GOING ON!")
    wordcounts = dict()

    syllables = open("REALsyllables.txt", "rU").readlines()

    for line in syllables:
        try:
            line = line.strip()
            line = line.split('=')
            name = line[0]
            syllabi = line[1]
            count = 0
            for w in syllabi.split('-'):
                count += 1
            wordcounts[name] = count
            if name[-1] != 's':
                wordcounts[name + 's'] = count
        except: continue

    msg_list = dostuff()
    for msg in msg_list:
        msg = is_haiku(msg, app, wordcounts)
        if msg != "No haiku found!":
            line1 = []
            line2 = []
            line3 = []
            count = 0
            while count != 5:
                word = msg.pop(0)
                line1.append(word)
                count += wordcounts[word]
            count = 0
            while count != 7:
                word = msg.pop(0)
                line2.append(word)
                count += wordcounts[word]
            count = 0
            while count != 5:
                word = msg.pop(0)
                line3.append(word)
                count += wordcounts[word]
            stanza0 = ' '.join(line1)
            stanza1 = ' '.join(line2)
            stanza2 = ' '.join(line3)
            return htmls.format(stanza0, stanza1, stanza2)
            pass
    return "Couldn't find any decent haiyakkus!"

