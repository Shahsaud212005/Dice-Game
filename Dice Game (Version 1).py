import random

# ● ┌ ─ ┐ │ └ ┘

dice_art = {
1: ("┌─────────┐",
    "│         │",
    "│    ●    │",
    "│         │",
    "└─────────┘"),
2: ("┌─────────┐",
    "│  ●      │",
    "│         │",
    "│      ●  │",
    "└─────────┘"),
3: ("┌─────────┐",
    "│  ●      │",
    "│    ●    │",
    "│      ●  │",
    "└─────────┘"),
4: ("┌─────────┐"
    "│  ●   ●  │"
    "│  ●   ●  │"
    "│         │"
    "└─────────┘"),
5: ("┌─────────┐",
    "│  ●   ●  │",
    "│    ●    │",
    "│  ●   ●  │",
    "└─────────┘"),
6: ("┌─────────┐",
    "│  ● ● ●  │",
    "│  ● ● ●  │",
    "│  ● ● ●  │",
    "└─────────┘")
}


dice = []
total = 0
rolls = int(input("how many time do you wanna dice: "))

for roll in range(rolls):
    dice.append(random.randint(1, 6))

# for r in range(rolls):
#     for l in dice_art.get(dice[r]):
#         print(l)

for h in range(5):
    for c in dice:
        print(dice_art.get(c)[h], end="")
    print()


for i in dice:
    total += i
print(total)


 