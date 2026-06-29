weight = int(input("Enter weight: "))
unit = input("Enter the input: ")

if unit == "K" or unit == "KG":
    a = 1

# Alternative way to write if condition
if unit in ("K", "KG", "k", "kg"):
    a = 1

num = 5
print("Positive" if num > 0 else "Negative")

result = "Even" if num % 2 == 0 else "Odd"