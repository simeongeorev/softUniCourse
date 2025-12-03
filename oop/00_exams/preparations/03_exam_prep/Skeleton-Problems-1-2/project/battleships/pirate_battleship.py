from project.battleships.base_battleship import BaseBattleship


class PirateBattleship(BaseBattleship):
    STARTING_AMMO = 80
    MIN_AMMO = 0
    AMMO_PER_ATTACK = 10

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, ammunition=self.STARTING_AMMO)

    def attack(self):
        self.ammunition -= self.AMMO_PER_ATTACK
        if self.ammunition < self.MIN_AMMO:
            self.ammunition = self.MIN_AMMO