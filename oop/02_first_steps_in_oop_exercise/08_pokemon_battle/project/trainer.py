from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: list[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        # for pok in self.pokemons:
        #     if pokemon_name == pok.name:
        #         self.pokemons.remove(pok)
        #         return f"You have released {pokemon_name}"
        #
        # return "Pokemon is not caught"

        # using next()
        pokemon_to_release = next((pok for pok in self.pokemons if pok.name == pokemon_name), None)
        if pokemon_to_release:
            self.pokemons.remove(pokemon_to_release)
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = (f"Pokemon Trainer {self.name}\n"
                  f"Pokemon count {len(self.pokemons)}\n")

        for pok in self.pokemons:
            result += f"- {pok.pokemon_details()}\n"

        return result.rstrip()

# Test code:

# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
