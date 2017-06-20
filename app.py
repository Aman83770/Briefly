from __future__ import division

#lsa modules
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


#lxa
from sumy.summarizers.lex_rank import LexRankSummarizer 


import nltk
import numpy as np
from nltk.book import *
from nltk.tokenize import sent_tokenize, word_tokenize
import math
import random
import time


start_time = time.clock()
from flask import Flask, render_template, request
from results import results
from learning_algo import Learning


app = Flask(__name__)



    

@app.route('/')

def home():
    return render_template('index.html')


@app.route('/lex')

def home2():
    return render_template('index2.html')


if __name__ == '__main__':
    app.run()
