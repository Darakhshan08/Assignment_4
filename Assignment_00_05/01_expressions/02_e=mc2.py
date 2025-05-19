C: int = 3e8

def main():
    mass_in_kg = float(input("Enter mass in kg: "))

    energy_in_jouls = mass_in_kg * (C ** 2)

    print("\ne = m * C^2")
    print(f"m = {mass_in_kg}kg")
    print(f"C = {C}m/s")
    print(f"{energy_in_jouls} Joules of energy")

if __name__ == "__main__":
    main()