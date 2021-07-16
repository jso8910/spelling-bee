import json
from string import ascii_lowercase
import random
import sys

with open("wordsNoProf.json") as f:
    j = json.loads(f.read())

while True:
    nj = []
    letters = random.sample(ascii_lowercase, k=7)
    middle_letter = letters[0]
    panagrams = []
    print(f"Trying {letters}")
    for word in j:
        if len(word['word']) > 3 and middle_letter in word['word'].lower() and all(c in letters for c in word['word'].lower()):
            nj.append(word['word'])
    for word in nj:
        if set(word) >= set(letters):
            if len(panagrams) == 0:
                print(nj)
                print(len(nj))
            panagrams.append(word)

    if len(panagrams) > 0:
        print(f"Panagrams: {panagrams}")
        print(f"Center letter: {middle_letter}")
        print(f"Other letters: {' '.join(letters[1:])}")
        print(f"Number of words: {len(nj)}")
        print(f"Words: {nj}")
        tocontinue = input("Do you want to continue trying for more words? [y/N] ")
        if tocontinue.lower() != 'y':
            break

