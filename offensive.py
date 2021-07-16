import json
from better_profanity import profanity
from concurrent.futures import ProcessPoolExecutor as PoolExecutor

def fun(w):
    print(w)
    return profanity.contains_profanity(w)

with open("words.json") as f:
    words = json.loads(f.read())

wordNames = []
for word in words:
    wordNames.append(word['word'])

profanityList = []
with PoolExecutor(max_workers=16) as executor:
    profanityList = list(executor.map(fun, wordNames))

for count, word in enumerate(words):
    words[count]['profane'] = bool(profanityList[count])

with open("wordsprof.json", 'w') as f:
        f.write(json.dumps(words))
