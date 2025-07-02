class Party:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def get_all_people(self):
        return self.people

    def get_people_count(self):
        return len(self.people)

party = Party()

while (line := input()) != "End":
    party.add_person(line)

print(f'Going: {", ".join(party.get_all_people())}')
print(f"Total: {party.get_people_count()}")