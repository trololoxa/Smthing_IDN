import time
from TextVersionPackage.PC import PC


#TODO: Day-Night cycle
class Player:
    #TODO: Gimme name
    #TODO: Save-Load :Test and polishing
    base_name = "Kamenshik"

    def __init__(self, is_load=False, money=0, pc_tier=0, file_name='Placeholder.save'):
        self._money = money
        self.PC = PC(pc_tier)
        self.file_name = file_name
        #TODO: Hunger
        #TODO: Sad
        #TODO: crminal

    def work(self):
        print("Choose work type(plz print number):")
        print("1) PC Freelance")
        #TODO: Skill lvl
        print("2) Street cleaner")
        #TODO: Car cleaner
        while True:
            try:
                command = int(input())
                if command == 2:
                    time.sleep(0.5)
                    self._money += 1
                elif command == 1:
                    time.sleep(0.1)
                    #TODO: Change Formula
                    self._money += round((1.75**(self.PC.strength**0.5)) if self.PC.strength > 0 else 0)
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
            if command == "help" or command == "0":
                print("Available commands:")
                print("\t0) Help")
                print("\t1) Info")
                print("\t2) Work")
                print("\t3) Upgrade PC")
                print("\t4) Exit")
            elif command == "info" or command == "1":
                print(f"Name = {self.base_name}")
                print(f"Money = {self._money}")
                print(f"PC = {self.PC.tiers[self.PC.tier]}")
            elif command == "work" or command == "2":
                self.work()
            elif command == "upgrade pc" or command == "3":
                self._money -= self.PC.upgrade(self._money)
            elif command == "exit" or command == "4":
                print("glhf")
                break
            else:
                print("Wrong command")
        return [self.file_name, self._money, self.PC.tier]
