
weight = int(input("Weight: "))
unit = input("(k)g or (l)bs: ")
if unit.upper() == "K":
    weight_in_kilos = weight
    weight_in_pounds = weight_in_kilos/ 0.45
    print("Weight in Lbs: " + str(weight_in_pounds))
else:
    weight_in_kilos = weight * 0.45
    print("Weight in Kgs: " + str(weight_in_kilos))

height = int(input("What is your height in centimeters?: "))
height_in_meters = height / 100
BMI = weight_in_kilos / (height_in_meters * height_in_meters)

print(f"Your Body mass index is, {BMI}")
