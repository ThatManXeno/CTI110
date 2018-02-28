number = int(input("How many books did you purchase this month? "))

if number ==0 or number ==1:
    print("You earned 0 points this month")
elif number ==2 or number ==3:
    print("You earned 5 points this month, congratulations!")
elif number ==4 or number ==5:
    print("You earned 15 points this month, congratulations!")
elif number ==6 or number ==7:
    print("You earned 30 points this month, congratulations!")
elif number ==8 or number ==9:
    print("You earned 60 points this month, congratulations!")
else:
    print("You earned a million points, stop buying books!")
