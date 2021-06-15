"""An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos from the user. Then your program should compute
and display the total weight of the parts."""

widgets_numbers = int(input("Enter the number of widgets: "))
gizmos_numbers = int(input("Enter the number of Gizmos: "))

weight_widgets = widgets_numbers * 75
weight_gizmos = gizmos_numbers * 112

total = weight_widgets + weight_gizmos

print(f"""The weight of widgets is {weight_widgets} grams and weight of Gizmos is {weight_gizmos} grams.
The total weight of Gizmos and widgets is {total} grams.""")

