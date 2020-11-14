from collections import deque

start_quantity = int(input())
names = input()
people = deque()
while names != 'Start':
    people.append(names)

    names = input()

command = input()
while command != 'End':
    if command.isdigit() and len(people) > 0:
        litter_to_drink = int(command)
        if start_quantity >= litter_to_drink:
            start_quantity -= litter_to_drink
            print(f"{people.popleft()} got water" )
        else:
            print(f"{people.popleft()} must wait" )

    elif command.startswith('refill '):
        liters_refiled = int(command.split(' ')[-1])
        start_quantity += liters_refiled

    command = input()

print(f"{start_quantity} liters left")