"""Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres."""

length = float(input("Enter the length of the field in feet: "))
width = float(input("Enter the width of the field in feet: "))

areainfeet = length * width
areainacre = areainfeet / 43560

print(f"The area of your field in acres is {areainacre} acres")

