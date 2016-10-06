'''b = 1
while b!=10:
    print (b)
    b += 1
'''
'''
b = int(input('To B'))
while b!=-1:
    print (b)
    b = int(input('b'))
'''

'''
b = (input('To B'))
while b!= '.'
:
    print (b)
    b = (input('b'))
'''

'''
b = float(input('To B'))
while b!=3.142:
    print (b)
    b = float(input('b'))
'''

'''
for i in range (0, 100):
    print (i)
'''

'''
b = 0
while b!=100:
    print (b)
    b +=1
'''

'''
b = 42
while b!= 16:
    print ((b)," ",) #singleline_nobreak
    b -= 1
'''

'''
for b in range (42, 17, -1):
    print (b)'''

'''
b = 2.25
while not ( b > 4):
    print (b)
    b +=0.25
'''
'''
a = int(input('a'))
b = int(input('b'))

for i in range (a, b+1):
    print (i)
'''

'''
a = int(input('a'))
b = int(input('b'))
c = 1

while c<11:
    if (a>b):
        c+=1
        
    c += 1
    
    a = int(input('a'))
    b = int(input('b'))
    else:
        

print (a)
print (b)
1
'''

'''
it = iter(iterable)
    first = next(it)     # Raises an exception if the input is empty
    minimum = maximum = cumsum = first
    n = 1
    for x in it:
        n += 1
        cumsum += x
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    average = cumsum / float(n)
    return minimum, average, maximum'''

we'''
Number = int(input("Please Enter any Number: "))
Reverse = 0
while(Number > 0):
    Reminder = Number %10
    Reverse = (Reverse *10) + Reminder
    Number = Number //10
 
print("\n Reverse of entered number is = %d" %Reverse)
'''
n = int(input('number'))
flip = 0
while (n>0):
    rem = n %10
    flip = flip*10 + rem
    n = n/10
    print (flip)

print( flip)
