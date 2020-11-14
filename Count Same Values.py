numbers = list(float(x) for x in input().split(' '))
count = {}
for el in numbers:
    if el not in count:
        count[el] = 0
    count[el] += 1

for key, value in count.items():
    print(f'{key} - {value} times')