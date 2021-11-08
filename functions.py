def greet(forename):
    greeting = "Hi, " + forename + " :)\nWelcome to the club"
    
  

    return greeting

print(greet("vikki"))



def pig_latin(text):
  words = text.split()
  pigg = []

  for word in words:
    word = word[1:] + word[0] + 'ay'
    pigg.append(word)

  return ' '.join(pigg)

print(pig_latin("hello how are you"))



""" whatever is within the three quotation marks, it will define the code """

def name(first, second = ""): 
  if second == "":
    print ("hello" + first )
  else:
    print("hi" + first + " " + second + " ")

  first = input("first name: ")
  second = input("second name: ")

  name(first, second)

#class.py

consonant = "bcdghjklmnpqrstvwxyz"

word = input("type a word" + " ")

cut_index = -1 

for i, letter in enumerate(word):
  if letter not in consonant:
    cut_index = i
    break 

result = ""

for number2 in range (cut_index, len(word)):
  result += word[number2]
  print(word[number2], end = "")

for number in range (0, cut_index) :
  print (word[number], end = "")

print(end = "ay")
print()
