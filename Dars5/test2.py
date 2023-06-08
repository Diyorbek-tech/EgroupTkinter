import math

n=int(input())
a=0
b=3
for i in range(1,int(math.sqrt(n))):
    a+=(i*b)
    b+=2
print(a+(n-int(math.sqrt(n))**2+1)*int(math.sqrt(n)))

