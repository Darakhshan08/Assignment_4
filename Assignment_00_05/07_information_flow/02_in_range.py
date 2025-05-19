def in_range(n, low, high):

    if n >= low and n <= high:
        return True
    return False

def main():
    
    n = int(input("Enter a number (n): "))
    low = int(input("Enter the lower bound (low): "))
    high = int(input("Enter the upper bound (high): "))

    result = in_range(n, low, high)
    print(result)

if __name__ == '__main__':
    main()
