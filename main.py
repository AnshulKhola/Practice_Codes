# from math import *
# text = "anshul"
# print(text.upper().isupper())
# print(len(text))
# print(text[0])
# print(text.index("h"))
# print(text.replace("anshul", "anshul khola"))
# num = 5
# print(str(num)+ " is my fav number")
# print(pow(3, 2))
# print(max(4, 6))
# print(min(4, 6))
# print(round(3.2))
# print(round(3.7))
# print(floor(3.7))
# print(ceil(3.7))
# print(int(sqrt(36)))
# input function
# name  = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + " !" + " You are " + age + " years old.")
# # calculator
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2)
# print(result)
# # mad libs game
# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")

# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

# list
# friends = ['Anshul','Himanshu','Aichu','Deepak','Rajjo']
# print(friends)
# print(friends[0])
# print(friends[-1])
# print(friends[1:])
# print(friends[1:3])
# friends[1] = 'Anshu'
# print(friends)

# list functions
# lucky_numbers = [4, 8, 15, 16, 23, 42]
# friends = ['Anshul','Himanshu','Aichu','Deepak','Rajjo']
# friends.extend(lucky_numbers)
# friends.append('Aman')
# friends.insert(1,'Aman')
# friends.remove('Aichu')
# friends.clear()
# friends.pop()
# print(friends.index('Mike'))
# friends.sort()
# lucky_numbers.reverse()
# friends2 = friends.copy()
# print(friends2)
# print(lucky_numbers)
# print(friends)

# tuple -> It is basicly a data structure in which we can store multiple values but we can't change them as we do in list and tuple is immutable.
# tuple is always in round brackets
# coordinates = (4,5)
# coordinates[1] = 10
# print(coordinates[0])
# print(coordinates[1])

# functions
# def say_hi(name,age):
#     print("Hello " + name + " !" + " You are " + str(age) + " years old.")

# print("Top")
# say_hi("Anshul",21)
# print("Bottom")

# return statements
# def cube(num):
#     return num*num*num

# result = cube(4)
# print(result)

# if statements
# is_Male = True
# is_Tall = False

# if is_Male and is_Tall:
#     print("You are a tall male")
# elif is_Male and not(is_Tall):
#     print("You are a short male")
# elif not(is_Male) and is_Tall:
#     print("You are not a male but are tall")
# else:
#     print("You are neither a male nor tall")

# if statements and comparison
# def max_num(num1,num2,num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3

# print(max_num(43,94,34))

# building a better calculator
# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2  = float(input("Enter second number: "))

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "*":
#     print(num1 * num2)
# elif op == "/":
#     print(num1 / num2)
# else:
#     print("Invalid operator")

# Dictionaries
# monthConversations = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December"
# }

# print(monthConversations["Nov"])
# print(monthConversations.get("Dec"))

# while loop
# i = 1
# while i<= 10:
#     print(i)
#     i += 1

# print("Done with loop")

# guess game
# secret_word = "anshul"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#         break

# if out_of_guesses:
#     print("Out of guesses, You lose!")
# else:
#     print("You win in " + str(guess_count) + " guesses!")

# for loop
# for letter in "Anshul":
#     print(letter)

# friends = ['Anshul','Himanshu','Aichu','Deepak','Rajjo']
# for friend in friends:
#     print(friend)
# for index in range(len(friends)):
#     print(friends[index])

# exponent function

# def raise_to_power(base_num,pow_num):
#     result = 1
#     for index in  range(pow_num):
#         result = result*base_num
#     return result

# print(raise_to_power(3,2))

# 2D lists and nested loops

# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]

# print(number_grid[0][0])
# for row in number_grid:
#     for col in row:
#         print(col)

# build a translator

# def translate(phrase):
#     transition = ""
#     for letter in phrase:
#         if letter in "AEIOUaeiou":
#             transition = transition + "g"
#         else:
#             transition = transition + letter
#     return transition

# string  = input("Enter a phrase: ")
# print(translate(string))

'''What about 
you do some 
practice on your
own?'''

# try/except

# try: 
#     value = 10/0
#     num = int(input("Enter a number: "))
#     print(num)
# except ZeroDivisionError as err:
#     print(err)
# except:
#     print("Invalid input")

# reading files
# employee_file = open("employees.txt","r")
# print(employee_file.readable())
# print(employee_file.read())
# print(employee_file.readline())
# print(employee_file.readlines())
# for employee in employee_file.readlines():
    # print(employee)
# print(employee_file.readlines()[1])
# employee_file.close()

# writing to files
# employee_file = open("employees.txt","a")
# employee_file.write("\nToby - Human Resources")
# employee_file.close()
# employee_file = open("employees1.txt","w")
# employee_file.write("\nToby - Human Resources")
# employee_file.close()
# employee_file = open("index.html","w")
# employee_file.write("<p>This is HTML</p>")
# employee_file.close()

# modules and pip
# module is a file containing python code that can be imported and used in another python file
# module is of two types: built-in modules and external modules
# built-in modules are already present in python
# external modules are not present in python, you have to install them
# lib contains all the external modules
# pip is a package manager for python packages, you can install packages using pip
# import useful_tools
# print(useful_tools.roll_dice(6))

# classes and objects
# class is a blueprint/template for creating objects
# object is an instance of a class / is an actual student with information 
# from Student import Student

# student1 = Student("Anshul","ECE",8.5,False)

# print(student1.name)
# print(student1.gpa)

# multiple choice quiz
# from Question import Question

# question_prompts = [
#     "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#     "What color are bananas?\n(a) Red\n(b) Yellow\n(c) Blue\n\n",
#     "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
# ]

# questions = [
#     Question(question_prompts[0],"a"),
#     Question(question_prompts[1],"b"),
#     Question(question_prompts[2],"b")
# ]

# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompts)
#         if answer == question.answer:
#             score += 1

#     print("You got  " + str(score) + "/" + str(len(questions)) + " correct")

# run_test(questions)

# from Student import Student

# s1 = Student("Anshul","ECE",8.5)
# s2 = Student("Himanshu","IT",8)

# print(s1.on_honour_roll())
# print(s2.on_honour_roll())

# inheritance
# from Chef import Chef
# from ChineseChef import ChineseChef

# myChef = Chef()
# myChef.make_special_dish()

# myChineseChef = ChineseChef()
# myChineseChef.make_special_dish()
# myChineseChef.make_fried_rice()


# python interpreter
# python is an interpreted language
# python interpreter reads the code line by line and executes it

# Terminal is used as a python interpreter

