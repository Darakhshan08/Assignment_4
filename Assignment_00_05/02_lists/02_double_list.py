def main():
    numbers = [1, 2, 3, 4]

    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2

    print(f"Doubled list {numbers}")


if __name__ == "__main__":
    main()