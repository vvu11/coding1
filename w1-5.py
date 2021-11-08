#  week 1:write a program that outputs even when no. is even and odd when no. is odd

while True:
    try:
        number =  float(input("input a number: ")) #float allows for decimal values
        if number % 2 == 0: #this is remainders: so the value is 0 and when we put our value on it,
            print("{0} is even number".format(number)) #if this statement is true 
        else: 
           print("{0} is odd number".format(number))  #if the statement is not true a.k.a cant be divisable by 2
    except ValueError:
         print("that is not a number")


# ? need to find out how to make it so that the code doesnt see decimals as odd
# code doesnt stop ? help :')

# week2: 
#task1: given 3 positive integers, find the sum of all numbers between the first 2 that are a multiple of the third

first = input 

count = 0

for i in range(0, 10,): 
  if i % 2 == 0:
      count = count + i

print (count)

#task2:given a string of text, print the no. of times each letter of the alphabet appears

alphabets = "abcdefghijklmnopqrstuvwxyz"
txt = "its beginning to look a lot like christmas, everywhere you gop"

for alpha in alphabets:
    count = 0

    for i in txt:
        if alpha == i or alpha.upper() == i:
            count = count + 1 

    print(alpha + " " + str(count)) 


#task3: implement division as a series of subtraction. the program will report the remainder if there is one

first = 10 #dividend
second = 2 #diviser
result = 0 #result is 10 devided by 2 (it always starts at value 0)

while first >= second: #while this condition is true it will continue printing the loop below 
    first = first - second  
    result = result + 1 #count how many times you did the subtraction 

print(result)
print("remainder" + str(first)) #you cant have a variable on its own, you have to string the variable 


#week3
#task1: make a function that takes 2 arguments + prints a greeting according to the arguments

def name(first, second = ""): 
  if second == "":
    print ("hello" + first )
  else:
    print("hi" + first + " " + second + " ")

  first = input("first name: ")
  second = input("second name: ")

  name(first, second)

#task2: write a function that turns any english word into pig latin 

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


