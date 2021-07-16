import json

from datamuse import datamuse
api = datamuse.Datamuse()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def getWord(word):
    try:
        response = api.words(sp=word, md="d,p,f", max=1)
        if not response[0]:
            print(bcolors.FAIL + word + bcolors.ENDC)
        else:
            print(bcolors.OKGREEN + word + bcolors.ENDC)
            return response[0]
    except:
        print(bcolors.FAIL + word + bcolors.ENDC)

from concurrent.futures import ProcessPoolExecutor as PoolExecutor
wordList =[]
m = ""
def runthreads():
    with open("ospd.txt", "r") as f:
        words = f.read().split('\n')
        with PoolExecutor(max_workers=128) as executor:
            m = executor.map(getWord, words)
            executor.shutdown(wait=True)

        for r in m:
            if r:
                wordList.append(r)

        return

runthreads()
print(len(wordList))
with open("words.json", "w") as f:
    f.write(json.dumps(wordList))

