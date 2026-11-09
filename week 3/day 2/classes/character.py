class Character:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
    
    def attack_power(self):
        raise NotImplementedError('every Character must implement attack_power()')
    