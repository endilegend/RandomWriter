######################################
# Random Writer programming assignment
# Endi Troqe
# 13-09-2024
######################################

# import libraries
from random import randint, choice, random
import random

###########
# FUNCTIONS
###########
# returns a random seed of length level (or k) from the book
def get_seed(k, text):
    # pick a random index that represents the beginning of the seed in the book
    startindex = randint(0, len(text) - k)
    # return the random seed of length level (or k)
    seed = text[startindex: startindex + k]
    return seed

# returns a random next character given a seed from the book
def get_next_char(seed, text, k):

    # initialize the current index (where we begin to look in the book)
    find_index = 0
    # initialize the list of characters
    follows = []
    
    # continually find the seed in the book
    while (text.find(seed, find_index) != -1):
        # find the index of the seed in the book beginning at the current index
        find_index = text.find(seed, find_index)
        # abort if the seed is not found (or it's at the end of the book)
        if find_index == -1:
            break        
        # otherwise, add the next character to the list
        elif 0 <= find_index + k < len(text):
            char = text[find_index + k]
            follows.append(char)
        # update the index in the book
        find_index += 1
    
    # if there is at least one next character in the list of characters, return a randomly chosen on
    selectedchar = random.choice(follows)
    return selectedchar


######
# MAIN
######


# the level of analysis performed on the book 
k = int(input("Select level: "))
# the length of output to generate
length = int(input("Select length: "))
# the filename that contains the text of the book
book = "/Users/enditroqe/Desktop/csc201/books-1/hg-wells_the-time-machine.txt"

# grab the book
with open(book, "r") as f:
    text = f.read()
    text = text.replace("\n", " ")
    text = text.lower()


# initialize the output
output = ""

# pick a random seed of length level (or k)
seed = get_seed(k,text)
# get a random next character
next_char = get_next_char(seed, text, k)

# repeat as long as there isn't enough output yet
while len(output) <= length:
    # add it to the output
    output += next_char
    #recalculate the seed
    seed = seed[1:] + next_char
    # get a random next character
    next_char = get_next_char(seed, text, k)
    
# display the output
print (output)


