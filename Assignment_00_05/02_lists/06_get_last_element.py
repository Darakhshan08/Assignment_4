def get_last_element(lst):
    if len(lst) > 0:
        print("The last element is:", lst[-1])
    else:
        print("The list is empty. Please enter at least one element.")

def main():
    lst = []
    while True:
        elem = input("Enter an element (press Enter to stop): ")
        if elem == "":
            break
        lst.append(elem)

    get_last_element(lst)

if __name__ == '__main__':
    main()
