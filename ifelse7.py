#1
a=int(input("Enter the units:"))
if a <= 100:
    b=a*3
   
elif a <= 200:
        b = (100 * 3) + ((a - 100) * 5)
else:
        b= (100 * 3) + (100 * 5) + ((a - 200) * 10)
print("electricity bill:",b)
#2
a=int(input("Enter the price of bike:"))
if a <= 50000:
    b=(a*5)/100
   
elif a >50000 and a<=100000:
        b = (a*10)/100
else:
        b=(a*15)/100 
print("road tax to be paid:",b)
#3
a=str(input("Enter the City:"))
if a=="Delhi":
        print("RED FORT")
elif a=="Jaipur":
        print("JAL MAHAL")
elif a=="Agra":
        print("TAJ MAHAL")
else:
        print("Not found")
#4
even=0
odd=0
for a in range(12,38):
        if a%2==0:
                even+=a
        else:
                odd+=a
print("sum of even:",even)
print("sum of odd",odd)
#5
x=int(input("enter the number:"))
rev=0
while  x:
        rev=rev*10+x%10
        x//=10
print("reversed Number",rev)
#6
import math
n = int(input("Enter the value of n: "))
sum_series = 0
for i in range(1, n + 1):
    sum_series += 1 / math.factorial(i)
print(f"Sum of the series is:{sum_series}")

#7
a=int(input("Enter the start of range"))
b=int(input("Enter the end of range"))
b+=1
even=0
odd=0
for num in range(a,b):
        if num%2==0:
                print(num)
#8
for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()