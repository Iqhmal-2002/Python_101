name = input("What is your name?\n")
age = int(input("What is your age?\n"))

print(f"Your name is {name}")
print(f"Your age is {age}")

length = float(input("Enter length: "))
width = float(input("Enter the width: "))

area = length*width

print(f"Area is {area}cm")

item = input("What item you want to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many items?: "))
total_price = price*quantity

print(f"You are buying {item} for the price of {price} and quantity of {quantity}.")
print(f"The total price is {total_price}")