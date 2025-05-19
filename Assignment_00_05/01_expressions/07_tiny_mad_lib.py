SENTANCE_START: str = "Panaversity is fun. I learned to programm and used python to make my "

def main():
    adjective : str = input("Enter an adjective and press enter: ")
    noun : str = input("Enter a noun and press enter: ")
    verb : str = input("Entwer a verb and press enter: ") 

    print(SENTANCE_START + adjective + " " + noun + " " + verb + ".")

if __name__ == "__main__":
    main()