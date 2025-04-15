#1
Engineers=set()
Engineers.update(['Jane','John','Janice','Jack'])
print("Engineers:",Engineers)
#2
Manager=set()
Manager.update(['Jane','Jack','Susan','Zack'])
print("Managers:",Manager)
#3
for a in Engineers:
    print("Name Of Engineer is ---",a)
#4
mymanager=tuple(Manager)
print("Tuple of Managers:",mymanager)
#5
myengineer=list(Engineers)
print("Tuple of Engineers:",myengineer)
#6
Manager.add('Jenifer')
print("Jenifer added:",Manager)
#7
Engineer_manager=Engineers.union(Manager)
print("Engineers & Managers:",Engineer_manager)
#8
Engineers.difference_update(Manager)
print("Engineers who are not Managers:",Engineers)
#9
Engineers={'Janice', 'Jack', 'Jane', 'John'}
Manager={'Jack', 'Susan', 'Jane', 'Zack'}
Manager.intersection_update(Engineers)
print("Engineers who are managers:",Manager)
#10
Engineers={'Janice', 'Jack', 'Jane', 'John'}
Manager={'Jack', 'Susan', 'Jane', 'Zack'}
Manager.symmetric_difference_update(Engineers)
print(Manager)