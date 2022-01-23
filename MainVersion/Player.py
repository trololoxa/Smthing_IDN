from MainVersion.PC import PC


# TODO: Day-Night cycle da
class Player:
    # TODO: Gimme name
    # TODO: Save-Load :Test and polishing
    base_name = "Kamenshik"

    def __init__(self, money=0, pc_tier=0, file_name='Placeholder.save', hunger=100, game_time=None, cheerfulness=100):
        if game_time is None:
            game_time = {'days': 0, 'hours': 0}
        self._money = money
        self.PC = PC(pc_tier)
        self.file_name = file_name
        self._hunger = hunger
        self.game_time = game_time
        self._cheerfulness = cheerfulness
        # TODO: Hunger da
        # TODO: Sad
        # TODO: crminal
        # TODO: Kalyannaya
        # TODO: health of hunger

    def return_save_data(self):
        return [self.file_name, self._money, self.PC.tier, self._hunger, self.game_time, self._cheerfulness]

    def work(self, worknum):
        # TODO: Skill lvl
        # TODO: Car cleaner
        # TODO: Random Dead inside
        #Street cleaner
        if worknum == 2:
            if not self.change_cheerfulness(-36):
                return 0
            self.add_time(12)
            self._money += 1
            self.change_hunger(-25)
        #PC Freelance
        elif worknum == 1:
            if self.PC.strength > 0:
                if not self.change_cheerfulness(-24):
                    return 0
                self.add_time(8)
                self.change_hunger(-8)
                # TODO: Change Formula
                self._money += round(1.625 ** (self.PC.strength ** 0.5))
        # TODO: Hack Pentagon

    def add_time(self, hours):
        self.game_time['hours'] += hours
        while self.game_time['hours'] >= 24:
            self.game_time['hours'] -= 24
            self.game_time['days'] += 1

    def change_hunger(self, hunger):
        self._hunger += hunger
        if self._hunger > 100:
            self._hunger = 100
        elif self._hunger <= 0:
            print('U ded inside')
            self._hunger = 0

    def change_cheerfulness(self, cheerfulness):
        if self._cheerfulness == 0:
            print("U rly want to sleep")
            return False
        if self._cheerfulness + cheerfulness <= 0:
            self._cheerfulness = 0
        self._cheerfulness += cheerfulness
        return True

    """def play_game(self):
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
                print("\t4) Sleep")
                print("\t5) Eat")
                print("\t6) Exit")
            elif command == "info" or command == "1":
                print(f"Name = {self.base_name}")
                print(f"Money = {self._money}")
                print(f"PC = {self.PC.tiers[self.PC.tier]}")
                print(f"hunger = {self._hunger}")
                print(f"Cheerfulness = {self._cheerfulness}")
                print(f"Time:\n\t Days = {self.game_time['days']}\n\t Hours = {self.game_time['hours']}")
            elif command == "work" or command == "2":
                self.work()
            elif command == "upgrade pc" or command == "3":
                self._money -= self.PC.upgrade(self._money)
            elif command == "sleep" or command == "4":
                self.add_time(8)
                self._cheerfulness = 100
                print('U slept in a wall')
            elif command == "eat" or command == "5":
                self.change_hunger(20)
                self._cheerfulness -= 10
                print('U ate 1 kilo of grass')
            elif command == "exit" or command == "6":
                print("glhf")
                break
            else:
                print("Wrong command")
        """
