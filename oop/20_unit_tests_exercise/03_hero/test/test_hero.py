import unittest
from project.hero import Hero

class HeroTests(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Gosho Geroia", 12, 90, 10)

    def test_initialization(self):
        self.assertEqual(self.hero.username, "Gosho Geroia")
        self.assertEqual(self.hero.level, 12)
        self.assertEqual(self.hero.health, 90)
        self.assertEqual(self.hero.damage, 10)

    # test battle win (happy path)
    def test_battle_win(self):
        enemy_hero = Hero("Rado Zliq", 10, 80, 7)

        self.assertEqual(self.hero.battle(enemy_hero), "You win")

    # test fight yourself
    def test_battle_with_yourself_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    # test health at 0
    def test_battle_my_health_at_zero_raises(self):
        enemy_hero = Hero("Rado Zliq", 10, 80, 90)

        self.hero.battle(enemy_hero)

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    # test enemy health at 0
    def test_battle_enemy_health_at_0_raises(self):
        enemy_hero = Hero("Rado Zliq", 10, 80, 5)

        self.hero.battle(enemy_hero)

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)

        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(ex.exception))

    # test battle draw (happy path)
    def test_battle_draw(self):
        enemy_hero = Hero("Rado Zliq", 12, 90, 10)

        self.assertEqual(self.hero.battle(enemy_hero), "Draw")

    # test you lose (happy path)
    def test_hero_loses(self):
        enemy_hero = Hero("Rado Zliq", 15, 150, 10)

        self.assertEqual(self.hero.battle(enemy_hero), "You lose")

    # test the state of the hero after the battle
    def test_hero_state_after_battle(self):
        enemy_hero = Hero("Rado Zliq", 10, 80, 7)
        self.hero.battle(enemy_hero)
        self.assertEqual(self.hero.level, 13)
        self.assertEqual(self.hero.health, 25)
        self.assertEqual(self.hero.damage, 15)

    # test the state of the enemy after the battle
    def test_enemy_hero_state_after_battle(self):
        enemy_hero = Hero("Rado Zliq", 10, 130, 10)
        self.hero.battle(enemy_hero)
        self.assertEqual(enemy_hero.level, 11)
        self.assertEqual(enemy_hero.health, 15)
        self.assertEqual(enemy_hero.damage, 15)

    # test str method (happy path)
    def test_str(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        self.assertEqual(str(self.hero), expected)

if __name__ == "__main__":
 unittest.main()