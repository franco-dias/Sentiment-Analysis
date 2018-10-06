#!/usr/bin/env python
# -*- coding: utf-8 -*-


import nltk

stemmer = nltk.stem.RSLPStemmer()

frase = 'meu nome e Gabriel Franco, tenho 21 anos e sou aluno da universidade federal de uberlandia'

splitted = frase.split(' ')
stemmed = set()

for word in splitted:
	stemmed.add( stemmer.stem(word) )

stopwords = nltk.corpus.stopwords.words('portuguese')

removed_stopwords = set()
for stopword in stopwords:
	removed_stopwords.add(stopword)

print(stemmed - removed_stopwords)

#filter (lambda x: x not in stopwords, stemmed) 




