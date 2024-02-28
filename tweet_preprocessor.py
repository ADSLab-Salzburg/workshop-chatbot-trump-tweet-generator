#!/usr/bin/env python
# coding: utf-8

# # trump tweet preprocessor
# 
# [The Trump Archive](https://www.thetrumparchive.com/) is the source of all the data. Here the data is exported as csv, with only the the tweet text - no delimeter.
# 
# This scripts preprocesses those and stores them in the corresponding train/validation files.

from random import shuffle
import string

train_test_split = 0.11

with open("trump.csv", "r") as f:
    text_read = f.readlines()

n_val = int(len(text_read) * train_test_split)
shuffle(text_read)

text_test, text_train = text_read[:n_val], text_read[n_val:]


characters = list(string.printable)
characters.remove('\x0b')
characters.remove('\x0c')

for idx, tweet in enumerate(text_test):
    text_test[idx] = ''.join([c for c in tweet if c in characters])

for idx, tweet in enumerate(text_train):
    text_train[idx] = ''.join([c for c in tweet if c in characters])

text_test = ' '.join(text_test)
text_train = ' '.join(text_train)

text_train, text_test = text_train.replace("\n", " "), text_test.replace("\n", " ")

with open("trump_train.txt", "w") as f:
    f.write(text_train)
with open("trump_val.txt", "w") as f:
    f.write(text_train)

