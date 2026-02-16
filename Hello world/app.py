while True:
    try:
        quantity = int(input("number of users : "))
        if quantity > 0:
            break
        else:
            print("enter number greater than 0")
    except ValueError:
        print("That's not a number! Try again.")
users_list = []
for i in range(quantity):
    name = (input("full name? : "))
    while True:
        try:
            age = int(input("Age? : "))
            if age < 0 or age > 120:
                print("Need proper age")
            else:
                print(f"You are {age}  years old!")
                if age > 17:
                    print("Unc status!")
                users_list.append([name, age])
                break
        except ValueError:
            print("number")
print("--- list of users data ---")
for user in users_list:
    print(f"user: {user[0]}, {user[1]} years old")
