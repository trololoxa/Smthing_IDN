from MainVersion.PC import PC


class Player:
    def __init__(self, money=0, pc_tier=0, file_name='Placeholder.save', hunger=100, game_time=None, cheerfulness=100):
        if game_time is None:
            game_time = {'days': 0, 'hours': 0}
        self._money = money
        self.PC = PC(pc_tier)
        self.file_name = file_name
        self._hunger = hunger
        self.game_time = game_time
        self._cheerfulness = cheerfulness
        self._sad = 0
        self._health = 100
        self._skill = 0
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
        elif worknum == 3:
            if not self.change_cheerfulness(-24):
                return 0
            self.add_time(9)
            self._money += 2
            self.change_hunger(-30)
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

    def upgrade_pc(self):
        self._money -= self.PC.upgrade(self._money)

    def sleep(self):
        self.add_time(8)
        self._cheerfulness = 100

    def eat(self):
        self.change_hunger(20)
        self._cheerfulness -= 10
