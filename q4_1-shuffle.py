import numpy as np
import matplotlib.pyplot as plt

def shuffle(deck, num_shuffles):
    num_cards = len(deck)
    for _ in range(num_shuffles):
        # Take a card from the *back* (makes more sense in memory)
        pop = deck.pop()
        deck.insert(np.random.randint(0, num_cards), pop)


num_cards = 3
num_decks_to_prepare = 10000
num_shuffles = 10

counts = {}

for _ in range(num_decks_to_prepare):
    deck = list(range(1, num_cards+1))  # 1 to num_cards
    shuffle(deck, num_shuffles)
    t = str(tuple(deck))

    if t in counts:
        counts[t] += 1
    else:
        counts[t] = 1

print(counts)

keys = list(counts.keys())
values = list(counts.values())

plt.bar(keys, values)
plt.xlabel('Decks')
plt.ylabel('Counts')
plt.show()
