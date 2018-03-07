keep_going = "y"

while keep_going == "y":
    sales = float (input("Enter amount of sales: "))
    
    comm_rate = float(input("Enter commission rate: "))
    
    commission = sales * comm_rate
    
    print ("The commission rate is:" ,commission)

    keep_going = input("Enter y if you want calculate another commission: ")
    print()

print ("Nice commission! Have a great day!")
