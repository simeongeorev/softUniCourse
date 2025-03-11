deck = input().split()
shuffled_deck = []
holder_deck = deck
times_to_shuffle = int(input())

for _ in range(times_to_shuffle):
    shuffled_deck = []
    for i in range(1, int(len(deck) / 2)):
        shuffled_deck.append(holder_deck[i + int(len(holder_deck) / 2) - 1])
        shuffled_deck.append(holder_deck[i])

    holder_deck = shuffled_deck
    holder_deck.insert(0, deck[0])
    holder_deck.append(deck[-1])

print(shuffled_deck)