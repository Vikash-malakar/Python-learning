seats = [
    ["A1", "A2", "A3"],
    ["B1", "B2", "B3"],
    ["C1", "C2", "C3"]
]

booked_seats = []

TICKET_PRICE = 200


def show_seats():
    print("\nAvailable Seats")

    for row in seats:
        for seat in row:
            if seat in booked_seats:
                print("XX", end=" ")
            else:
                print(seat, end=" ")
        print()


def book_ticket():
    seat = input("Enter Seat Number: ").upper()

    all_seats = []

    for row in seats:
        all_seats.extend(row)

    if seat not in all_seats:
        print("Invalid Seat Number")

    elif seat in booked_seats:
        print("Seat Already Booked")

    else:
        booked_seats.append(seat)

        print("Booking Successful")
        print("Seat:", seat)
        print("Amount:", TICKET_PRICE)


while True:

    print("\n===== MOVIE BOOKING SYSTEM =====")
    print("1. Show Seats")
    print("2. Book Ticket")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        show_seats()

    elif choice == "2":
        book_ticket()

    elif choice == "3":
        print("Thank You")
        break

    else:
        print("Invalid Choice")