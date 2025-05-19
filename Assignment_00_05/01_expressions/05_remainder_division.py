def main():
    try:
        dividend: int = int(input("Enter the number you want to divide:  "))
        divisor: int = int(input("Enter the number you want to divide by: "))

        quitent: int = dividend // divisor
        remainder: int = dividend % divisor

        print(f"The result of division is {quitent}, The remainder is {remainder}")

    except ZeroDivisionError:
        print("Division by zero not allowed")

if __name__ == "__main__":
    main()