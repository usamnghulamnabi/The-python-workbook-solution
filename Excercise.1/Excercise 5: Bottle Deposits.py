"""In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and two digits to the right of the decimal point."""


liter = int(input("Enter the number of bottles of 1 liter or less. \nEnter 0 if none: "))
more = int(input("Enter the number of bottles of more than 1 liter. \nEnter 0 if none: "))

litermoney = liter * 0.10
if liter == 0:
    print("you didn't enter any value for liter bottles")
    pass
else:
    print(f"You will get ${litermoney} for recycling {liter} Bottles")

moremoney = more * 0.25
if more == 0:
    print("You didn't enter any value for larger bottles")
    pass
else:
    print(f"You will get ${moremoney} for recycling {more} Bottles")

