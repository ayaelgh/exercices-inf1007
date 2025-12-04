#mini projects
#exo 1

kettle_boiled = False

if kettle_boiled:
    print("make some chai")

#exo 2
snack = input("Enter yout preferred snack: ").lower() #type it in lower case
print(f"user said: {snack}")

if snack == "cookies" or snack == "samosa":
    print(f"Great choice! {snack}")

else:
    print("Sorry we dont have it")

#exo 3
size = input("What size did you get? ").lower()

if size == "small":
    print("price is 10")

elif size == "medium":
    print("price is 15")

elif size == "large":
    print("price is 20")

else: 
    print("unknown")

#exo 4
device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35:
        print("high")
    else:
        print("temp is normal")

else:
    print("device if offline")

#exo 5

order_amount = int(input("order amount? "))

delivery_fees = 0 if order_amount > 300 else 30 #ternary operator
print(delivery_fees)

#exo6

seat = input("enter seat type? ").lower()

match seat:
    case "sleeper":
        print("no ac")
    case "AC":
        print("AC")
    case "general":
        print("general cheap")
    case "luxury":
        print("luxyyy")
    case _:
        print("invalid")




