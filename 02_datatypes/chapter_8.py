# Mutable
# List

ingredients = ["water", "milk", "ginger"]
ingredients.append("sugar")
print(f"Ingredients: {ingredients}")
ingredients.remove("water")
print(f"Ingredients after removal: {ingredients}")

spice_options = ["ginger", "cardamom", "cloves"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"Chai ingredients: {chai_ingredients}")
chai_ingredients.insert(2, "tea leaves")
print(f"Chai ingredients after insert: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"Last added ingriedient: {last_added}")
print(f"chai: {chai_ingredients}")