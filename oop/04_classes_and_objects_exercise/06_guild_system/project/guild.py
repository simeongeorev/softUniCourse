from project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players: list[Player] = []

    def assign_player(self, player: Player) -> str:
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.change_guild(self.name)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        current_player = next((player for player in self.players if player.name == player_name), None)
        if current_player:
            self.players.remove(current_player)
            current_player.change_guild("Unaffiliated")
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players_info = "\n".join([player.player_info() for player in self.players])
        return (f"Guild: {self.name}\n"
                f"{players_info}")

# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
