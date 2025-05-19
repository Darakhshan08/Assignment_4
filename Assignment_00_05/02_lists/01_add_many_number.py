def add_many_numbers(numbers):

    total = 0

    for num in numbers:
        total += num

    return total

def main():
    numbers = [1, 2, 3, 4, 5]

    result = add_many_numbers(numbers)

    print(f"The sum of the numbers is {result}")

if __name__ == "__main__":
    main()