end = int(input("Enter ending limit for the program: "))


print("KPH \t MPH")
print("------------")



for kph in range (60, end+1,10):
    mph = kph * 0.6214
    print(kph, "\t",format(mph,",.1f"))
