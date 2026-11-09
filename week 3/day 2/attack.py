def attack(attacker, attacked):
    attacked.health -= attacker.attack_power()
    print (f'{attacker.name} hits {attacked.name} for {attacker.attack_power()}')