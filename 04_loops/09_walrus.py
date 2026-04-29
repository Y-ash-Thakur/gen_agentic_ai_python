# value = 13
# remainder = value % 3

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")


# value = 13
# if (remainder := value % 3):
#     print(f"Not divisible, remiander is {remainder}")


# available_sizes = ["small", "medium", "large"]

# if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
#     print(f"Serving {requested_size} chai")
# else:
#     print(f"Size is unavailable - {requested_size}")

flavors = ["Ginger", "masala", "lemon", "mint"]

print("Available flavors are: ", flavors)

while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available.")

print(f"you choose {flavor} chai")
