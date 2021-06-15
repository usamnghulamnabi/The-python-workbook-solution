"""Create a program that reads two integers, a and b, from the user. Your program should
compute and display:

The sum of a and b
The difference when b is subtracted from a
The product of a and b
The quotient when a is divided by b
The remainder when a is divided by b
The result of log 10 a
The result of a b"""

import math

a = int(input("Enter integer a: "))
b = int(input("Enter integer b: "))

add = a + b
sub = a - b
mul = a * b
div = a / b
remainder = a % b
log = math.log10(a)
power = a ** b

print(f"""
The sum of a and b is {add}.
The difference of a and b is {sub}.
The product of a and b is {mul}.
The quotient of a divided by b is {div}.
The remainder of a divided by b is {remainder}.
The result of log 10 a is {log}.
The result of a^b is {power}""")

