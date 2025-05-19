def get_first_element(lst):
    print("The first element of the list is", lst[0])

def get_lst():

    lst = []
    elem = input("Please enter and element of the list or press Enter to stop: ")

    while elem != "":
        lst.append(elem)
        elem = input("Please enter another element or press Enter to stop: ")

    return lst

def main():
    lst = get_lst()

    get_first_element(lst)

if __name__ == "__main__":
    main()