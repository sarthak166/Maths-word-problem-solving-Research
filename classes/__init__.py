import spacy
import numpy as np
import pandas as pd
import nltk
from nltk.tag import StanfordNERTagger
from nltk.tag import StanfordPOSTagger
from nltk.parse.stanford import StanfordParser
from nltk.parse.stanford import StanfordDependencyParser
from nltk.tokenize import sent_tokenize, word_tokenize
import networkx as nx

nlp = spacy.load('en')

jar = '/home/puru/Documents/d/arithmetic/code/api/libs/stanford-postagger-2016-10-31/stanford-postagger.jar'
model = '/home/puru/Documents/d/arithmetic/code/api/libs/stanford-postagger-2016-10-31/models/english-left3words-distsim.tagger'
pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')

path_to_jar = '/home/puru/Documents/d/arithmetic/code/api/libs/stanford-parser-full-2015-04-20/stanford-parser.jar'
path_to_models_jar = '/home/puru/Documents/d/arithmetic/code/api/libs/stanford-parser-full-2015-04-20/stanford-parser-3.5.2-models.jar'
dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)
