"""Practice with dictionaries - 2023-10-24."""

# Constructing a dictionary; this is a bit like JavaScript, huh.
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

# Adding a key/value pair
ice_cream["mint"] = 3

# Removing a thing
ice_cream.pop("mint")

# Accessing and modifying dictionary values: subscription notation
print(ice_cream["chocolate"])
ice_cream["vanilla"] = 10

print(len(ice_cream))

# Checking if key is in dictionary
if "mint" in ice_cream:
    print(f"{ice_cream['mint']} orders of mint!")
else:
    print("No orders of mint...")

if "mint" in ice_cream and "chocolate" in ice_cream:
    print("woah, chocomint")

# Looping!
for key in ice_cream:
    print(key, ice_cream[key])

print(ice_cream)
