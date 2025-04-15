speed=float(input("speed in km/hr \t"))
x=speed*1000
y=(speed*1000)/3600
print("speed in m/hr \t",x)
print("speed in m/sec \t",y)
#1
Temp_centigrate=float(input("Enter temperature in celcius:"))
x=(1.8*Temp_centigrate)+32
print("Temp in F is",x)
#3
a=float(input("Sub 1 mark:"))
b=float(input("Sub 2 mark:"))
c=float(input("Sub 3 mark:"))
d=float(input("Sub 4 mark:"))
e=float(input("Sub 5 mark:"))
f=float(input("Sub 6 mark:"))
per=((a+b+c+d+e+f)/600)*100;
print("percentage :", "%.1f"%per)    #"%.2f"% for limited decimal points
#4
a=str(input("Enter a string:"))
b=str(input("Enter a string:"))
if(a==b):
    print("true")
else:
    print("false")
    #6
def count_occurrences(lst):
    counts = {}
    
    for element in lst:
        # Check if the element is already in the counts dictionary
        if element not in counts:
            # Count how many times the element appears in the list using 'in' operator
            counts[element] = lst.count(element)
    
    return counts

# Example usage
my_list = [1, 2, 2, 3, 4, 1, 5, 2, 3, 4]
result = count_occurrences(my_list)
print(result)