#lecture practice

a = 2 
b = 2

c = 0

# while c < 1000:
   # c = c + a
   # b = a + c
    
   # if b > 200: 
      #  break

for i in range(0, 1000):
    c = c + a
    b = a * c

    if b > 200:
        break 