print("Bus Reservation System")

total_seats = 10
bookings = {}

while True:
    print("\n1. Book Seat")
    print("2. View Bookings")
    print("3. Check Available Seats")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        if total_seats == 0:
            print("No Seats Available")

        else:
            name = input("Enter passenger name: ")
            seat_number = input("Enter seat number: ")

            if seat_number in bookings:
                print("Seat Already Booked")

            else:
                bookings[seat_number] = name
                total_seats -= 1

                print("Seat Booked Successfully")

    elif choice == "2":
        print("\nBooking Details")

        if len(bookings) == 0:
            print("No Bookings Found")

        else:
            for seat, name in bookings.items():
                print("Seat:", seat, "| Passenger:", name)

    elif choice == "3":
        print("Available Seats:", total_seats)

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")