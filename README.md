# spelling-bee

Here is a basic overview of all of the files and how to use them.

First, `ospd.txt`. This file comes from this Github repo which contains a few curated dictionary files. This is the medium sized dictionary with 60-70k words. 

Then, our first Python script. These scripts aren't very well written (imports all over the place) but they function. This script is `dict.py`. This script opens up `ospd.txt` and uses the Datamuse API to get a json containing certain data for each word including the obscurity of the word. It runs 128 concurrent threads. It then dumps the results into `words.json` which is a very basic and not at all curated word list.

Another Python script marks profanity. `offensive.py` uses the better_profanity Python package to mark words that are offensive. By the way, if you do install it, install the 0.6.1 version. So run this command: `pip install better_profanity==0.6.1` because that has far better performance than the most recent version as noted in the repo. 

From here I don't have scripts so I will just list the commands I ran in the Python interpreter and what for.

To remove all offensive words and save it to a file called `wordsNoProf.json`

```py
import json
f = open('wordsprof.json')
j = json.loads(f.read())
open("wordsNoProf.json", "w").write(json.dumps([word for word in j if not word['profane']]))
```

To remove obscure words and save it to a file called `noObscureProfane.json`. This doesn't work well beacuse I have no idea how the score works and it is much easier to manually remove words.

```py
f = open('wordsNoProf.json"')
j = json.loads(f.read())
open("noObscureProfane.json", "w").write(json.dumps(sorted(j, key=lambda x: x['score'])[int(len(j) / 2) + int(len(j) / 7):]))
```
You can replace the `int(len(j) / 2) + int(len(j) / 7)` for different amounts cut out, in this case just over half (to be exact 9/14). 

The last script, `spellingwords.py`. This essentially tries as many combinations as possible until you get a combination of letters that has at least one panagram. It only returns words that have more than 3 letters, have the middle letter in them, and only letters in the letters list (which contains the middle letter). If it finds this and a panagram then it will notify you. It will tell you the panagrams, the letters, the words, and the number of words. It then lets you decide whether this isn't enough (if you look over the words and decide there aren't enough good words or whatever reasons). This means that you are highly unlikely to miss any words as there are 60 thousand words included. If you want to you can get the `unix-words` file from the Github repo that includes `ospd.txt` and repeat the steps just changing the filenames. However this will contain tens of thousands of useless words. I haven't been able to filter out the proper nouns. To do that I would need to scrape a website like Cambridge because it appears that there aren't any free APIs that give that information.
