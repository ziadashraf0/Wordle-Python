import enchant;
from random_word import RandomWords

dictionary = enchant.Dict("en_US")
secret=RandomWords().get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb",  minDictionaryCount=15   , maxDictionaryCount=100, minLength=5, maxLength=5)
secret=secret.lower()
def checkAlpha(wordle,result) :
 for alpha in wordle :
    if secret.__contains__(alpha):
        if secret.index(alpha) == wordle.index(alpha):
            result.append(1)
        else :
            result.append(-1)
    else:
        result.append(0)
 return secret
def printingResults(result) :
    for result in result:
        print(result, end=" ")
    print("")


def scanningInput() :
    print("enter a new word of 5 letters : ")
    wordle = input()
    while  len(wordle) !=5 or  dictionary.check(wordle) is False:
        wordle=input("enter a correct word of 5 letters : ")
    return wordle