import os
from flask import Flask
from YikYak import *
from haiku import is_haiku

app = Flask(__name__)

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
    wordcounts = dict()

    syllables = open("REALsyllables.txt", "r").readlines()

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
        msg, count = is_haiku(msg, wordcounts)
        if count == 17:
            return HTML_MESSAGE.format(msg)
    return "Couldn't find any of them!"

