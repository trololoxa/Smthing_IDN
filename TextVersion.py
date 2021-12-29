# from TextVersionPackage.Save_Load import load


def main():
    print("Do u wanna:")
    print("1) Start new game")
    print("2) Load Game")

    while True:
        inp = int(input())
        if inp == 1:
            # load()
            break
        elif inp == 2:
            # load(False)
            break
        print("Wrong input")
        print("Plz, print number between 1 and 2")


if __name__ == "__main__":
    main()
