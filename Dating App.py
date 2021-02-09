from collections import deque
males = [int(x) for x in input().split(' ')]
females = deque([int(x) for x in input().split(' ')])
matches = 0

while males and females:
    first_female = int(females[0])
    last_male = int(males[-1])

    if first_female <= 0 or last_male <= 0:
        if first_female <= 0:
            females.popleft()
        elif last_male <= 0:
            males.pop()
        continue

    if first_female % 25 == 0 or last_male % 25 == 0:
        if first_female % 25 == 0:
            females.popleft()
            females.popleft()
        elif last_male % 25 == 0:
            males.pop()
            males.pop()
        continue

    if first_female == last_male:
        matches += 1
        females.popleft()
        males.pop()
    elif first_female != last_male and len(females) > 0 and len(males) > 0:
        females.popleft()
        males.pop()
        males.append(last_male - 2)

print(f'Matches: {matches}')
if males:
    print(f"Males left: {', '.join([str(x) for x in males])}")
else:
    print('Males left: none')
if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")
