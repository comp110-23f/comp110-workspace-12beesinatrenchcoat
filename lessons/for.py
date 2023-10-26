"""Learning about for loops."""

xs: list[int] = [1, 2, 3]

for elem in xs:
    print(elem)

pets: list[str] = ["Louie", "Bo", "Bear"]

for pet in pets:
    print(f"Good boy, {pet}!")

names: list[str] = ["Alyssa", "Janet", "Vrinda"]

for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")
