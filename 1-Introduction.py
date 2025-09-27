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


#Lesson 21: Function
# a block of code which is executed only when it is called.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

# what is given (Bro) is argument (information sending to function).
# These match to parameters (first_name).
def hello(first_name, last_name, age):
    print("Hello "+first_name+" "+last_name)
    print("You are "+ str(age) + " years old") # need to convert int to str.
    print("Have a nice day!")

hello("Bro", "Code", 33)


#Lesson 22: Return statements
# functions send Python values/objects back to the caller.
# these values/objects are known as the function's return value
# https://www.youtube.com/watch?v=XKHEtdqhLK8

def multiply(number1, number2):
    return number1 * number2

x = multiply(6,8)
print(x)


#Lesson 23: Keyword Arguments
# Arguments preceded by an identifier when we pass them to a function
# The order of the arguments does not matte,r unlike positional arguments
# Python knows the names of the arguments that our function receives
# https://www.youtube.com/watch?v=XKHEtdqhLK8

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello("Code", "Dude", "Bro") #these are positional arguments.
hello(last="Code", middle="Dude", first="Bro") #these are keyword arguments.


#Lesson 24: Nested Function Calls
# function calls inside other function calls
# innermost function calls are resolved first
# return value is used as arugment for the next outer function.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

num = input("Enter a whole positive number: ")
print(num)
num = float(num)
print(num)
num = abs(num)
print(num)
num = round(num)
print(num)
# this is a nested function call below. it combines all above functions.
print(round(abs(float(input("Enter a whole positive number: ")))))


#Lesson 25: Variable Scope
# The region that a variable is recognized
# A variable is only available from inside the region it is created.
# A global and locally scoped version of a variable can be created.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

name = "Bro" # global scope because global variable (available inside & outside functions)

def display_name():
    name = "Code" # local scope because local variable (available only inside this function)
    print(name)
# Will first use local variable first then Global full rule below for Python
# LEGB Rule. Local. Then Enclosing. Then Global. Then Built-in.
display_name()
print(name)


#Lesson 26: *args
# parameter that will pack all arguments into a tuple (ordered, unchangable).
# useful so that a function can accept a varying amount of arguments.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

def add(*stuff):
    sum = 0
    #stuff = list(stuff) # if want to change an item in tuple, turn into list.
    #stuff[0] = 0    # this turns the 1st item to 0.
    for i in stuff:
        sum += i
    return sum
print(add(1,2,3,4,5,6,7,8))


#Lesson 27: **kwargs
# parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword arguments
# https://www.youtube.com/watch?v=XKHEtdqhLK8

def hello(**kwargs):  #just need the two **. Dont need to name it kwargs.
    print("Hello "+ kwargs['first']+" "+kwargs['last'])
    print("Hello",end=" ")
    for key, value in kwargs.items():
        print(value, end= " ")  #end=" " replaces the new line character (default) with space.

hello(title="Mr.", first="Bro", middle="Dude", last="Code")


#Lesson 28: String Format
# str.format() = optional method that gives users more control when displaying outputs
# https://www.youtube.com/watch?v=XKHEtdqhLK8

animal = "cow"
item = "moon"
#print("The "+animal+" jumped over the "+item)  better way to write this is below.
print("The {} jumped over the {}".format(animal, item))
print("The {0} jumped over the {1}".format(animal, item))  #positional argument
print("The {food} jumped over the {house}".format(house="tall", food="pizza"))  #keyword argument

#another way to format:
text = "The {} jumped over the {}"
print(text.format(animal, item))

name = "Bro"
print("Hello, my name is {}".format(name)) #can add some padding.
print("Hello, my name is {:10}".format(name))  #adding ten spacing worth of padding after name.
print("Hello, my name is {:^10}".format(name)) #added center align. Can do right > or left <

number = 1000
print("The number pi is {:.3f}".format(number))  #adds 3 deciminal places.
print("The number is {:,}".format(number)) #adds commas
print("The number is {:b}".format(number)) #displays it in binary
print("The number is {:o}".format(number)) #displays it in octodecimal
print("The number is {:X}".format(number)) #displays it in hexidicimal.
print("The number is {:E}".format(number))


#Lesson 29: Random Numbers
# creating psuedo random numbers.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

import random
x = random.randint(1,6) #random integir  between 1 and 6.
y = random.random()     #random floating point number.

my_list = ['rock', 'paper', 'scissors']
z = random.choice(my_list)

cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']
random.shuffle(cards)
print(cards)


#Lesson 30: Exception Handling
# Exceptions are events detected during execution that interrupt the flow of a program.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    results = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You cannot divide by zero! Idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers please.")
except Exception as e:  #good pratice to put specific exceptions first.
    print(e)
    print("Something went wrong: ")
else:
    print(results)
finally:  #should be at end as want to close files when done
    print("This will always execute")


#Lesson 31: File Detection
# https://www.youtube.com/watch?v=XKHEtdqhLK8

import os
path = "C:\\Users\\WilliamBillCorkery\\OneDrive - Iberia Advisory\\Desktop\\folder"
# need to manually put in double back slashes
if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location does not exist")


#Lesson 32: Read a File
# this will read a file. need to created a plain text file called test.txt in project folder
# https://www.youtube.com/watch?v=XKHEtdqhLK8

try:
    with open('test.txt') as file:  #will need file path and double-slashes if not here.
        print(file.read())  #'with' will also close file after reading them.
except FileNotFoundError:
    print("That file was not found")


#Lesson 33: Write a File
#
# https://www.youtube.com/watch?v=XKHEtdqhLK8

text = "Hello \nThis is some text \nHave a good date!\n"# \n is a new line.
with open('test.txt', 'w') as file: #by default the mode is r. but here it is set to w for write.
    #mode 'a' will append the new lines to the file.
    file.write(text)


#Lesson 34: Copy a File
# https://www.youtube.com/watch?v=XKHEtdqhLK8

# copyfile() = copies contents of a file
# copy()     = copyfile(0 + persmission mode + destination can be a directory
# copy2()    = copy() + copies metadata (file's creation and modification times)

import shutil  #good module to copy files.
shutil.copyfile('test.txt', 'copy.txt') #this function has both a source (src) and a destination (dst)
# if file is not in project folder, would need to list the file path.


#Lesson 35: Move a file
# move a file from projects folder to desktops folder.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

import os
source = "test.txt"
destination = "C:\\Users\\WilliamBillCorkery\\OneDrive - Iberia Advisory\\Desktop\\text.txt"

try: #recommend doing code in try/except block to handle issues.
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")


#Lesson 36: Delete a File
# https://www.youtube.com/watch?v=XKHEtdqhLK8

import os
import shutil
path = 'test.txt'

try:
    os.remove(path)     # delete a file
    #os.rmdir(path)      # delete a file or empty folder
    #shutil.rmtree(path) # delete files and/or folders
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("That folder contains files")
else:
    print(path+" was deleted")


#Lesson 37: Modules
# a file containing python code. may contain functions, classes, etc.
# Used with modular programming, which is to separate a program into parts.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

# so this is a module (37-Modules). So lets say there is another module called messages and has two functions.
# the first is hello() and the second is bye().
#import messages as msg  # this imports the messages module as msg (makes it easier).
#msg.hello()       # this would call the hello() function from the messages module.

# another way to import is below.
# it is longer at first but no longer need message or msg before function.
#from messages import hello,bye  # cann also say import * which imports all. dont do this as huge.
#hello()
#bye()

# prepackaged modules below.
# can also go to python module index on python.org.
help("modules")


#Lesson 38: Rock, Paper, Scissors
# https://www.youtube.com/watch?v=XKHEtdqhLK8

import  random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None  # need to initalize player here.
    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

        if player == computer:
            print("computer: ", computer)
            print("player: ", player)
            print("Tie!")
        elif player == "rock":
            if computer == "paper":
                print("computer: ", computer)
                print("player: ", player)
                print("You lose!")
            if computer == "scissors":
                print("computer: ", computer)
                print("player: ", player)
                print("You win!")
        elif player == "scissors":
            if computer == "rock":
                print("computer: ", computer)
                print("player: ", player)
                print("You lose!")
            if computer == "paper":
                print("computer: ", computer)
                print("player: ", player)
                print("You win!")
        elif player == "paper":
            if computer == "scissors":
                print("computer: ", computer)
                print("player: ", player)
                print("You lose!")
            if computer == "rock":
                print("computer: ", computer)
                print("player: ", player)
                print("You win!")
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Bye!")


#Lesson 39: Quiz Game
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# first create the shell of four functions that need.

def new_game():
     guesses = []
     correct_guesses = 0
     question_num = 1
     for key in questions:
         print("--------------------------")
         print(key)
         for i in options[question_num-1]:
             print(i)
         guess = input("Enter (A, B, C, or D): ")
         guess = guess.upper()
         guesses.append(guess)
         correct_guesses += check_answer(questions.get(key), guess)
         question_num += 1
     display_score(correct_guesses, guesses)
# ------------------------------------
def check_answer(answer,guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

# ------------------------------------
def display_score(correct_guesses, guesses):
    print("--------------------------")
    print("RESULTS")
    print("--------------------------")
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")
# ------------------------------------
def play_again():
    response = input("Do you want to play again? (Yes or no):")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False

questions = {"Who created Python?: " : "A",
             "What year was Python created?: ": "B",
             "Python is atributed to which comedy group?: ": "C",
             "Is the Earth round?: ": "A"}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. Sometimes", "D. What is the Earth?"]]

new_game()
while play_again():
    new_game()

print("Goodbye!")


#Lesson 40: Object Oriented Programming (OOP)
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# object is an instance of a class. Combination of attributes (what object is/has, e.g. tall) and
# methods (what object can do, e.g. sleep).

#if program is large, pull class in a seperate module.
# Dont need to pass in self into class.

from car import Car
car_1 = Car("Chevy", "Corvette", 2021, 'blue')
# print(car_1.make)
car_2 = Car("Ford", "Mustang", 2022, 'red')

car_1.drive()
car_2.stop()


