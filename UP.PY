print("=== Movie Ticket Booking System ===")

available_seats = 30
ticket_price = 200

while True:
    print("\n1. Book Ticket")
    print("2. Check Available Seats")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter customer name: ")
        movie = input("Enter movie name: ")
        seats = int(input("Enter number of tickets: "))

        if seats <= available_seats:
            total = seats * ticket_price
            available_seats -= seats

            print("\n=== Booking Confirmed ===")
            print("Customer Name:", name)
            print("Movie Name:", movie)
            print("Tickets:", seats)
            print("Total Amount:", total)
            print("Remaining Seats:", available_seats)
        else:
            print("Seats Not Available")

    elif choice == "2":
        print("Available Seats:", available_seats)

    elif choice == "3":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")