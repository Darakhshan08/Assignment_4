MAX_LENGTH = 3  

def shorten(lst):
 
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()  
        print("Removed:", removed)

def get_lst():
   
    lst = []
    while True:
        elem = input("Enter an element (press Enter to stop): ")
        if elem == "":
            break
        lst.append(elem)
    return lst

def main():
    lst = get_lst()
    shorten(lst)


if __name__ == '__main__':
    main()
