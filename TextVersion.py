import time


class Player:
    base_name = "Kamenshik"

    def __init__(self):
        self._money = 0
        self.PC = PC()
        #TODO: Hunger

    def work(self):
        print("Choose work type(plz print number):")
        print("1) PC Freelance")
        print("2) Street cleaner")
        while True:
            try:
                command = int(input())
                if command == 1:
                    time.sleep(0.5)
                    self._money += 1
                elif command == 2:
                    time.sleep(0.1)
                    self._money += (2**(self.PC.strength**0.5)) if self.PC.strength == 0 else 0
                else:
                    print("No")
                #TODO: Hack Pentagon
                break
            except ValueError:
                print("NAN")

    def play_game(self):
        print("U r gamer")
        print("U shud print commands")
        while True:
            print("print:", end=" ")
            command = input().lower()
            if command == "help":
                print("Available commands:")
                print("\t1) Info")
                print("\t2) Work")
                print("\t3) Upgrade PC")
                print("\t4) Exit")
            elif command == "info" or command == "1":
                print(f"Name = {self.base_name}")
                print(f"Money = {self._money}")
                print(f"PC = {self.PC.tiers[self.PC.tier]}")
            elif command == "upgrade pc" or command == "2":
                self._money -= self.PC.upgrade(self._money)
            elif command == "work" or command == "3":
                self.work()
            elif command == "exit" or command == "4":
                print("glhf")
                break
            else:
                print("Wrong command")


class PC:
    tiers = {
        0: "not PC", 1: "Potato Pc", 2: "Bad Pc", 3: "Not Bad PC",
        4: "PC", 5: "Gut PC", 6: "Quantum Pc", 7: "Black PC"
            }
    tier_price = {1: 1, 2: 4, 3: 16, 4: 64, 5: 256, 6: 1024, 7: 4096}

    def __init__(self):
        self.tier = 0
        if self.tier <= 0:
            self.strength = 0
        else:
            self.strength = 3 ** self.tier

    def upgrade(self, my_money):
        if my_money < self.tier_price[self.tier+1]:
            print("Not enought money")
            return 0
        elif self.tier >= 7:
            print("U have max tier")
            return 0
        self.tier += 1
        return self.tier_price[self.tier]


Sanya = Player()
Sanya.play_game()
