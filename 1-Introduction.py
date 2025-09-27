#Lesson 1: Introduction
# https://www.youtube.com/watch?v=XKHEtdqhLK8
print('I love learning Python')
print("It's really fun")


#Lesson 2: Variables
# https://www.youtube.com/watch?v=XKHEtdqhLK8
#variable = a container for a value.
# Behaves as the value that it contains
name = "Bro"
print(type(name))
print("Hello " + name)
first_name="Bro"
last_name="Code"
full_name=first_name + last_name
print("Hello "+ full_name)

#when assign value of int type not with quotes
# because cant use strings with math
age = 21
age +=1
#Better way to write above is age +=1
print(age)
print(type(age))
print('Your age is: '+str(age))

#Float
height=250.5
print(height)
print(type(height))

#Boolean. Can only store True or False
human = False
print(human)
print(type(human))


#Lesson 3: Multiple Assignment
# https://www.youtube.com/watch?v=XKHEtdqhLK8
#Multiple assignment = allows us to assign multiple variables
# at the same time in one line of code.

name ='Bro'
age = 32
attractive = True
print(name, age, attractive)

#multiple assignment show it is easier to assign.
name, age, attractive= "Bro", 32, True
print(name, age, attractive)

#also multiple assignment
Bill = Tina = Steve = 30
print(Bill)



#Lesson 4: String Methods
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# create a new .py file is Ctrl + Alt + Insert
name = "Bro"
#print(len(name))

#this looks for index position of B
print(name.find("B"))

print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
#isalpha to check if only alphetical letters
print(name.isalpha())
print(name.count("o"))
print(name.replace("o", 'a'))
print(name*3)


#Lesson 5: Type Cast
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# type casting = convert the data type of a value
# to another data type.

x = 1     #int
y = 2.0   #float
z = '3'   #str

x = str(x)
y = str(y)
z = str(z)

print(x)
print(y)
print(z*3)

x = float(x)
y = float(y)
z = float(z)

print(x)
print(y)
print(z*3)


#Lesson 6: User Input
# https://www.youtube.com/watch?v=XKHEtdqhLK8

name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))

print("Hello "+name)
print("You are "+str(age)+ " years old")
print("You are "+str(height)+ " feet tall")


#Lesson 7: Math Functions
# https://www.youtube.com/watch?v=XKHEtdqhLK8

import math
pi = 3.14
x = 1
y = 2
z = 3

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi, 2)) #raises it to power of 2
print(math.sqrt(pi)) #square root
print(max(pi,x,y,z)) #finds max value
print(min(pi,x,y,z)) #finds min value


#Lesson 8: String Slicing
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# slicing = create a substring by extracing elements from
# another string. indexing[] or slice()
# [start:stop:step]
# start index in inclusive. stop index is exclusive.
# step is how much increasing index. default is 1.

name = "Bro Code"
first_name = name[:3]
last_name = name[4:]
funky_name = name[::3]
reversed_name = name[::-1]
print(first_name)
print(last_name)
print(funky_name)

website1 = 'http://test.com'
website2 = 'http://google.com'
slice = slice(7,-4)
print(website1[slice])
print(website2[slice])


#Lesson 9: If Statements
#a block of code that will execute if it's condition is true
# https://www.youtube.com/watch?v=XKHEtdqhLK8

age = int(input("How old are you?:"))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age <0:
    print("You have not been born yet!")
else:
    print("You are a child!")


#Lesson 10: Logical Operators (and, or, not)
#used to check if two or more conditional statements
# https://www.youtube.com/watch?v=XKHEtdqhLK8
#I cannot get this to work.
#I want to have it be that the user picks where they live to give answer based on cel vs far

location = input("Do you live in the USA? (Yes or No):")
temp = int(input("What is the temperature outside?:"))

if location == "Yes" or "yes" or "yea" or "Yea":
    location1 = location
else: location2 = location


if location1 == location:
    if temp >= 35 and temp <= 90:
        print("The temperature is good today!")
        print("Go outside!")
    elif temp < 35 or temp > 90:
        print("The temperature is bad today!")
        print("Stay inside!")

elif location2 == location:
    if temp >= 0 and temp <= 30:
        print("The temperature is good today!")
        print("Go outside!")
    elif temp < 0 or temp > 30:
        print("The temperature is bad today!")
        print("Stay inside!")


# not operator: flips it from true to false or reverse
    if not(temp >= 0 and temp <= 30):
        print("The temperature is bad today!")
        print("Stay inside!")
    elif not(temp < 0 or temp > 30):
        print("The temperature is good today!")
        print("Go outside!")


#Lesson 11: While loops = a statement that will execute
#its block of code, as long as its condition remains true.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

#will try to create a loop for user to enter name.
# need an escape to the while loop

#To start a code execution below, Ctrl + F5
#To stop a code execution below, Ctrl + F2

name = ""
while len(name) == 0:
    name = input("Enter your name: ")
print("Hello "+name)

#another way to write this:
name = None
while not name:
    name = input("Enter your name: ")
print("Hello "+name)


#Lesson 12: For Loops
# a statement that will execute its block of code a limited
# amount of times.
# https://www.youtube.com/watch?v=XKHEtdqhLK8
import time

#i means index.
# The +1 will make the count 1 to 10 because starts at 0.
# Can also add the +1 to the range
#for i in range(10):
    #print(i+1)

#this program counts by 2
#for i in range(50,100+1,2):
    #print(i)

#for i in "Bro Code":
    #print(i)

#import time module at top of code.
# i can be anything. below it is seconds.
# the -1 it the step amount. so here it is counting down.
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")


#Lesson 13: Nested Loops
# the "inner loop" will finish all its interations before
# finishing on iteration of the "outer loop"
# https://www.youtube.com/watch?v=XKHEtdqhLK8

#going to draw a rectange with nested loops.
#Outer loop will be in charge of rows. Inner incharge of columns.
rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")
#common convetion for innter for loops is j.
#end="" prevents cursor from moving to next line.
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()


#Lesson 14: Loop Control Statements
# Change a loop execution from its normal sequence
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# break = used to terminate the loop entirely
# continue = skips to the next ieration of the loop
# pass = dows nothing, acts as a placeholder

#while True:
    #name = input("Enter your name: ")
    #if name !="":
        #break

phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1,21):
    if i == 13:
        pass
    else: print(i)


#Lesson 15: Lists
# used to store multiple items in a single variable.
# element is a part of the list.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

food = ["pizza", "hamburger", "hotdog"]
food.append("ice cream")
food.remove("hotdog")
food.pop() #removes last element in list
food.insert(0,"cake")
food.sort()
food.clear()

#print(food[0])
for x in food:
    print(x)


#Lesson 16: 2D Lists
# a lists of lists
# https://www.youtube.com/watch?v=XKHEtdqhLK8

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
desert = ["cake", "ice cream"]

food = [drinks, dinner, desert]
print(food[0][1])
print(food[1][1])


#Lesson 17: Tuple
# a collection which is ordered and unchangeable. used to group together realted data
# https://www.youtube.com/watch?v=XKHEtdqhLK8

student = ("Bro", 21, "male")
print(student.count("Bro"))
print(student.index("male"))

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here!")


#Lesson 18: Sets
# collection which is undordered, unindexed. no duplicate values.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
dishes.update(utensils)
dinner_table = utensils.union(dishes)

print(dishes.difference(utensils))
print(utensils.intersection(dishes))

for x in dinner_table:
    print(x)


#Lesson 19: Dictionaries
# A changeable, unordered collection of unique key:value pairs.
# Fast because they use hashing, allow us to access a value quickly.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}
print(capitals['Russia']) #this causes issues if not in dictionary. Get method better.
print(capitals.get('Germany')) # this will return None if not there.
print(capitals.keys()) # will print only the keys
print(capitals.values()) # will print only the values
print(capitals.items()) # will print all items

for key, value in capitals.items(): # this will also print whole dictionary.
    print(key, value)

capitals.update({'Germany': 'Berlin'}) # way to add to dictionary.
capitals.update({'USA': 'Las Vegas'}) # way to update or add to dictionary.
capitals.pop('China') # removes key, value from dictionary.
capitals.clear()


#Lesson 20: Index operator []
# gives access to a sequence's element (str, list, tuples)
# https://www.youtube.com/watch?v=XKHEtdqhLK8

name = "bro Code!"
if(name[0].islower()):
    name = name.capitalize()
print(name)

first_name = name[:3].upper()
last_name = name[4:].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)


