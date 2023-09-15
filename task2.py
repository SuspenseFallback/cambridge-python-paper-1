from check_one_parcel import check_one_parcel
from calc_cost import calc_cost

number_of_parcels = ""
while number_of_parcels == "":
    try:
        number_of_parcels = int(input("Enter the number of parcels: "))
    except ValueError:
        print("Please enter an integer value for the number of parcels")

total_error_list = []
number_of_accepted_parcels = 0
weight_of_accepted_parcels = 0
number_of_rejected_parcels = 0
total_cost_of_packages = 0
cost_of_accepted_packages = 0

for i in range(number_of_parcels):
    print("\nParcel", i + 1)
    print("-" * 30, "\n")

    values = check_one_parcel()
    errors = values["errors"]
    weight = values["weight"]

    if len(errors) > 0:
        number_of_rejected_parcels += 1
    else:
        number_of_accepted_parcels += 1
        weight_of_accepted_parcels += weight
        cost_of_accepted_packages = calc_cost(weight)

    total_cost_of_packages = calc_cost(weight)

    total_error_list.append([errors, weight, calc_cost(weight)])

print("\n", "-" * 30, "\n")

print("Weight of total consignment:", total_cost_of_packages, "kg \n")

print("Number of accepted parcels:", number_of_accepted_parcels)
print("Cost of accepted parcels:", "$", cost_of_accepted_packages)
print("Weight of accepted parcels:", weight_of_accepted_parcels, "kg \n")
print("Number of rejected parcels:", number_of_rejected_parcels)
print(
    "Cost of rejected parcels:", "$", total_cost_of_packages - cost_of_accepted_packages
)


print("\n", "-" * 30, "\n")

for i in range(0, len(total_error_list)):
    print("\n Parcel", i + 1)
    print("-" * 30, "\n")
    errors = total_error_list[i][0]
    weight = total_error_list[i][1]
    cost = total_error_list[i][2]

    print("Weight:", weight, "kg")
    print("Cost:", "$" + str(cost))

    if errors == []:
        print("Accepted")
    else:
        print("Rejected due to the following reasons: \n")
        for err in errors:
            print(err)
