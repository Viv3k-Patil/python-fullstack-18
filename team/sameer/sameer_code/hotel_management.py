class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_booked = False
        self.customer = None
        self.days = 0

    def book_room(self, customer, days):
        if not self.is_booked:
            self.is_booked = True
            self.customer = customer
            self.days = days
            return f"✅ Room {self.room_number} booked for {customer.name}"
        return f"❌ Room {self.room_number} already booked"

    def checkout(self):
        if self.is_booked:
            total_bill = self.days * self.price
            customer_name = self.customer.name

            # Reset room
            self.is_booked = False
            self.customer = None
            self.days = 0

            return f"💰 Checkout successful for {customer_name}. Total bill: ₹{total_bill}"
        return "❌ Room was not booked"


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def show_rooms(self):
        print("\n--- Room Status ---")
        for room in self.rooms:
            status = "Booked" if room.is_booked else "Available"
            print(f"Room {room.room_number} | {room.room_type} | ₹{room.price} | {status}")

    def show_available_rooms(self):
        print("\n--- Available Rooms ---")
        for room in self.rooms:
            if not room.is_booked:
                print(f"Room {room.room_number} | {room.room_type} | ₹{room.price}")

    def find_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None


# ---------------- MAIN PROGRAM ---------------- #

hotel = Hotel("Grand Stay Hotel")

# Predefined rooms
hotel.add_room(Room(101, "Single", 1000))
hotel.add_room(Room(102, "Double", 2000))
hotel.add_room(Room(103, "Suite", 5000))
hotel.add_room(Room(104, "Deluxe", 3000))


while True:
    print("\n====== HOTEL MANAGEMENT SYSTEM ======")
    print("1. Show All Rooms")
    print("2. Show Available Rooms")
    print("3. Book Room")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        hotel.show_rooms()

    elif choice == "2":
        hotel.show_available_rooms()

    elif choice == "3":
        room_no = int(input("Enter room number: "))
        room = hotel.find_room(room_no)

        if room:
            if not room.is_booked:
                name = input("Enter customer name: ")
                phone = input("Enter phone number: ")
                days = int(input("Number of days: "))

                customer = Customer(name, phone)
                print(room.book_room(customer, days))
            else:
                print("❌ Room already booked")
        else:
            print("❌ Room not found")

    elif choice == "4":
        room_no = int(input("Enter room number: "))
        room = hotel.find_room(room_no)

        if room:
            print(room.checkout())
        else:
            print("❌ Room not found")

    elif choice == "5":
        print("👋 Thank you for using the system!")
        break

    else:
        print("❌ Invalid choice. Try again.")