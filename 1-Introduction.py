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


#Lesson 41: Class Variables
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# class variable is declared inside class and is default normally.
# instance variable is declared inside a constructor. Has unique value.

from car import Car
car_1 = Car("Chevy", "Corvette", 2021, 'blue')
car_2 = Car("Ford", "Mustang", 2022, 'red')

#Car.wheels = 2  #this changes all default wheels number


#Lesson 42: Inheritance
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# classes can inherit attributes and methods from something else (usally another class).
# so if Animal (parent class) is a class with move() and eat().
# then have Dog (subclass/child class) has move(), bark(), and eat().
# move() is overriden. eat(0 is inheritied. Bark() is new.

#will keep all classes in same file for ease.
#the reason want things in parent class if need to make changes,
#only need to do it in one place.

class Animal:
    alive = True
    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):  #Rabbit is child class of Animal parent class
    def run(self):
        print("This rabbit is running")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.run()
fish.swim()
hawk.fly()

#print((rabbit.alive))
#fish.eat()
#hawk.sleep()


#Lesson 43: Multilevel Inheritance
# https://www.youtube.com/watch?v=XKHEtdqhLK8
#Multi-level inerhtiance = when a derived (child) class inherits from
#another derived (child) class

class Organism:
    alive = True
class Animal(Organism):
    def eat(self):
        print("This Animal is eating")
class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()


#Lesson 44: Multiple  Inheritance
# https://www.youtube.com/watch?v=XKHEtdqhLK8
#Multiple Inheritance = when a child class is derived from more than one parent class

#this is used when want to create a class that needs different attributes/methods from multiple classes.
#so below some animals are both prey and predator (e.g. fish)
class Prey:
    def flee(self):
        print("This animal flees")
class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

#as can be seen below, only fish has flee and hunt.
#rabbit.flee()
#hawk.hunt()
#fish.hunt()
#fish.flee()


#Lesson 45: Method Overriding
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# method overridding is when a subclass (or child class)
# can override a method of its parent class.

#animal is parent class and rabbit is child class.
class Animal:
    def eat(self):
        print("This animal is eating")
class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()


#Lesson 46: Method Chaining
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# Method chaining = calling multiple methods sequentially
# each call performs an action on the same object and returns self

class Car:
    def turn_on(self):
        print("You start the engine")
        return self
    def drive(self):
        print("You drive the car")
        return self
    def brake(self):
        print("You step on the brakes")
        return self
    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()
#car.turn_on()
#car.drive()
car.turn_on().drive()
car.brake()\    #this backslash is introduced by program to make it more readable.
    .turn_off()


#Lesson 47: Super Function
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# super() = Function used to give access to the methods of a parent class.
# Returns a temporary object of a parent class when used.

#so with below, any similarities between square and cube,
# can move to rectangle. This will decrease repeat code.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        return self.length*self.width
class Cube(Rectangle):
    def __init__(self,length, width, height):
        super().__init__(length, width)
        self.height = height
    def volumne(self):
        return self.length*self.width*self.height

square = Square(3,3)
cube = Cube(3,3,3)
print(square.area())
print(cube.volumne())


#Lesson 48: Abstract Classes
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# Prevents a user from creating an object of that class +
# compels a user to override abstract methods in a child class.
# basically a form of checks and balances

#abstract class = a class which contains one or more abstract methods.
#abstract method = a method that has a declaration but doe not have an implementation.

from abc import ABC, abstractmethod
class Vehicle(ABC):  #this is class.
    @abstractmethod   #this is a decorator.
    def go(self):  #this is the method.
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("This motorcycle is stopped")

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#if try to run this, get typeerror because abstract class.
#vehicle.go()
car.go()
car.stop()
motorcycle.go()
motorcycle.stop()


#Lesson 49: Objects as Arguments
# https://www.youtube.com/watch?v=XKHEtdqhLK8

class Car:
    color = None
class Motorcylce:
    color = None

# make sure this is not within class because then would be a method of car class.
def change_color(vehicle, color): #argument names should be lower case.
    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()
bike_1 = Motorcylce()

change_color(car_1, "red")
change_color(car_2, "white")
change_color(car_3, "blue")
change_color(bike_1, "yellow")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)


#Lesson 50: Duck Typing
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# concept where the class of an objet is less important than the methods/attributes
# class type is not checked if minimum methods/attributes are present.
# "If it walks like a duck, and it quacks like a duck, then it must be a duck."

class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("this duck is quacking")
class Chicken:
    def walk(self):
        print("This chicken is walking")
    def talk(self):
        print("this chieckn is clucking")
class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck = Duck()
chicken= Chicken()
person = Person()

#person.catch(duck)
person.catch(chicken)


#Lesson 51: Walrus Operator :=
# https://www.youtube.com/watch?v=XKHEtdqhLK8

# new to Python 3.8
# assignment expression aka walrus operator
# assigned values to variables as part of a lager expression

happy = True
print(happy)
print(happy := True) #in this walrus operator, happy is assigned to True and printed in same line

#example without walrus
foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)
#example with walrus
foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)


#Lesson 52: Functions to Variables
# https://www.youtube.com/watch?v=XKHEtdqhLK8

#This defines the function
def hello():
    print("Hello")

#this calls the function.
hello()

#this will pring the location of the function in memory. It changes.
print(hello)
#these will be the same location as it is basically a function with two alias or names (hi and hello)
hi = hello
print(hi)

say = print  #this is assigning print function to a variable.
say("What! I cannot believe this works!")


#Lesson 53: Higher Order Function
# https://www.youtube.com/watch?v=XKHEtdqhLK8

# Higher Order Functions = a function that either:
# 1. accepts a function as an argument or
# 2. returns a function (In Python, functions are also treated as objects)

# example of a function as argument. loud and quiet go into hello as function arguments.
def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()
def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)

# example of a returning a function
def divisor(x):
    def dividend(y):
        return y/x
    return dividend
divide = divisor(2)
print(divide(10))


#Lesson 54: Lambda
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# lambda = function written in 1 line using lambda keyword.
# Accepts any number of arguments (parameters), but only has one epxression.
# (think of it as a shortcut)
# (useful if needed for a short period of time, throw-away)

# lambda parameters:expression

def double(x):
    return x * 2
print(double(5))
# this is the same as above lines of code.
double = lambda x:x*2
multiply = lambda x,y:x*y
add = lambda x,y,z: x+y+z
full_name = lambda first_name, last_name: first_name+" "+last_name
age_check = lambda age: True if age >= 18 else False

print(double(5))
print(multiply(5,6))
print(add(5,6,7))
print(full_name("Bro", "Code"))
print(age_check(18))


#Lesson 55: Sort
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# sort() method = used with lists
# sort() function = used with iterables

#this is sorting simple lists, tuples, etc.
students_0 = ("Squidward", "Sandy","Patrick","Spongebob","Mr. Krabs")
sorted_students_0 = sorted(students_0)
for i in sorted_students_0:
    print(i)

#this is for sorting complex things like list of tuples below.
students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78)]

students.sort() # can have students.sort(key=age) which will just sort by students age
for i in students:
    print(i)

age = lambda ages:ages[2]
students.sort(key=age) # can have students.sort(key=age) which will just sort by students age
for i in students:
    print(i)

#sort doesnt work well with tuples. so can use sorted() function with tuples.
grade = lambda grades:grades[1]
sorted_stuents = sorted(students, key=grade, reverse=True) # this reverses it
for i in sorted_stuents:
    print(i)


#Lesson 56: Map
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# map() = applies a function to each itme in an iterable (list, tuple, etc.)
# map(function, iterable) so it accepts two arguments

#list of tuples
store = [("shirt", 20.00),
          ("pants", 25.00),
          ("jacket", 50.00),
          ("socks", 10.00)]

# one USD is 0.82 euros
to_euros = lambda  data:(data[0], data[1]*0.82)
to_dollars = lambda  data:(data[0], data[1]/0.82)

#store_euros = list(map(to_euros, store))
#for i in store_euros:
#    print(i)

store_dolalrs = list(map(to_dollars, store))
for i in store_dolalrs:
    print(i)


#Lesson 57: Filter
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# filter() = creates a collection of elements from an iterable for which a function returns True
# filter(function, iterable) so it accepts two arguments

friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phobe", 17),
           ("Joey", 16),
           ("Chandler", 21),
           ("Ross", 20)]

age = lambda data:data[1] >= 18
drinking_buddies = list(filter(age, friends))  # the list() is casting it back into a new list, drinking_buddies
for i in drinking_buddies:
    print(i)


#Lesson 58: Reduce
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# reduce()= apply a function to a iterable and reduce it to a single cumulative value.
# performs function on first tow elements and repeats process until 1 value remains.

# reduce(function, iterable)

import functools

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x,y,:x+y, letters)
print(word)

factorial = [5,4,3,2,1]
results = functools.reduce(lambda x,y,:x*y, factorial)
print(results)


#Lesson 59: List Comprehensions
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# list comprehension = a way to create a new list with less syntax
# can mimic certain lambda functions, easier to read
# list = [expression for item in iterable if conditional] <-- if one if condition
# list = [expression (if/else) for item in iterable]      <-- if have if/else condition

squares = []                # create an empty list
for i in range(1,11):       # create a for loop
    squares.append(i*i)     # define what each loop iteration should do
print(squares)

squares1 = [i*i for i in range(1,11)]
print(squares1)

#using lambda
students = [100,90,80,70,60,50]
passed_students = list(filter(lambda x:x>=60, students))
print(passed_students)

#using list comprehension
passed_students1 = [i for i in students if i>=60]
passed_students2 = [i if i>=60 else "Failed" for i in students]
print(passed_students1)
print(passed_students2)


#Lesson 60: Dictionary Comprehension
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# Dictionary Comprehension = create dictionaries using an expression
# can replace for loops and certain lambda functions

# 1: dictionary = {key: expression for (key,value) in iterable}
# 2: dictionary = {key: expression for (key,value) in iterable if conditional}
# 3: dictionary = {key:(if/else) for (key,value) in iterable}
# 4: dictionary = {key: function(value) for (key,value) in iterable}

# Dictionary version 1
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles':100, 'Chicago':50}
cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C )

# Dictionary version 2
weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles':"sunny", 'Chicago':"cloudy"}
sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
print(sunny_weather)

# Dictionary version 3
cities = {'New York': 32, 'Boston': 75, 'Los Angeles':100, 'Chicago':50}
desc_cities3 = {key:("Warm" if value >=40 else "Cold") for (key,value) in cities.items()}
print(desc_cities3)

# Dictionary version 4
def check_temp(value):
    if value>= 70:
        return "Hot"
    elif 69>=value >=40:
        return "Warm"
    else:
        return "Cold"
cities = {'New York': 32, 'Boston': 75, 'Los Angeles':100, 'Chicago':50}
desc_cities4  = {key:check_temp(value) for (key,value) in cities.items()}
print(desc_cities4)


#Lesson 61: Zip Function
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

username = ["Dude", "Bro", "Mister"]
passwords = ("passwprd", "abc123", "guest")
users = dict(zip(username, passwords))
# users = list(zip(username, passwords)) can also make this into a list zip.
print(type(users))

for i in users:
    print(i)

for key, value in users.items():
    print(key+" : "+value)


#Lesson 62:  if _name_ == '__main__'
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# Python interpreter sets "special variables", one of which is __name__
# Python will assign the __name__ variable a value of '__main__' if it is
# the initial module being run.

def main():
    print("Hello")

if __name__ == '__main__':
    main()


#Lesson 63:Time Module
# https://www.youtube.com/watch?v=XKHEtdqhLK8
import time

print(time.ctime(0))    # convert a time expressed in seconds epoch to a readable string
                        # epoch = when your computer thinks time began (reference point)
print(time.time())  # return current seconds since epoch
print(time.ctime(time.time())) # will get current time.
time_object = time.localtime()
time_object = time.gmtime() # this is UTC time.
print(time_object)
local_time = time.strftime("%B %d %Y %H: %M:%S", time_object) # go to python offical documentation
print(local_time)

time_string = "20 April, 2020"
time_object = time.strptime(time_string, "%d %B, %Y") # this parse a string a return time object.
print(time_object)

# asctime will accept tuple format.
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple) # accepts a tuple representation of time.
print(time_string)

# mktime will take time and convert it to seconds since epoch.
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple) # accepts a tuple representation of time.
print(time_string)


#Lesson 64:Threading
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# thread = a flow of execution, like a separate order of instructions.
#               However each thread takes a turn running to achieve concurrency
#               GIL = Global interpreter lock, allows only one thread to hold
#               control of the python interpreter at any one time

# CPU bound = program/task spends mos of its time waiting for internal events
#               (CPU intensive). Use multiprocessing.

# io bound = program/task spends most of its time waiting for external events
#               (user input, web scraping). use multithreading.

import threading
import time

# in the example below, lots of time will be IO bound as waiting for sleep
# so running on main thread see it takes 12 seconds.
def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drink coffee")

def study():
    time.sleep(5)
    print("You finish studying")

#eat_breakfast()
#drink_coffee()
#study()
# these tasks were complete sequentailly.
#  but realistically we as humans these tasks can be completed together.
# so basically multithreading.

x = threading.Thread(target=eat_breakfast, args=())
x.start()
y = threading.Thread(target=drink_coffee, args=())
y.start()
z = threading.Thread(target=study, args=())
z.start()
# this program only took 5 seconds as there were 4 threads running.
# these threads were run concurrently.
# active count and enumerate were called first as main thread called these first

# if want our main thread to wait for 3 instructive threads, use join below.
x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())  # trick to return how long calling thread/main
# thread to finish instructions. main thread is in charge of creating 3 additonal threads.


#Lesson 65:Daemon Thread
# https://www.youtube.com/watch?v=XKHEtdqhLK8

# daemon thread = a thread that runs in the background, not important for program to run
#               your program will not wait for daemon threads to complete before exiting
#               non-daemon threads cannot normally be killed, stay alive until task is complete
#
#               Daemon thread examples: background tasks, garbage collection, waiting for input, long running processes

import threading
import time
def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: ", count, "seconds")

# if dont change it to daemon thread, will continue
# x = threading.Thread(target=timer)
x = threading.Thread(target=timer, daemon=True)
x.start()

answer = input("Do you wish to exit?")

# this is a way to set daemon thread to true or false
# x.setDaemon(True)
# this returns true of false
# print(x.isDaemon())


#Lesson 66: Multiprocessing
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# multiprocessing = running tasks in parallel on different cpu cores, bypassing GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy CPU usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
# this way below with only is if dont have multiprocessing
#    a = Process(target= counter, args=(1000,))
#    a.start
#    a.join
    print(cpu_count())
    a = Process(target=counter, args=(500,))
    b = Process(target=counter, args=(500,))
    a.start()
    b.start()
    a.join()
    b.join()
    print("Finished in:", time.perf_counter(), "Seconds")

# for some reason, my results are seconds since something? I got 103233 while it should be ~15 seconds.
if __name__ == '__main__':
    main()


#Lesson 67: GUI Windows
# https://www.youtube.com/watch?v=XKHEtdqhLK8

from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Bro Code first GUI program")

icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.config(background="black")
#window.config(background="#5cfcff") #this is a hexadecimal color value.

window.mainloop() #place window on computer screen, listen for events


#Lesson 68: Labels
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# labels = an area widget that holds text and/or an image within a window

from tkinter import *

window = Tk()

photo =PhotoImage(file='person.png')

#simple way to have a label.
#label = Label(window, text='Hello World')
#label.place(x=0,y=0) # this will place the label in a certain position

label = Label(window,
              text = 'Bro, do you even code?',
              font = ('Arial', 40, 'bold'),
              fg = '#00FF00',
              bg = 'black',
              relief = RAISED,
              bd = 10,
              padx = 20,
              pady=20,
              image = photo,
              compound="bottom")
label.pack()

window.mainloop()


#Lesson 69: Buttons
# https://www.youtube.com/watch?v=xiUTqnI6xk8
# button = you click it, then it does stuff

from tkinter import *
window = Tk()

count = 0
def click():
    global count
    count+=1
    print(count)

photo = PhotoImage(file='like.png')

button = Button(window,
                text="click me!",
                command = click,
                font = ("Comic Sans", 30),
                fg = "#00FF00",
                bg = "black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound='bottom')
button.pack()
window.mainloop()


#Lesson 70: Entrybox
# https://www.youtube.com/watch?v=xiUTqnI6xk8

#entry widet = textbox that accepts a single line of user input
from tkinter import *

def submit():
    username = entry.get()
    print("Hello "+username)
    entry.config(state=DISABLED)  # this makes it so unable to make changes once click submit.

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

window = Tk()

entry = Entry(window, font=("Arial", 50),
              fg="#00FF00",
              bg="black",
              show="*")   #this is a good way to hide what user is writing, good with passwords. 
entry.insert(0,'Default Text')
entry.pack(side =LEFT)

submit_button = Button(window,text="submit", command=submit)
submit_button.pack(side = RIGHT)

delete_button = Button(window,text="delete", command=delete)
delete_button.pack(side = RIGHT)

backspace_button = Button(window,text="backspace", command=backspace)
backspace_button.pack(side = RIGHT)

window.mainloop()


#Lesson 71: Checkbox
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *

def display():
    if(x.get()==1):
        print("You agree!")
    else:
        print("You do not agree")

window = Tk()
x = IntVar()  #returns 1 or 0
python_photo = PhotoImage(file= 'Python Image.png')

check_button= Checkbutton(window,
                          text='I agree to something',
                          variable=x,
                          onvalue=1,
                          offvalue=0,
                          command = display,
                          font=('Arial', 20),
                          foreground='#00FF00',
                          background="black",
                          activeforeground='#00FF00',
                          activebackground = "black",
                          padx=25,
                          pady=10,
                          image=python_photo,
                          compound='left')

check_button.pack()
window.mainloop()


#Lesson 72: Radio Buttons
# https://www.youtube.com/watch?v=xiUTqnI6xk8
# radio button = similar to checkbox, but you can only select one from a group
#I believe the pictures are too large so this isnt working.

from tkinter import *

food = ['pizza', 'hamburger', 'hotdog']

def order():
    if(x.get()==0):
        print('You ordered pizza!')
    elif(x.get()==1):
        print('You ordered a hotdog')
    elif(x.get()==2):
        print('You ordered a hamburger')
    else:
        print('huh?')

window = Tk()
Image_Pizza = PhotoImage(file='pizza.png')
Image_Hotdog = PhotoImage(file='Hotdog.png')
Image_Hamburger = PhotoImage(file='Hambuger.png')
Food_Images = [Image_Pizza, Image_Hamburger, Image_Hotdog]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], #adds text to radio buttons
                              variable=x, #groups radiobuttons together if they share
                              value=index, #assigns each radiobutton a different value.
                              padx=25, #adds padding on x-axis
                              font=("Impact",50),
                              image=Food_Images[index], # this adds image to radio button
                              compound='left',   #adds image & text left side
                              indicatoron=0, #eliminate circle indicators
                              width=375,
                              command=order # this will set command of radio button to function.
                              )
    radiobutton.pack(anchor=W)

window.mainloop()


#Lesson 73: Scale
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+ " degrees C")

window = Tk()
#below adds image to the scale.
#hotImage = PhotoImage(file = 'hot.png')
#hotLabel = Label(image=hotImage)
#hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font = ('Consolas',20),
              tickinterval = 10, #this adds numeric indicators for value
              showvalue = 0,   #hides current value
              troughcolor = 'blue',
              fg = '#FF1C00',
              bg = 'black')
#scale.set(100)   # this sets default slider. below sets it to the middle.
scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

button = Button(window,text='submit', command=submit)
button.pack()

window.mainloop()


#Lesson 74: Listbox
# https://www.youtube.com/watch?v=xiUTqnI6xk8
#listbox = a listing of slectable text items within its own container

from tkinter import *

window = Tk()
def submit():
    food=[]
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("You have ordered: ")
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),EntryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
#    listbox.delete(listbox.curselection())  way to delete only one.
    listbox.config(height=listbox.size())

listbox=Listbox(window,
                bg='#f7ffde',
                font=("Constantia", 35),
                width=12,
                height=10,
                selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,'pizza')
listbox.insert(2,'pasta')
listbox.insert(3,'garlic bread')
listbox.insert(4,'soup')
listbox.insert(5,'salad')
listbox.config(height=listbox.size())

EntryBox = Entry(window)
EntryBox.pack()

SubmitButton = Button(window,text='submit', command=submit)
SubmitButton.pack()

AddButton = Button(window,text='add', command=add)
AddButton.pack()

DeleteButton = Button(window,text='delete', command=delete)
DeleteButton.pack()


window.mainloop()


#Lesson 75: Messagebox
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *
from tkinter import messagebox #import messagebox library

def click():
#    messagebox.showinfo(title='This is an info message box', message='You are a person') # displays a simple message.
#    messagebox.showwarning(title='WARNING!', message='You have a VIRUS!!!') # displays a warning message.
#    messagebox.showerror(title='ERROR!', message='Something went wrong')

#the if-else statement below is useful to ask for a decision from user
#    if messagebox.askokcancel(title='ask ok cancel', message='Do you want to do the thing?'):
#        print('You did a thing!')
#    else:
#        print('You canceled a thing!')

#    if messagebox.askretrycancel(title='ask ok cancel', message='Do you want to retry the thing?'):
#        print('You retried a thing!')
#    else:
#        print('You canceled a thing!')

#    if messagebox.askyesno(title='ask yes or no', message='Do you like cake?'):
#        print('I like cake too')
#    else:
#        print('Why do you not like cake?')

#    answer = messagebox.askquestion(title='ask question', message='Do you like pie?')
#    if (answer == 'yes'):
#        print('I like pie too')
#    else:
#        print('Why do you not like pie?')

# for icon can also use info and error
    answer = messagebox.askyesnocancel(title='Yes no cancel', message='Do you like to code?',icon='warning')
    if(answer == True):
        print('You like to code!')
    elif(answer == False):
        print('Then why are you watching a video on coding?')
    else:
        print('You have dodged the question.')

window = Tk()

button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()


#Lesson 76: Color chooser
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *
from tkinter import colorchooser  #submodule. not necessary.

def click():
#    window.config(bg=colorchooser.askcolor()[1])  #one line of code version of below.
    color = colorchooser.askcolor() #assign color to a variable
    color_Hex = color[1]            #assigns element at index 1 to a varaible
    window.config(bg=color_Hex)     #change background color

window = Tk()
window.geometry('420x420')
button = Button(text='click me', command=click)
button.pack()
window.mainloop()


#Lesson 77: Text Area
# https://www.youtube.com/watch?v=xiUTqnI6xk8
# text widget = functions like a text area, you can enter multiple lines of text

from tkinter import *

def submit():
    input = text.get("1.0", END)
    print(input)

window = Tk()
text = Text(window,
            bg="light yellow",
            font=("Ink Free",16),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="blue")
text.pack()
button = Button(window,text="submit", command=submit)
button.pack()
window.mainloop()


#Lesson 78: Open a file
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *
from tkinter import filedialog

def open_File():
    filepath = filedialog.askopenfilename(initialdir='C://Users//WilliamBillCorkery//PycharmProjects//BroCode-PythonFullCourse',
                                          title="Open File Please",
                                          filetypes=(('text files','*.txt'),
                                          ('all files', '*.*')))
    file = open(filepath,'r')
    print(file.read())
    print(filepath)
    file.close()

window = Tk()
button = Button(text="Open", command=open_File())
button.pack()
window.mainloop()


#Lesson 79:Save a File
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile(initialdir='C://Users//WilliamBillCorkery//PycharmProjects//BroCode-PythonFullCourse',
                                    defaultextension='.txt',
                                    filetypes=[('Text File', '.txt'),
                                               ('HTML file', '.html'),
                                               ('All files', '.*')])
    if file is None:
        return # this is a way to make sure no error.
    file_text = str(text.get(1.0,END))
    # file_text = input("Enter some text I guess: ") #This is good but can do below if want to enter text via console
    file.write(file_text)
    file.close()

window = Tk()
button = Button(text="save", command=save_file)
button.pack()
text = Text(window)
text.pack()
window.mainloop()


#Lesson 80: Menu Bar
# https://www.youtube.com/watch?v=xiUTqnI6xk8
from tkinter import *

def open_file():
    print("File has been opened")
def save_file():
    print("File has been saved")
def cut():
    print("You cut some text")
def copy():
    print("You copied some text")
def paste():
    print("You pasted some text")

window = Tk()

#If want to add images
#open_image = PhotoImage(file='file.png')
#save_image = PhotoImage(file='save.png')
#exit_image = PhotoImage(file='exit.png')

menubar = Menu(window)
window.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0, font=('MV Boli', 15))
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file) #image=open_image, compound='left')
file_menu.add_command(label="Save", command=save_file) #image=save_image, compound='left')
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit) #image=exit_image, compound='left' )

edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

window.mainloop()


#Lesson 81: Frames
# https://www.youtube.com/watch?v=xiUTqnI6xk8
# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

#button = Button(window,text='W', font=('Consolas', 25), width=3)
#button.pack()

frame = Frame(window, bg='pink', bd=5,relief=RAISED)
#frame.pack(BOTTOM) #place below this replaces this function.
frame.place(x=0,y=0)


Button(frame,text='W', font=('Consolas', 25), width=3).pack(side=TOP)
Button(frame,text='A', font=('Consolas', 25), width=3).pack(side=LEFT)
Button(frame,text='S', font=('Consolas', 25), width=3).pack(side=LEFT)
Button(frame,text='D', font=('Consolas', 25), width=3).pack(side=LEFT)

window.mainloop()


#Lesson 82: New Window
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *

def window_create():
    # window_new = Toplevel() #this new window is dependent on main window.
    window_new = Tk() #this new window is not dependent on main window.
    window_old.destroy()  # this creates a new window and closes out of old window.

window_old = Tk()

Button(window_old,text='create new window', command=window_create).pack()

window_old.mainloop()


#Lesson 83: Window Tabs
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)  # widget that managed a collection of windows/displays

tab1=Frame(notebook)  #this will be new frame for tab 1
tab2=Frame(notebook)
notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.pack(expand=True, fill='both')  #expand = expand to fill any space not used.
                                            # fill = fill space on x and y axis.

Label(tab1,text='Hello, this is tab #1', width=50, height=25).pack()
Label(tab2,text='Goodbye, this is tab #2', width=50, height=25).pack()

window.mainloop()


#Lesson 84: Grid
# https://www.youtube.com/watch?v=xiUTqnI6xk8
# grid()= geometry manager that organizes widgets in a table-like structure in a

from tkinter import *

window = Tk()

titleLabel = Label(window,text="Enter your info", font=('Arial', 15)).grid(row=0,column=0, columnspan=2)

firstNameLabel = Label(window,text='First name: ', width=20,bg='red').grid(row=1, column=0)
firstNameEntry = Entry(window).grid(row=1, column=1)

lastNameLabel = Label(window,text='Last name: ', bg='green').grid(row=2, column=0)
lastNameEntry = Entry(window).grid(row=2, column=1)

emailLabel = Label(window,text='email: ', width=30,bg='blue').grid(row=3, column=0)
emailEntry = Entry(window).grid(row=3, column=1)

submitButton = Button(window, text='Submit').grid(row=4, columnspan=2)

window.mainloop()


#Lesson 85: Progress Bar
# https://www.youtube.com/watch?v=xiUTqnI6xk8
import time
from tkinter import *
from tkinter.ttk import *

def start():
    tasks = 10
    x= 0
    while(x<tasks):
        time.sleep(1)
        bar['value']+=10
        x+=1
        percent.set(str(int((x/tasks)*100))+"%")
        text.set(str(x)+"/"+str(tasks)+" tasks completed")
        window.update_idletasks()

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(window,textvariable=percent).pack()
taskLabel = Label(window,textvariable=text).pack()

button = Button(window,text='download', command=start).pack()

window.mainloop()


#Lesson 86: Canvas
# https://www.youtube.com/watch?v=xiUTqnI6xk8
# canvas = widget that is used to draw graphs, plots, images in a window.

from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500)
#blueLine=canvas.create_line(0,0,500,500, fill='blue', width=5)  # can set this to a value
#redLine=canvas.create_line(0,500,500,0, fill='red', width=5) # notice this is overlaping blue line.
#canvas.create_rectangle(50,50,250,250, fill='purple')
#points = 250,0,500,500,0,500
#canvas.create_polygon(points, fill='yellow', outline='black', width=5)
#canvas.create_arc(0,0,500,500, fill='green', style=PIESLICE, start=180, extent=180)

#create a pokibal
canvas.create_arc(0,0,500,500, fill='red', extent=180, width=10)
canvas.create_arc(0,0,500,500, fill='white', extent=180,start=180, width=10)
canvas.create_oval(190,190,310,310, fill='white', width=10)
canvas.pack()

window.mainloop()


#Lesson 87: Keyboard Events
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import  *

def doSomething(event):
    print("You pressed:" + event.keysym)
    label.config(text=event.keysym)

window = Tk()

# return is enter. Key is any key.
window.bind("<Return>", doSomething)
window.bind("<Key>", doSomething)

label = Label(window,font=('Helvetica', 100))
label.pack()

window.mainloop()


#Lesson 88: Mouse Events
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *

def doSomething(event):
    # this shows where the mouse button was clicked on screen
    print("Mouse coordinates: "+str(event.x)+","+str(event.y))

window = Tk()

window.bind('<Button-1>', doSomething)  # left mouse button click
window.bind('<Button-2>', doSomething)  # mouse scroll wheel
window.bind('<Button-3>', doSomething)  # right mouse button click
window.bind('<ButtonRelease>', doSomething)  # shows where the button release happened
window.bind('<Enter>', doSomething)  # enter the window
window.bind('<Leave>', doSomething)  # leave the window
window.bind('<Motion>', doSomething)  # where the mouse moved

window.mainloop()


#Lesson 89: Drag and Drop
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

window = Tk()

label = Label(window,background='red', width=10, height=5)
label.place(x=0, y=0)

label2 = Label(window,background='blue', width=10, height=5)
label2.place(x=100, y=100)

label.bind('<Button-1>',drag_start) #(event,function)
label.bind('<B1-Motion>',drag_motion)

label2.bind('<Button-1>',drag_start) #(event,function)
label2.bind('<B1-Motion>',drag_motion)

window.mainloop()


#Lesson 90: Move image with keys
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-10)
def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+10)
def move_left(event):
    label.place(x=label.winfo_x()-10, y=label.winfo_y())
def move_right(event):
    label.place(x=label.winfo_x()+10, y=label.winfo_y())

window = Tk()
window.geometry("500x500")

window.bind('<w>', move_up)
window.bind('<s>', move_down)
window.bind('<a>', move_left)
window.bind('<d>', move_right)

myimage = PhotoImage(file='racecar.png')
label = Label(window,image=myimage)
label.place(x=0,y=0)

window.mainloop()


#Lesson 90-b: Moving image on canvas
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *

def move_up(event):
    canvas.move(myimage,0,-10)
def move_down(event):
    canvas.move(myimage,0,10)
def move_left(event):
    canvas.move(myimage,-10,0)
def move_right(event):
    canvas.move(myimage,10,0)

window = Tk()

window.bind('<w>',move_up)
window.bind('<s>',move_down)
window.bind('<a>',move_left)
window.bind('<d>',move_right)
window.bind('<Up>',move_up)
window.bind('<Down>',move_down)
window.bind('<Left>',move_left)
window.bind('<Right>',move_right)

canvas = Canvas(window,width=500,height=500)
canvas.pack()

photoimage = PhotoImage(file='racecar.png')
myimage = canvas.create_image(0,0, image=photoimage, anchor=NW)

window.mainloop()