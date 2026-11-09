from classes.character import Character

class Mage(Character):
    def attack_power(self):
        return 10 if self.health <= 50 else 20