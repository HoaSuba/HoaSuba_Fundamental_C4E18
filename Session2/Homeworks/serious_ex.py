height = int(input("What's your height(cm)? "))
weight = int(input("What's your weight? "))
print(" I will show your BMI")

BMI = weight/(height* height/(100**2))
if BMI < 16:
    print("Severely underweight")
elif BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")