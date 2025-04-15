
f1=open('Particular.txt')
count= dict()
for line in f1:
  words=line.split()
  for word in words:
       if word not in count:
           count[word]=1
       else:
           count[word]+=1
print("myWallet=",count)
#1
count["CCards"]+=1
print("appending credit card",count)
#2
print( "photograph" in count)
#3
count["photograph"]=4
print("Photographs added",count)
#4
count.pop("photograph")
print("After popping Photograph",count)
count["photograph"]=4
print(count)
del count["photograph"]
print("After deleting Photograph",count)
#5
count=tuple(count)
print("tuple:",count)
#6
count=list(count)
count.sort()
print(count)
#7
val={1:'Dairy',2:'ccards',3:'dcards',4:'vcards'}
keys=list(val.keys())
keys.sort()
for s  in keys:
    print("{}=>{}".format(s,val[s]))