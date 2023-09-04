# Sample data for food items
food_items = [
    {"FoodID": 1, "Name": "Tandoori Chicken", "Quantity": "4 pieces", "Price": 240, "Discount": 0, "Stock": 50},
    {"FoodID": 2, "Name": "Vegan Burger", "Quantity": "1 piece", "Price": 320, "Discount": 10, "Stock": 30},
    {"FoodID": 3, "Name": "Truffle Cake", "Quantity": "500gm", "Price": 900, "Discount": 5, "Stock": 20},
]

# Sample data for user accounts
registered_users = []

# Sample data for user orders
user_orders = []

# User registration (simplified)
def register_user():
    full_name = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    password = input("Create a password: ")

    # Store user data in a dictionary
    user_data = {
        "Full Name": full_name,
        "Phone Number": phone_number,
        "Email": email,
        "Address": address,
        "Password": password,
    }
    registered_users.append(user_data)
    print("Registration successful!")

# User login (simplified)
def login_user():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check if the user with the given email and password exists
    for user_data in registered_users:
        if user_data["Email"] == email and user_data["Password"] == password:
            return user_data
    return None

# Function to display food items
def display_food_items():
    print("Food Menu:")
    for item in food_items:
        print(
            f"{item['FoodID']}. {item['Name']} ({item['Quantity']}) [INR {item['Price']}] - {item['Stock']} left"
        )

# Function to place a new order
def place_order(user_data):
    display_food_items()
    selected_items = input("Enter the food item numbers you want to order (e.g., 1, 2): ").split(", ")
    selected_items = [int(item) for item in selected_items]

    order = {
        "User": user_data["Full Name"],
        "Items": [],
        "Total Price": 0,
        "Status": "Pending",
    }

    for item_number in selected_items:
        if 1 <= item_number <= len(food_items):
            food_item = food_items[item_number - 1]
            order["Items"].append(food_item)
            order["Total Price"] += food_item["Price"]

    user_orders.append(order)
    print("Order placed successfully!")

# Function to display order history
def order_history(user_data):
    print(f"Order History for {user_data['Full Name']}:")
    for i, order in enumerate(user_orders, start=1):
        if order["User"] == user_data["Full Name"]:
            print(f"Order {i}:")
            for item in order["Items"]:
                print(f"{item['Name']} ({item['Quantity']}) [INR {item['Price']}]")
            print(f"Total Price: INR {order['Total Price']}")
            print(f"Status: {order['Status']}")
            print()

while True:
    print("Options:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        register_user()
    elif choice == "2":
        logged_in_user = login_user()
        if logged_in_user:
            while True:
                print("User Menu:")
                print("1. Place New Order")
                print("2. Order History")
                print("3. Logout")
                inner_choice = input("Enter your choice: ")

                if inner_choice == "1":
                    place_order(logged_in_user)
                elif inner_choice == "2":
                    order_history(logged_in_user)
                elif inner_choice == "3":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Login failed. Invalid credentials.")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

