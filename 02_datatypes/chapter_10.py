# Dictionary Examples

chai_order = dict(type="Masala Chai", size="Medium", sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = ["milk"]

print(f"Recipe base: {chai_recipe['base']}")
print(f"recipe: {chai_recipe}")
del chai_recipe["liquid"]
print(f"recipe : {chai_recipe}")

print(f"Is sugar in the order? {'sugar' in chai_order}")

# print(f"Ordered details (keys): {chai_order.keys()}")
# print(f"Ordered details (values): {chai_order.values()}")
# print(f"Ordered details (items): {chai_order.items()}") # returns list of tuples

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")

# chai_size = chai_order["size"]
# print(f"Sugar level in the order: {chai_size}")

customer_note = chai_order.get("note", "No Note")
print(f"Customer note: {customer_note}")