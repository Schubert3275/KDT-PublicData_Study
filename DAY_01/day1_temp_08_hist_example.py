import random
import matplotlib.pyplot as plt

dice = []
for i in range(10):
    dice.append(random.randint(1, 6))
print(dice)

plt.hist(dice, bins=6)
plt.xticks([1, 2, 3, 4, 5, 6])
plt.show()
