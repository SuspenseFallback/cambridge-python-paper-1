def check_one_parcel():
    width = ""
    while width == "":
        try:
            width = float(input("Enter width of parcel (in cm): "))
        except ValueError:
            print("Please enter a non-zero numerical value for the parcel width")

        if width == 0:
            print("Please enter a non-zero numerical value for the parcel width")
            width = ""

    length = ""
    while length == "":
        try:
            length = float(input("Enter length of parcel (in cm): "))
        except ValueError:
            print("Please enter a numerical value for the parcel length")

        if length == 0:
            print("Please enter a non-zero numerical value for the parcel length")
            length = ""

    height = ""
    while height == "":
        try:
            height = float(input("Enter height of parcel (in cm): "))
        except ValueError:
            print("Please enter a numerical value for the parcel height")

        if height == 0:
            print("Please enter a non-zero numerical value for the parcel height")
            height = ""

    weight = ""
    while weight == "":
        try:
            weight = float(input("Enter weight of parcel (in kg): "))
        except ValueError:
            print("Please enter a numerical value for the parcel weight")

        if weight == 0:
            print("Please enter a non-zero numerical value for the parcel weight")
            weight = ""

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
        errors_array.append(
            "The sum of all the dimensions should be no more than 200 cm"
        )

    return {"errors": errors_array, "weight": weight}
