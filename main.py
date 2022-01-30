from helpers import scanningInput, checkAlpha, printingResults
# 0  letter is not in any spot -----  -1 letter is in the word but in the wrong spot ------ 1  letter is in the correct spot
result =[]
wordTrials=0
while wordTrials <5:
    wordle =scanningInput()
    secret= checkAlpha(wordle,result)
    printingResults(result)
    if result.__contains__(0):
        result=[]
        wordTrials = wordTrials+1
        if wordTrials==5:
            print ('secret word is :  ' ,secret)
    else:
        print("You Win")
        break