import codecs
import json
import markovify
import nltk
import random
import re
import time
from glob import glob
from num2words import num2words
import dominate
from dominate.tags import *
import pdfkit
import wikipedia
novel = ' '

with open("wiki_now.txt") as f:
    wiki = f.read()
    mark_wiki = markovify.Text(wiki)

with open("Invasive_Species_Affirmation.txt") as i:
    read_into = i.read()
    mark_invas = markovify.Text(read_into)


wiki_read = wikipedia.page("Invasive species in the United States")
wiki_file_write = wiki_read.content
file = 'wiki_now' '.txt'
with codecs.open(file, "w", "utf-8-sig") as t:
    t.write(wiki_file_write)

final_model = markovify.combine([mark_wiki, mark_invas], [1,4])

for i in range(3500):

        novel += str(final_model.make_sentence())
        r = random.randint(0,100)

        if (r < 36):
            novel += "\n\n"

sectioned = novel.split("\n\n")

len(novel.split(" "))

text_output = open("fin.txt", "w")
text_output.write(novel)
text_output.close()
