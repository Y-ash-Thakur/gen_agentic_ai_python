# Mutable data types example: sets

spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice mix : {(spice_mix)}")
spice_mix.add("cinnamon")
spice_mix.add("cardamom")
print(f"Initial spice mix : {(spice_mix)}")
print(f"Updated spice mix id: {id(spice_mix)}")