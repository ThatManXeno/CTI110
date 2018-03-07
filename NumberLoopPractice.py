keep_going = "y"

while keep_going == "y":

    num = int(input("Please enter a number: "))

    if num ==1:
        print("One")
        print()

    elif num ==2:
        print("Two")
        print()

    elif num ==3:
        print("Three")
        print()

    else:
        print("Sorry, number not within 1 to 3 range")
        print()

    keep_going = input("Do you want to enter another number? Enter y for yes: ")
    print()

print("Alright, have a great day!")
