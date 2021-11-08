first = input 

count = 0

for i in range(0, 10,): 
  if i % 2 == 0:
      count = count + i

print (count)


# finding which numbers are multiples of 2 and then the sum of the results e.g 2+4+6+8+10

#task 2 and find how many of each letter there is 

alphabets = "abcdefghijklmnopqrstuvwxyz"
txt = "the quick brown fox jumps over the lazy dog"

for alpha in alphabets:
    count = 0 
    
    for i in txt:
        if alpha == i:
            count = count + 1
            
    print(alpha + " " + str(count))      

# print(alpha + " " + i) = this prints it as a double loop thingy 

alphabets = "abcdefghijklmnopqrstuvwxyz"
txt = "the quick brown fox jumps over the lazy dog"

for alpha in alphabets:
    count = 0

    for i in txt:
        if alpha == i or alpha.upper() == i:
            count = count + 1 

    print(alpha + " " + str(count)) 

# task 3 remainder

first = 10 #dividend
second = 2 #diviser
result = 0 #result is 10 devided by 2

while first >= second: #while this condition is true it will continue printing the loop below 
    first = first - second  
    result = result + 1 #count how many times you did the subtraction 

print(result)
print("remainder" + str(first)) #you cant have a variable on its own, you have to string the variable 







