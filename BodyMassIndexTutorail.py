weight = float(input("Please enter how much you weigh in pounds: "))

height = float(input("Please enter how tall you are in inches: "))

bmi = weight * 703 / height**2

print ("Your Body Mass Index is: ",format(bmi, ".1f"))

if bmi >=18.5 and bmi <=25:
    print("Your BMI is optimal! Keep up the great work")
elif bmi <18.5:
    print("Eat more chicken, your underweight")
elif bmi >25:
    print("Put down the cake, your overweight buddy")
