#setup
key="numberToLetter.txt"
numKey = 0

#functions
def decripts(str, key):
  global numKey
  numKey=key
  seperatedList = str.split('\', \'')
  decripted = ""
  for i in seperatedList:
    decripted += multiplier(i)
  return decripted
  
def multiplier(string):
  list = []
  values= string.split("-")
  for i in values:
    v=""
    for pos, char in enumerate(i):
      if char == '\'': continue
      v  += char
    list += [v]
  mod = int(list[0])
  quotient = int(list[1])
  num = (quotient * int(numKey)) + mod
  value = cleaner(str(num))
  return value

def cleaner(number):
  value = ""
  for i, num in enumerate(number):
    if i == 0 or i+1 == len(number): continue
    value += num
  value = seperator(value)
  return value
  

def seperator(str):
  number = []
  value = ''
  for i, char in enumerate(str):
    if i == 2 or i==5 or i==8:
      value += char
      number += [value]
      value = ''
    else:
      value += char
  value = finder(number)
  return value

def finder(list):
  file = open(key, mode="r")
  new = ""
  values=[]
  for i in list:
    for line in file:
      val = line.split(",")
      val.pop(1)
      values += val
    for lists in values:
      set = lists.split(":")
      if i in set:
        new += set[0]
  return new.lower()

