print("Welcome to car rentals!")
continue_car = input("Would you like to continue (y/n)? ")

while continue_car == "y":
    customer_code = (input("Customer code (b or d): "))
    number_days = int(input("Number of days: "))
    odometer_start = int(input("Odometer reading at the start: " ))
    odometer_end = int(input("Odometer reading at the end: "))
    miles_driven = odometer_end - odometer_start
    amount_due_b = miles_driven * 0.25 + number_days * 40
    amount_due_d = (miles_driven - (100 * number_days)) * 0.25 + number_days * 60
    print("Miles driven:", miles_driven)
    if customer_code == "d": 
        print("Amount due:", round(amount_due_d, 1))
    elif customer_code == "b":  
        print("Amount due:", round(amount_due_b, 1))
    continue_car2 = (input("Would you like to continue (y/n)? "))
    if continue_car2 == "n":
        break 
   
