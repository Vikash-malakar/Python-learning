rooms = {
    101: None,
    102: None,
    103: None,
    104: None,
    105: None
}

ROOM_PRICE = 1500

def show_rooms():
    print("\nRoom Status")

    for room, guest in rooms.items():
        if guest is None:
            print("Room", room, "- Available")
        else:
            print("Room", room, "- Booked by", guest)


def book_room():
    room_no = int(input("Enter Room Number: "))

    if room_no not in rooms:
        print("Invalid Room Number")

    elif rooms[room_no] is None:
        name = input("Enter Guest Name: ")

        rooms[room_no] = name

        print("Room Booked Successfully")

    else:
        print("Room Already Booked")


def checkout():
    room_no = int(input("Enter Room Number: "))

    if room_no not in rooms:
        print("Invalid Room Number")

    elif rooms[room_no] is not None:
        days = int(input("Enter Number of Days: "))

        total_bill = days * ROOM_PRICE

        print("\nGuest Name:", rooms[room_no])
        print("Room Number:", room_no)
        print("Total Bill:", total_bill)

        rooms[room_no] = None

        print("Check-Out Successful")

    else:
        print("Room Is Already Available")


while True:

    print("\n===== HOTEL MANAGEMENT SYSTEM =====")
    print("1. Show Rooms")
    print("2. Book Room")
    print("3. Check Out")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        show_rooms()

    elif choice == "2":
        book_room()

    elif choice == "3":
        checkout()

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")