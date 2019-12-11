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


flora = ["Purple Loosestrife", "Japanese Honeysuckle", "Japanese Barberry", "Norway Maple", "English Ivy", "Kudzu", "Privet", "Black Alder", "Yellow Rocket", "Guineagrass"]

all_texts = []
#
# for fname in glob("wikiCorpus/*txt"):
#     cur_text = open(fname).read()
#     all_texts.append(cur_text)
#
# print(all_texts)

# Load input text for the Markov models
with open("cFinal.txt") as f:
    text_relationship1 = f.read()
    mark_text_rel = markovify.Text(text_relationship1)

with open("flora_BlackAlder.txt") as a, open("flora_EnglishIvy.txt") as b:
    black_adler = a.read()
    mark_black_adler = markovify.Text(black_adler)
    all_texts.append(black_adler)

    english_ivy = b.read()
    all_texts.append(english_ivy)
    mark_english_ivy = markovify.Text(english_ivy)


with open("flora_Guineagrass.txt") as c, open("flora_JapaneseBarberry.txt") as d:
    guineagrass = c.read()
    all_texts.append(guineagrass)
    mark_guinea = markovify.Text(guineagrass)

    japanese_barberry = d.read()
    all_texts.append(japanese_barberry)
    mark_barb = markovify.Text(japanese_barberry)

with open("flora_JapaneseHoneysuckle.txt") as e, open("flora_Kudzu.txt") as g:
    japanese_honeysuckle = e.read()
    all_texts.append(japanese_honeysuckle)
    mark_honey = markovify.Text(japanese_honeysuckle)

    kudzu = g.read()
    all_texts.append(kudzu)
    mark_kudz = markovify.Text(kudzu)

with open("flora_NorwayMaple.txt") as h, open("flora_Privet.txt") as i:
    norway_maple = h.read()
    all_texts.append(norway_maple)
    mark_maple = markovify.Text(norway_maple)

    privet = i.read()
    all_texts.append(privet)
    mark_privet = markovify.Text(privet)

with open("flora_PurpleLoosestrife.txt") as j, open("flora_YellowRocket.txt") as k:
    purple_strife = j.read()
    all_texts.append(purple_strife)
    mark_strife = markovify.Text(purple_strife)

    yellow_rocket = k.read()
    all_texts.append(yellow_rocket)
    mark_rocket = markovify.Text(yellow_rocket)

#print(all_texts[3])

text_model = markovify.combine([mark_rocket, mark_text_rel ], [6,1])


for x in flora:
    T = "\n" + "\n" + "<h2>" + x.capitalize() + "</h2>" + "\n" + "\n"

    try:
        wiki_read = wikipedia.page(x)
        wiki_file_write = wiki_read.content
        file = 'flora_%s' %x + '.txt'
        with codecs.open(file, "w", "utf-8-sig") as t:
            t.write(wiki_file_write)
    except wikipedia.exceptions.DisambiguationError as e:
        wiki = " "

for i in range(500):

        novel += str(text_model.make_sentence())
        r = random.randint(0,100)

        if (r < 36):
            novel += "\n\n"

sectioned = novel.split("\n\n")

len(novel.split(" "))





text_output = open("Output10.txt", "w")
text_output.write(novel)
text_output.close()
