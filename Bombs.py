from collections import deque

bomb_effect = deque([int(x) for x in input().split(', ')])
bomb_casing = [int(x) for x in input().split(', ')]
is_complete = False
bomb = {
    'Datura Bombs': {'value': 40, 'count': 0},
    'Cherry Bombs': {'value': 60, 'count': 0},
    'Smoke Decoy Bombs': {'value': 120, 'count': 0}
}

while bomb_casing or bomb_effect:
    if bomb['Datura Bombs']['count'] >= 3 and bomb['Cherry Bombs']['count'] >= 3 and bomb['Smoke Decoy Bombs']['count'] >= 3:
        is_complete = True
        break

    first_bomb = int(bomb_effect[0])
    last_casing = int(bomb_casing[-1])
    total = first_bomb + last_casing
    if total == 40:
        bomb['Datura Bombs']['count'] += 1
        bomb_effect.popleft()
        bomb_casing.pop()

    elif total == 60:
        bomb['Cherry Bombs']['count'] += 1
        bomb_effect.popleft()
        bomb_casing.pop()

    elif total == 120:
        bomb['Smoke Decoy Bombs']['count'] += 1
        bomb_effect.popleft()
        bomb_casing.pop()

    else:
        bomb_casing.pop()
        bomb_casing.append(last_casing - 5)

if is_complete:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effect:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effect])}")
else:
    print("Bomb Effects: empty")
if bomb_casing:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casing])}")
else:
    print("Bomb Casings: empty")

sorted_bomb = sorted(bomb.keys())

for x in sorted_bomb:
    print(f"{x}: {bomb[x]['count']}")


