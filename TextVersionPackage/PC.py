class PC:
    tiers = {
        0: "not PC", 1: "Potato Pc", 2: "Bad Pc", 3: "Not Bad PC",
        4: "PC", 5: "Gut PC", 6: "Quantum Pc", 7: "Black PC"
            }
    tier_price = {1: 1, 2: 4, 3: 16, 4: 64, 5: 256, 6: 1024, 7: 4096}

    def __init__(self, tier):
        self.tier = tier
        self.strength = (3 ** self.tier) if self.tier > 0 else 0

    def upgrade(self, my_money):
        if self.tier >= 7:
            print("U have max tier")
            return 0
        elif my_money < self.tier_price[self.tier+1]:
            print("Not enough money")
            print("U need " + str(self.tier_price[self.tier+1] - my_money) + " more money")
            return 0
        self.tier += 1
        print("Ur PC upgraded to " + self.tiers[self.tier])
        self.strength = 3 ** self.tier
        return self.tier_price[self.tier]
