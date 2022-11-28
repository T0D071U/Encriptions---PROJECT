#imports
import random as rand
from random import choice

#setup
key="numberToLetter.txt"
numKey = rand.randint(100000,999999)
#functions


def seperator(string):
  fourE = ""
  list = []
  for i, char in enumerate(string):
    if i==0:
      fourE = "1{}".format(char)
    elif i + 1 == len(string):
      fourE += char + "2"
      list +=[fourE]
    elif len(fourE) != 10:
      fourE += char
    else:
      list += [fourE + "2"]
      fourE = "1{}".format(char)
  encripted = divider(list)
  return(encripted)

def divider(list):
  newList = []
  global numKey
  for i in list:
    num = int(i)
    mod = num % numKey
    quotient = num // numKey
    amount = "{}-{}".format(mod, quotient)
    newList += [amount]
  return(newList)  

def seperatorString(string):
  fourE = ""
  list = []
  for i, char in enumerate(string):
    if i + 1 == len(string):
      fourE += char
      list +=[fourE]
    elif len(fourE) != 3:
      fourE += char
    else:
      list += [fourE]
      fourE = char

def numFirst(string):
  new=""
  file = open(key, mode="r")
  values=[]
  for line in file:
    val = line.split(",")
    val.pop(1)
    values += val
  for i, char in enumerate(string):
    for list in values:
      set = list.split(":")
      if set[0] == char:
        new+=set[rand.randint(1,10)]
      
  encripted = seperator(new)
  return(encripted)


def encripts(sentence):
  randomizer = ''.join(choice((str.upper, str.lower))(c) for c in sentence)
  encriptedStr = numFirst(randomizer)
  return encriptedStr, numKey
  

#get functions

