"""
   By Usman GhulamNabi
   usmanghulamnabi@gmail.com
"""


class Calculator():

    def _init_(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


    def add(self):
        return self.num1 + self.num2

    def subs(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

num1 = int(input("enter any  number of your choice"))
num2 = int(input("enter any number of your choice again"))
operation = input('''select any one of the  operation from below + - / * ''')
cal = Calculator(num1, num2)

if operation == "+":
    print(cal.add())

elif operation == "-":
    print(cal.subs())

elif operation == "*":
    print(cal.multiply())

elif operation == "/":
    print(cal.div())

else:
    print("wrong input")
