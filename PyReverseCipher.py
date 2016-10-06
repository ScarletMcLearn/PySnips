message = 'Hello!'
print (message, "\n")

print (len(message), " \n")

n= len(message)
translated = ' '
p = n - 1
for i in range (p, 0):
    translated = translated + message[i]
    p = p - 1

print (translated)
    
