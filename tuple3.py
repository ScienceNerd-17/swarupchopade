myTuple=(10,20,30)
yourTuple=("Pune", "Mumbai", "Delhi")
mixTuple=('Foo',[1,2,3], 'True')
nested_tuple=(('Wes McKinney', 'Python for Data Analysis', 'O Reilly Media'), ('Mark Lutz', 'Programming Python', 'O Reilly Media'), ('Charles Severance', 'Python for Everybody', 'Blumenberg'))

#1
print("Ourtuple=",myTuple+yourTuple)

#2
myTuple=list(myTuple)
print(myTuple)
myTuple.reverse()
print(myTuple)
#3
District,state,national=yourTuple
print("District:",District)
print("State:",state)
print("National:",national)
#4
print(mixTuple)
#5
X=mixTuple[1]
X.append(4)
print(mixTuple)
#6
print(myTuple+myTuple)
print(myTuple*2)
print(yourTuple+yourTuple)
print(yourTuple*2)
#7
nameofauthor,nameofbook,nameofpublisher=nested_tuple[0]
print("Name of Author:",nameofauthor)
print("Name of Book:",nameofbook)
print("Name of Publisher:",nameofpublisher)