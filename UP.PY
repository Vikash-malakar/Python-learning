available_seats = 20
bookings = {}

def book_ticket():
    global available_seats

    if available_seats == 0:
        print("No Seats Available")
        return

    name = input("Enter Passenger Name: ")
    age = int(input("Enter Age: "))

    ticket_id = len(bookings) + 1

    bookings[ticket_id] = {
        "name": name,
        "age": age
    }

    available_seats -= 1

    print("Ticket Booked Successfully")
    print("Ticket ID:", ticket_id)


def view_bookings():
    if len(bookings) == 0:
        print("No Bookings Found")
        return

    print("\nPassenger List")

    for ticket_id, data in bookings.items():
        print(
            "Ticket ID:", ticket_id,
            "| Name:", data["name"],
            "| Age:", data["age"]
        )


def cancel_ticket():
    global available_seats

    ticket_id = int(input("Enter Ticket ID: "))

    if ticket_id in bookings:
        del bookings[ticket_id]
        available_seats += 1

        print("Ticket Cancelled Successfully")
    else:
        print("Invalid Ticket ID")


def check_seats():
    print("Available Seats:", available_seats)


while True:

    print("\n===== RAILWAY RESERVATION SYSTEM =====")
    print("1. Book Ticket")
    print("2. View Bookings")
    print("3. Cancel Ticket")
    print("4. Check Available Seats")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        book_ticket()

    elif choice == "2":
        view_bookings()

    elif choice == "3":
        cancel_ticket()

    elif choice == "4":
        check_seats()

    elif choice == "5":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")