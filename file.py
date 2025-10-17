weight = int(input("Enter the weight in kg : "))
height = int(input("Enter the heigh in meter: "))
bmi = weight / (height ** 2)

print(f"BMI of {weight}kg and {height}m is  {bmi}")

if (bmi >= 18 and bmi <= 25):
    print("Category: Normal")
elif (bmi < 18):
    print("Category: Underweight")
elif (bmi > 25):
    print("Category: Overweight")
else: 
    print("Error")
    