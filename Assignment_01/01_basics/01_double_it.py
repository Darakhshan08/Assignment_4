def main():
    
    user_input = int(input("Enter a number: "))

    curr_val = user_input * 2
    print(curr_val)

    while curr_val < 100:
        curr_val = curr_val *2
        print(curr_val)

    
if __name__ == "__main__":
    main()
    