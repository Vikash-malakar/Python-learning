print("=== Bus Ticket Booking System ===")

available_seats = 20

while True:
    print("\n1. Book Ticket")
    print("2. Check Available Seats")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter passenger name: ")
        destination = input("Enter destination: ")
        seats = int(input("Enter number of seats: "))
        fare_per_seat = 250

        if seats <= available_seats:
            total_fare = seats * fare_per_seat
            available_seats -= seats

            print("\n=== Ticket Confirmed ===")
            print("Passenger Name:", name)
            print("Destination:", destination)
            print("Seats Booked:", seats)
            print("Total Fare:", total_fare)
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