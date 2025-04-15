# pandas dataframe
import pandas as pd
mydataset = {
   'cars': ["BMW", "Volvo", "Ford"],
   'passings': [3, 7, 2]
 }
m = pd.DataFrame(mydataset)
print(m)

# pandas dataseries
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

# give name to labels
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print(myvar["y"])

# pandas series from dictionary
import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
s=pd.Series(calories,index=["day1"])
print(s)

# dataframe from two series
import pandas as pd
data = {
   "c": [420, 380, 390],
         "d": [50, 40,77]
 }
m = pd.DataFrame(data)
print(m)
print(m.loc[1])
print(m.loc[[0, 1]])

import pandas as pd
data = {
   "calories": [420, 380, 390],
   "duration": [50, 40, 45]
 }
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df) 

# Read csv file
import pandas as pd
df = pd.read_csv('data.csv')
print(df) 

import pandas as pd
print(pd.options.display.max_rows) 

import pandas as pd
df = pd.read_csv('data.csv')
print(df.head(10))


 

 

