# Dictionary storing planet names and their gravity factors relative to Earth
gravity_factors = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Prompt the user for their Earth weight
earth_weight = float(input("Enter a weight on Earth: "))

# Prompt the user for the planet name
planet = input("Enter a planet: ")

# Calculate the weight on the chosen planet
if planet in gravity_factors:
    planet_weight = round(earth_weight * gravity_factors[planet], 2)
    print(f"The equivalent weight on {planet}: {planet_weight}")
else:
    print("Unknown planet. Please enter a valid planet name with the first letter capitalized.")
