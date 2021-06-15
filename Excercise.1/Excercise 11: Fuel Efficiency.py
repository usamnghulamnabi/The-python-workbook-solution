"""In the United States, fuel efficiency for vehicles is normally expressed in miles-per-
gallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units."""

mpg_in = float(input("Eter the value in MPG: "))

convert = 282.48 / mpg_in

print(f"{mpg_in} miles per gallon is equal to {convert} L/100 km.")

