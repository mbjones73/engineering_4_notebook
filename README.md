# Engineering_4_Notebook
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.

I didn't ask you to document hello_world.py or dice_roller.py. I'll start off with an example for dice_roller.py, and then you will reflect on calculator.py.

## Table of Contents
* [Basics](#Basics)
* [Python_Dice_Roller](#PythonDiceRoller)
* [Python_Calculator](#Python_Calculator)
* [Quadratic Solver](#QuadraticSolver)
* [Strings and Loops](#Strings_and_Loops)
* [MSP Challenge](#MSP_Hangman)
* [Cad 2.1-2.5](#Cad_2.1-2.5)
---


## Python_Dice_Roller

Okay so I am giving you a freebie so you have an example of the kind of reflections that I want. I'll start you off with an example for dice_roller.py, then its up to you to start your reflections with the Python calculator and all subsequent assignments. You can delete this section from your personal readme. 

### Assignment Description

The purpose of this assignment was to create a program that can automatically roll dice. The program also took user input to decide whether another dice should be rolled, or if the program should exit. The spicy version added complexity by asking the user to specify the number of sides on the dice and the number of dice to be rolled at a time. The user was then asked whether they wanted to roll again with the same settings, change the settings, or exit the program. 

### Evidence 

Vanilla version:

![Screenshot 2021-09-10 3 15 26 PM](https://user-images.githubusercontent.com/89222808/133513775-a3eafb43-f836-4e4f-8aa6-e28ca584901f.png)

Spicy version:

![Screenshot 2021-09-10 3 18 38 PM](https://user-images.githubusercontent.com/89222808/133513750-727cdb6c-1c27-4c8a-83d4-50ea9136a221.png)

### Wiring

N/A

### Reflection

This assignment was relatively simple, but was challenging because I had not coded in Python for several months. I learned that I could import parts of toolboxes without importing the entire thing, but that changes the syntax of how I call the function later. I also learned about using a while loop to control whether a user wants to exit the program. For the spicy version, I needed to use nested loops. Python determines what is inside a loop by the indent level of each line of text, rather than brackets like some other coding styles. That means I need to be really careful with my tabs!


## Python_Calculator

### Assignment Description

This assignment was to make a code to create a calculator.
### Evidence 
![Screenshot 2021-09-10 3 18 38 PM](https://raw.githubusercontent.com/mbjones73/engineering_4_notebook/main/python/calcoutput2.PNG)

### Wiring


### Reflection

This was a benficial assignment because I learned how to use functions and realised what I can do with them. At first it was real hard to understand a function. But in engineering I learned the internet is your best friend. Now I understand that they take in variables and you have to use 'return' inside the function in order to output values.



## QuadraticSolver

### asignment description
assignment was to create a calculator to solve quadratics.
### Evidence 

### Reflection
This assignment taught me the syntax for squaring things in Python, a ** x, as well as how to import and use the square root function, from math import sqrt and sqrt(x). I also learned how to use f strings to be able to put variables inside of strings more easily,
f" This is {variableA} and {variableB}".



## Strings_and_Loops
 
### asignment description
 I wrote a program that takes a sentence input by the user and prints out each character on a new line, with a - after each word. 
### Evidence 

### Reflection
In this assignment I learned a few things, but didn't run in to any major obstacles. While doing the vanilla version, I learned that in Python, you can use list(string) to create a list with each character in the string as its own element and string.split() to create a list of each substring in the string between a certain character, which defaults to a space. In the spicy version, I learned a new string method (you can replace every instance of a certain character in a string with another character using string.replace(oldCharacter, newCharacter)), but my main takeaway that Python for loop syntax can be very strange; you can put a print statement on the same line before the for statement it is printing the value of, but only if you have brackets around it. (I think, at least, although I have no idea why this syntax would be used)



## MSP_Hangman

### asignment description
assignment was to create a hangman game.
### Evidence 
![screenshot](https://github.com/mbjones73/engineering_4_notebook/blob/main/python/Screenshot%202021-10-07%209.51.27%20PM%20(3).png)
### Reflection
In this assignment I learned alot with false statements and with if statements. Its useful to learn them before to make this easy. But when you're like me you never prepare. So I went and used my best friend(the internet). I learned to replace a certain character at certain place in a string, you can use string = string[:index] + characterReplacement + string[index+1:]

## Cad_2.1-2.5
### Assignment Description

this assignment was to create a skateboard.

### Evidence 

![screenshot](https://github.com/mbjones73/engineering_4_notebook/blob/main/skateboard.PNG)


### Reflection
This was a fun assignment because its a cool object. While working through all the different parts you learn a lot of skills. The fillet key will be the most used feature. You use a lot of extrude and revolve features. And during the drawing centerlines are very helpful!!!
