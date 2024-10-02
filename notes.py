# print () function
print("que onda, esta es mi primera línea de código en python")
# strings are pieces of text and always go in between double quotes ""

#search for feedback and errors on stack overflow
# "SyntaxError: EOL while scanning string literal" means that you miss the double quote before the end of the 

# use double quotes "" or singe quotes '' depending on wich one you want to print on the console
print('elige cual comilla "escribir"')

#beware the decorative “double quotes”, and only use the programming "double quotes" for the real code
print("“decorative double quotes”")

# we use \n in a string to go to the next line
print("para escribir en linea debajo\nhay que poner 'backslash'seguido de 'n'")

#command  "control+enter" to run the console

#concatenate strings by using "+" sign
print("hola"+"luis")
print("hola "+"luis")
print("hola"+" "+"luis")

# we can also use the "*" operator to repeat a string or other items
print("perro"*3)
num = 10
tupla = (0,)*num
print(tupla)

#"IndentationError: unexpected indent" spaces are important so we don't have these kind of errors where we have a space before the line of code where it's not intended to be

#"SyntaxError: unexpected EOF while parsing" means that the end of your source code was reached before all code blocks were completed. For example missing or having more parenthesis than needed

#input () function
#what the user types replaces the input part of the code and it's always a string data type
input("color favorito: ")
print("hola "+input("¿cómo te llamas? "))

#you can use thonny.org or pythontutor.com to se your code in execution
#and use "#" to make comments that the computer will ignore
#use the command "control+/" to convert code lines to comments

#len () function gives you the number of items inside the parenthesis, such as characters on a string or elements in a list
print(len("12345"))
print(len(input("¿cómo te llamas? ")))

#variables
#it's a form to store data and it can change over the course of the program

name="luis"
print(name)
name="eduardo"
print(name)

name=input("write your name: ")
lenght=len(name)
print(lenght)

#variable naming: make your code readable, use words that you can remember what they are
#you can use an underscore "_" to use compound names for your variables
user_score="4"

#you can use numbers for your variable names but they can't be at the beginning of the name of the variable e.g. 1user, 3color
user_score1="4"
user_score2="5"
#don't use words that are assigned to functions as names for your variables e.g. print="45", input="fresa"

#"NameError:name 'xxx' is not defined" usually occurs when you make a typo in your variables

#https://www.google.com/search?sxsrf=ACYBGNRxEaJIWyKHuWI0Lk24t4KuZVyeew:1579706585702&q=how+to+get+the+length+of+a+string+in+python+stack+overflow
