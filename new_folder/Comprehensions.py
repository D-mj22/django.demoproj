'''
n=[2,5,7,10]
new=[5 for i in n]
print(new)

n=[2,5,7,10]
new=[i**2 for i in n]
print(new)

# take only even numbers from given list using LC

n=[1,2,3,4,5,6,7,8,9,10]
new=[i for i in n if i%2==0]
print(new)

# Create a new list with square root of odd numbers from seq n
n=[49,81,64,25,100,16]
from math import sqrt
new=[sqrt(i) for i in n if i%2!=0]
print(new)

# Create a new list with fruit name containing letter 'r' from existing list fruits.
fruits =['pineapple','orange','grapes','apple']
new_fruits=[i for i in fruits if 'r' in i]
print(new_fruits)

# Create a new list with even numbers in the range (200,300)
new=[i for i in range(200,301) if i%2==0]
print(new)

# Create a new list from list l with elements whose value less than 50. l=[45,23,19,95,62,57]
l=[45,23,19,95,62,57]
new=[i for i in l if i<50]
print(new)

# Create a reversed list from existing list
l = [1,2,3,4,5,6]
new = [i for i in range(len(l),0,-1)]                   # or range(len(l)-1,-1,-1)
print(new)

# Remove floating point numbers from the list.
n=[2.45,78,0,5,10.1,150,-12,-9.9]
new =[i for i in n if not isinstance(i,float)]          # or type(i)!=float
print(new)


# Create a list with all the words in a string that are less than 6 letters
s="Python is a programming language"
s_new=s.split()
s1=[i for i in s_new if len(i)<6]
print(s1)

# Count the number of spaces in a string
s="Python is a programming language"
new=[i for i in s if i==" "]
count=len(new)
print(count)

# Create a list with each item reversed from existing list fruits
fruits =['pineapple','orange','grapes','apple']
rev=[i[::-1] for i in fruits]
print(rev)

# Find all numbers from 1-1000 that have 3 in them.
new=[i for i in range(1,1001) if '3' in str(i)]       # We can't use in-operator in numbers
print(new)'''

# SET COMPREHENSION

s=[1,2,3,11,2]
new={i**3 for i in s}
print(new)

# DICTIONARY COMPREHENSION

d=[1,2,3,11,2]
new={i:i+10 for i in d}
print(new)