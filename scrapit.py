import math
import string

def add(num1, num2):
   return num1 + num2

def subs(num1, num2):
   return num1 - num2

def mult(num1, num2):
   return num1 * num2

def div(num1, num2):
   return num1 / num2

def mod(num1, num2):
   return num1 % num2

def menu():
   print(" CALCULATE\n")
   print(" Available functions:")
   print("\t + Addition ")
   print("\t - Substraction ")
   print("\t * Multiplication")
   print("\t / Divition")
   print("\t % Module")
   op = input("Selection:   ")
   if(op == '+'):
      val1 = input("Value #1: ")
      val2 = input("Value #2: ")
      sum = add(val1,val2)
      print("The sum is ", sum)

menu()