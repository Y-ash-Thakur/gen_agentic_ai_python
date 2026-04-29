# Integer and arithmetic operations related to tea preparation

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea is {remaining_tea}")

milk_liters = 7
servings = 4
milk_per_serving = milk_liters/servings
print(f"Milk per servings is: {milk_per_serving}")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"While tea bags per pot: {bags_per_pot}")

total_cardamom = 10
pots_per_cup = 3
leftover_pods = total_cardamom % pots_per_cup

base_falvor_strength = 2
scale_factor = 3
powerful_flavor_strength = base_falvor_strength ** scale_factor
print(f"Scaled flavor strength is: {powerful_flavor_strength}")

total_tea_leaves_harvested = 1_000_000_000
print(f"Total tea leaves harvested: {total_tea_leaves_harvested}")