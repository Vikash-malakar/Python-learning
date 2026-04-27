print("=== Hotel Room Booking System ===")

single_rooms = 10
double_rooms = 5

while True:
    print("\n1. Book Single Room")
    print("2. Book Double Room")
    print("3. Check Available Rooms")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter customer name: ")
        rooms = int(input("Enter number of rooms: "))
        price = 1000

        if rooms <= single_rooms:
            total = rooms * price
            single_rooms -= rooms

            print("\nBooking Confirmed")
            print("Customer Name:", name)
            print("Room Type: Single")
            print("Rooms Booked:", rooms)
            print("Total Bill:", total)
        else:
            print("Rooms Not Available")

    elif choice == "2":
        name = input("Enter customer name: ")
        rooms = int(input("Enter number of rooms: "))
        price = 1800

        if rooms <= double_rooms:
            total = rooms * price
            double_rooms -= rooms

            print("\nBooking Confirmed")
            print("Customer Name:", name)
            print("Room Type: Double")
            print("Rooms Booked:", rooms)
            print("Total Bill:", total)
        else:
            print("Rooms Not Available")

    elif choice == "3":
        print("Single Rooms Available:", single_rooms)
        print("Double Rooms Available:", double_rooms)

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")