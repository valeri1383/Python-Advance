n = int(input())
parking = set()
for _ in range(n):
    token = input().split(', ')
    direction = token[0]
    number = token[1]

    if direction == 'IN':
        parking.add(number)
    else:
        parking.remove(number)

if parking:
    print('\n'.join([str(x) for x in parking]))
else:
    print('Parking Lot is Empty')