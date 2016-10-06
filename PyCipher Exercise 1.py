#input the message
message = input('ur messeg')

#testing message input and its length to manually deter ranges
print (message, "\n")

print (len(message), " \n")

#for loop with decrement operator - DOperator must ! - stores in trans empty str var
n= len(message)
translated = ' '
p = n - 1
for i in range (p, -1, -1):
    translated = translated + message[i]
    p = p - 1

print (translated)
    
