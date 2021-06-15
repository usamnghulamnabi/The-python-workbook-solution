"""Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added to the
balance of the savings account. Write a program that begins by reading the amount of
money deposited into the account from the user. Then your program should compute
and display the amount in the savings account after 1, 2, and 3 years. Display each
amount so that it is rounded to 2 decimal places."""


deposited = float(input("Enter the amount you deposited: "))

first_year = deposited * 0.04
first = first_year + deposited

second_year = first * 0.04
second = second_year + first

third_year = second * 0.04
third = third_year + second

print(f"After 1 year the amount in saving account would be {first}.\nAfter 2 years the amount in the savings account would be {second}.\nAfter 3 years the amount in the savings account would be {third}.")

