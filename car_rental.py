# ==========================================
# PROJECT 4 - CAR RENTAL SYSTEM
# ==========================================
# ==========================================
# CAR CLASS
# ==========================================

class Car:

    def __init__(self, car_id, name, price):
        self.id = car_id
        self.name = name
        self.price = price
        self.available = True
        self.customer = None
        self.phone = None
        self.days = 0

    def rent(self, customer, phone, days):
        self.available = False
        self.customer = customer
        self.phone = phone
        self.days = days

    def return_car(self):
        self.available = True
        self.customer = None
        self.phone = None
        self.days = 0
# ==========================================
# CAR OBJECTS
# ==========================================

cars = [
    Car(1, "Toyota Corolla", 5000),
    Car(2, "Honda Civic", 6000),
    Car(3, "Suzuki Alto", 3000),
    Car(4, "Kia Sportage", 8000),
    Car(5, "Toyota Yaris", 4500),
    Car(6, "Honda City", 4500),
    Car(7, "Hyundai Tucson", 7500),
    Car(8, "Suzuki Swift", 3500),
    Car(9, "Toyota Fortuner", 12000),
    Car(10, "Kia Picanto", 3500)
]


# ------------------------------------------
# Display Cars
# ------------------------------------------

def display_cars():
    print("\n========== AVAILABLE CARS ==========")

    for car in cars:
        status = "Available" if car.available else "Rented"

        print(
            f"ID: {car.id} | "
            f"Car: {car.name} | "
            f"Price per day: Rs.{car.price} | "
            f"Status: {status}"
        )
# ------------------------------------------
# Return a Car
# ------------------------------------------

def return_car():
    display_cars()

    try:
        car_id = int(input("\nEnter the ID of the car you want to return: "))
    except ValueError:
        print("\nInvalid input! Please enter a valid car ID.")
        return

    for car in cars:

        if car.id == car_id:

            if not car.available:

                customer = car.customer

                car.return_car()

                print("\n========== CAR RETURNED ==========")
                print("Customer:", customer)
                print("Car:", car.name)
                print("Car has been returned successfully.")

            else:
                print("\nThis car is already available.")

            return

    print("\nCar ID not found.")

# ------------------------------------------
# Rent a Car
# ------------------------------------------

def rent_car():
    display_cars()

    customer_name = input("\nEnter customer name: ")

    if not customer_name.strip():
        print("\nCustomer name cannot be empty.")
        return

    phone = input("Enter customer phone number: ")

    if not phone.isdigit():
        print("\nInvalid phone number! Please enter digits only.")
        return

    if len(phone) < 10 or len(phone) > 15:
        print("\nInvalid phone number! Please enter a valid number.")
        return

    try:
        car_id = int(input("Enter the ID of the car you want to rent: "))
        days = int(input("Enter number of rental days: "))
    except ValueError:
        print("\nInvalid input! Please enter numbers only.")
        return

    if days <= 0:
        print("\nRental days must be greater than 0.")
        return

    for car in cars:

        if car.id == car_id:

            if car.available:

                car.rent(customer_name, phone, days)

                total_cost = car.price * days

                print("\n========== RENTAL SUCCESSFUL ==========")
                print("Customer:", customer_name)
                print("Phone:", phone)
                print("Car:", car.name)
                print("Rental Days:", days)
                print("Price Per Day: Rs.", car.price)
                print("Total Cost: Rs.", total_cost)

            else:

                print("\nSorry! This car is already rented.")
                print("Rented by:", car.customer)

            return

    print("\nCar ID not found.")
  # ------------------------------------------
# Search Car
# ------------------------------------------

def search_car():

    search_name = input("\nEnter car name to search: ").lower()

    found = False

    for car in cars:

        if search_name in car.name.lower():

            found = True

            status = "Available" if car.available else "Rented"

            print("\n========== CAR FOUND ==========")
            print("ID:", car.id)
            print("Car:", car.name)
            print("Price Per Day: Rs.", car.price)
            print("Status:", status)

    if not found:
        print("\nNo car found with that name.")
# ------------------------------------------
# View Rental Records
# ------------------------------------------

def view_rentals():
    print("\n========== RENTAL RECORDS ==========")

    found = False

    for car in cars:

        if not car.available:
            found = True

            total_cost = car.price * car.days

            print("Customer:", car.customer)
            print("Phone:", car.phone)
            print("Car:", car.name)
            print("Rental Days:", car.days)
            print("Price Per Day: Rs.", car.price)
            print("Total Cost: Rs.", total_cost)
            print("-----------------------------------")

    if not found:
        print("No cars are currently rented.")

# ------------------------------------------
# Main Menu
# ------------------------------------------

while True:

    print("\n================================")
    print("       CAR RENTAL SYSTEM")
    print("================================")
    print("1. View Cars")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. View Rental Records")
    print("5. Search Car")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_cars()

    elif choice == "2":
        rent_car()

    elif choice == "3":
        return_car()

    elif choice == "4":
        view_rentals()

    elif choice == "5":
        search_car()

    elif choice == "6":
        print("\nThank you for using Car Rental System!")
        break

    else:
        print("\nInvalid choice! Please try again.")