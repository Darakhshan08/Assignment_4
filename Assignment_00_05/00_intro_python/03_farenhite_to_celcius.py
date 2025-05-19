def main():
    farenhite = float(input("\033[1;3m Enter temprature in ferenhite: \033[0m"))

    celcius = (farenhite - 32) * 5.0/9.0

    print(f"Temprature : {farenhite}F = {celcius}C")

if __name__ == "__main__":
    main()