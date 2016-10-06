n=int(input('n:'))
x1=float(input('x:'))
y1=float(input('y:'))
A=0
x1s=x1
y1s=y1
for i in range (1,n):
    x=float(input('x:'))
    y=float(input('y:'))
    A=A+x1*y-y1*x
    x1=x
    y1=y
    A=(A+(y*y1s-y*x1s))/2.0
if A<0:
    A=-A
print (A)
