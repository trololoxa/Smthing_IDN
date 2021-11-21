from TextVersionPackage.Player import Player

def load():
    print("Do u wanna:")
    print("1) Start new game")
    print("2) Load Game")

    while True:
        inp = int(input())
        if inp == 1:
            Sanya = Player()
            Sanya.play_game()
        elif inp == 2:
            #Load Game
            #Sanya.play_game()
            break
        print("Wrong input")
        print("Plz, print number between 1 and 2")

