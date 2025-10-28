class Player:

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict = {}
        self.guild: str = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost) -> str:
        if skill_name not in self.skills.keys():
            self.skills[skill_name] = mana_cost
            return (f"Skill {skill_name} added "
                    f"to the collection of the player {self.name}")
        return "Skill already added"

    def player_info(self) -> str:
        skills_details = "\n".join([f"==={skill} - {mana}" for skill, mana in self.skills.items()])
        return (f"Name: {self.name}\n"
                f"Guild: {self.guild}\n"
                f"HP: {self.hp}\n"
                f"MP: {self.mp}\n"
                f"{skills_details}")

    def change_guild(self, new_guild: str) -> None:
        self.guild = new_guild
