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
chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")
chai_ingredients.sort()
print(f"chai: {chai_ingredients}")

sugar_levels = [1,2,3,4,5]
print(f"Max sugar level: {max(sugar_levels)}")
print(f"Min sugar level: {min(sugar_levels)}")

# operator overloading

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Full liquid mix: {full_liquid_mix}")

strong_brew = ["black tea", "Water"] * 3
print(f"Strong brew: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMOM")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")