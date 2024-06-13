#List is a sequence of data type which is used to store a collection of data
#Lists can have duplicates values in it 

#creating a blank list 
List=[]
print("Blank list...")
print(List)

#creating a list of numbers
List=[23,78,90,56]
print("\nList of numbers:")
print(List)

#creating a list of string and accessing using index
List=["Majid","Faridah","Francis","Man From Nowhere"]
print("\nList items:")
print(List[0])
print(List[1])
print(List[2])
print(List[3])

#creating list with duplicates or multiple distinct elements
# Creating a List with
# the use of Numbers
# (Having duplicate values)
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of Numbers: ")
print(List)

# Creating a List with
# mixed type of values
# (Having numbers and strings)
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nList with the use of Mixed Values: ")
print(List)

#Accessing elements from a list
# Python program to demonstrate
# accessing of element from list

# Creating a List with
# the use of multiple values
List = ["Geeks", "For", "Geeks"]

# accessing a element from the
# list using index number
print("Accessing a element from the list")
print(List[0])
print(List[2])

#Accessing elements from a multidimensional LIST
# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Geeks', 'For'], ['Geeks']]

# accessing an element from the
# Multi-Dimensional List using
# index number
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])

List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

# accessing an element using
# negative indexing
print("Accessing element using negative indexing")

# print the last element of list
print(List[-1])

# print the third last element of list
print(List[-3])

# Creating a List
List1 = []
print(len(List1))

# Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2))

# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = []
print("Initial blank List: ")
print(List)

# Addition of Elements
# in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)

# Adding elements to the List
# using Iterator
for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)

# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)

# An integer assignment 
age = 23

# A floating point 
salary = 789.8

# A string 
name = "Cole Palmer"

print(age) 
print(salary) 
print(name) 

a = 10
b = 20
print(a+b) 

a = "Amadile "
b = "Majid"
print(a+b) 

# numberic 
var = 789
print("Numeric data : ", var) 

# Sequence Type 
String1 = 'Welcome to our World'
print("String with the use of Single Quotes: ") 
print(String1) 

# Boolean 
print(type(True)) 
print(type(False)) 

# Creating a Set with 
# the use of a String 
set1 = set("Man From Nowhere") 
print("\nSet with the use of String: ") 
print(set1) 

# Creating a Dictionary 
# with Integer Keys 
Dict = {1: 'Java', 2: 'For', 3: 'Language'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 

# Creating an empty Tuple
Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)

# Creating a Tuple
# with the use of string
Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple1)

# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

# Creating a Tuple
# with the use of built-in function
Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)

# Creating a Tuple
# with Mixed Datatype
Tuple1 = (5, 'Welcome', 7, 'Animals')
print("\nTuple with Mixed Datatypes: ")
print(Tuple1)

# Creating a Tuple
# with nested tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'version')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

# Creating a Tuple
# with repetition
Tuple1 = ('Exactly',) * 3
print("\nTuple with repetition: ")
print(Tuple1)

# Creating a Tuple
# with the use of loop
Tuple1 = ('Wizards')
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    print(Tuple1)

# Accessing Tuple
# with Indexing
Tuple1 = tuple("Geeks")
print("\nFirst element of Tuple: ")
print(Tuple1[0])


# Tuple unpacking
Tuple1 = ("Food", "For", "Thought")

# This line unpack
# values of Tuple1
a, b, c = Tuple1
print("\nValues after unpacking: ")
print(a)
print(b)
print(c)

# Concatenation of tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Something', 'For', 'Good')

Tuple3 = Tuple1 + Tuple2

# Printing first Tuple
print("Tuple 1: ")
print(Tuple1)

# Printing Second Tuple
print("\nTuple2: ")
print(Tuple2)

# Printing Final Tuple
print("\nTuples after Concatenation: ")
print(Tuple3)

# Slicing of a Tuple

# Slicing of a Tuple
# with Numbers
Tuple1 = tuple('AMADILEMAJID')

# Removing First element
print("Removal of First Element: ")
print(Tuple1[1:])

# Reversing the Tuple
print("\nTuple after sequence of Element is reversed: ")
print(Tuple1[::-1])

# Printing elements of a Range
print("\nPrinting elements between Range 4-9: ")
print(Tuple1[4:9])

#python sets
var = {"Aroma", "for", "Guild"}
type(var)

# typecasting list to set
myset = set(["a", "b", "c"])
print(myset)

# Adding element to the set
myset.add("d")
print(myset)

# Python program to demonstrate that
# a set cannot have duplicate values 
# and we cannot change its items

# a set cannot have duplicate values
myset = {"Guy", "for", "Me"}
print(myset)

# values of a set cannot be changed
#myset[1] = "Hello"
print(myset)

Dict = {1: 'Food', 2: 'For', 3: 'Boys'} 
print(Dict)

Dict = {1: 'Good', 2: 'For', 3: 'Bad'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 

Dict = {'Name': 'pythons', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 

Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ") 
print(Dict) 

Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ") 
print(Dict) 

Dict[2] = 'Welcome'
print("\nUpdated key value: ") 
print(Dict) 
Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}} 
print("\nAdding a Nested Key: ") 
print(Dict) 

dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"} 
dict2 = dict1.copy() 
print(dict2) 
dict1.clear() 
print(dict1) 
print(dict2.get(1)) 
print(dict2.items()) 
print(dict2.keys()) 
dict2.pop(4) 
print(dict2) 
dict2.popitem() 
print(dict2) 
dict2.update({3: "Scala"}) 
print(dict2) 
print(dict2.values()) 











