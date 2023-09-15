width = ""
while width == "" and width != 0:
    try:
        width = float(input("Enter width of parcel (in cm): "))
    except ValueError:
        print("Please enter a numerical value for the parcel width")


length = ""
while length == "" and length != 0:
    try:
        length = float(input("Enter length of parcel (in cm): "))
    except ValueError:
        print("Please enter a numerical value for the parcel length")

height = ""
while height == "" and height != 0:
    try:
        height = float(input("Enter height of parcel (in cm): "))
    except ValueError:
        print("Please enter a numerical value for the parcel height")


weight = ""
while weight == "" and weight != 0:
    try:
        weight = float(input("Enter weight of parcel (in kg): "))
    except ValueError:
        print("Please enter a numerical value for the parcel weight")

errors_array = []

if height > 80:
    errors_array.append("The height must be no more than 80 cm")

if width > 80:
    errors_array.append("The width must be no more than 80 cm")

if length > 80:
    errors_array.append("The length must be no more than 80 cm")

if weight < 1 or weight > 10:
    errors_array.append(
        "The weight of the parcel weight must be between 1 and 10 kilograms inclusive"
    )

if height + width + length > 200:
    errors_array.append("The sum of all the dimensions should be no more than 200 cm")

if len(errors_array) > 0:
    print("\nYour parcel has been rejected due to the following reasons: \n")
    for error in errors_array:
        print(error)
else:
    print("\nYour parcel has been accepted.")
