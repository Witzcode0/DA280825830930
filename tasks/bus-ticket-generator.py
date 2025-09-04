import random

print("===== Welcome to Bus ticket Booking system =====")

b1_seats = 2
b1_route = "Surat to Ahemadabad"
b1_price = 600

b2_seats = 20
b2_route = "Surat to Baroda"
b2_price = 300

b3_seats = 30
b3_route = "Surat to Mumbai"
b3_price = 1200

while(1):
    print("\nAvailable Buses: ")
    print(f"1. {b1_route} | seats : {b1_seats} | Price : {b1_price}")
    print(f"2. {b2_route} | seats : {b2_seats} | Price : {b2_price}")
    print(f"3. {b3_route} | seats : {b3_seats} | Price : {b3_price}")

    # print("1. ",b1_route," | seats : ",b1_seats, " | Price : ",b1_price)
    # print("2. ",b2_route," | seats : ",b2_seats, " | Price : ",b2_price)
    # print("3. ",b3_route," | seats : ",b3_seats, " | Price : ",b3_price)

    choice = int(input("\nEnter bus number to book (0 to exit): "))

    if choice == 0:
        print("\nThank you for using the bus ticket booking system!")
        break

    if choice == 1:
        if b1_seats <= 0:
            print("No seats available on this bus.")
            continue
        route = b1_route
        price = b1_price
    elif choice == 2:
        if b2_seats <= 0:
            print("No seats available on this bus.")
            continue
        route = b2_route
        price = b2_price
    elif choice == 3:
        if b3_seats <= 0:
            print("No seats available on this bus.")
            continue
        route = b3_route
        price = b3_price
    else:
        print("Invalid choice. Try again!")
        continue

    name = input("Enter passenger name: ")
    age = int(input("Enter passenger age: "))

    if age < 12:
        price = price * 0.5
    elif age >= 60:
        price = price * 0.7

    confirm = input(f"Ticket price is {price} INR. confirm booking? [yes/no]: ")

    if confirm != "yes":
        print("Nooking canceled.")
        continue

    if choice == 1:
        b1_seats -= 1
    elif choice == 2:
        b2_seats -= 1
    elif choice == 3:
        b3_seats -= 1

    token = random.randint(100000, 999999)



    print("\n ===== Ticket booked successfully! ===== ")
    print(f"Passenger name: {name}")
    print(f"Passenger age: {age}")
    print(f"Route {route}")
    print(f"Price {price}")
    print(f"Price {price}")
    print(f"Ticket token : {token}")
    print("===========================================")

    another_ticket = input("Book another ticket? [yes/no]: ")
    if another_ticket != "yes":
        print("Thank you for using the bus ticket  booking system!")
        break




