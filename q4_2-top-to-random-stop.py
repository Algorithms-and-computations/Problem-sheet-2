import numpy as np
import matplotlib.pyplot as plt

def shuffle(deck):
    num_cards = len(deck)
    first = deck[0]
    num_shuffles = 0
    one_more_shuffle = False
    while True:
        # Take a card from the *back* (makes more sense in memory)
        pop = deck.pop()
        deck.insert(np.random.randint(0, num_cards), pop)
        num_shuffles += 1


        if one_more_shuffle:
            break

        if deck[-1] == first:
            # Have reached the last card.
            # Need to shuffle it, then have a perfect sample
            one_more_shuffle = True

    return num_shuffles


num_cards = 5
num_decks_to_prepare = 100000

counts = {}
total_shuffles = 0

shuffle_counts = []

for _ in range(num_decks_to_prepare):
    deck = list(range(1, num_cards+1))  # 1 to num_cards
    num_shuffles = shuffle(deck)
    shuffle_counts.append(num_shuffles)
    total_shuffles += num_shuffles
    t = str(tuple(deck))

    if t in counts:
        counts[t] += 1
    else:
        counts[t] = 1

avg_shuffle_per_deck = total_shuffles / num_decks_to_prepare
print("Average number of shuffles per deck = %d" % avg_shuffle_per_deck)
print(counts)

keys = list(counts.keys())
values = list(counts.values())

plt.bar(keys, values)
plt.xlabel('Decks')
plt.ylabel('Counts')
plt.show()


numbers_sorted = np.sort(np.array(shuffle_counts))
cdf = np.linspace(1/len(numbers_sorted), 1, len(numbers_sorted))
plt.plot(numbers_sorted, cdf)
plt.xlabel('n')
plt.title('F(n)')
plt.show()
