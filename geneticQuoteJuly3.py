'''Genetic Quote Editing
July 3, 2018'''

import random

target = "I never go back on my word, because that is my Ninja way."
characters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.',?!"

def makeList():
    '''Returns a list of characters the same length as the target'''
    charList = [random.choice(characters) for i in range(len(target))]
    return charList

def score(myList):
    '''Returns one integer: the number of matches with target'''
    matches = 0
    for i in range(len(target)):
        if myList[i] == target[i]:
            matches += 1
    return matches

def mutate(mylist):
    '''Returns mylist with one letter changed'''
    newlist = list(mylist)
    new_letter = random.choice(characters)
    index = random.randint(0,len(target) - 1)
    newlist[index] = new_letter
    return newlist

random.seed()
bestList = makeList()
bestScore = score(bestList)

guesses = 0
improvements = 0

while True:
    guess = mutate(bestList)
    guessScore = score(guess)
    guesses += 1

    if guessScore <= bestScore:
        continue
    print(''.join(guess),guessScore,guesses)
    if guessScore == len(target):
        break
    bestList = list(guess)
    bestScore = guessScore
    
