def greet(name):
    
    print("Greetings " + name + "!")

def main():

    name: str = input("What's your name? ")
    greet(name)

if __name__ == "__main__":
    main()