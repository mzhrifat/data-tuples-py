"""
Tuples
-ORDERS
-Allow duplicates
-Heterogeneous
-fIXED sizes
_immutable data type

tuple methods
-count():return no.of occurences TIMES A specified value appars in the tuple
-index():Returns the index of the first occurence appears in the tuple

Converting between Lists anD Tuples
-Tuple slicing
-looping Through a Tuple

tuples use case
_Immutable data storage
-Returm multiple values
-fixes collecyios
-database records
-
"""


""""
fruits=("apple","banana","cherry",1,True)
print(id(fruits))
print(fruits)
"""
"""
numbers=(1,2,3,4,5)
valueCount=numbers.count(1)
print(valueCount)
"""
numbers=(1,2,3,2,4,2)
valueIndex=numbers.index(3)
print(valueIndex)

fruits=("apple","banana","cherry","MANGO","gRAPE")

print(fruits[1:3])

ruits=("apple","banana","cherry","MANGO","gRAPE")
for item in fruits:
print(item)