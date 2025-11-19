# Set operations with spices

essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
print(f"ALl Spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"Common Spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only in essential: {only_in_essential}")

print(f"is 'cloves' in optional spices? {'cloves' in optional_spices}")