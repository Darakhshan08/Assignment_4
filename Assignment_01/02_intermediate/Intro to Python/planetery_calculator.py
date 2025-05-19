"""
Planetary Weight Calculator

This program prompts the user for their weight on Earth and the name of a planet.
It then calculates and displays the equivalent weight on that planet.

Each planet has a unique gravitational constant (relative to Earth's gravity),
so the user's weight will vary depending on the planet chosen.

Assumptions:
- User will type the planet name correctly with the first letter capitalized.
- Only planets in the solar system (excluding Pluto) are considered.
"""

MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():

    earth_weight = float(input("Enter a weight on Earth: "))

    planet = input("Enter a planet: ")

    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    elif planet == "Neptune":
        gravity_constant = NEPTUNE_GRAVITY
    else:
        print("Unknown planet.")
        return

    planetary_weight = earth_weight * gravity_constant
    rounded_weight = round(planetary_weight, 2)

    print("The equivalent weight on " + planet + ": " + str(rounded_weight))

if __name__ == "__main__":
    main()
