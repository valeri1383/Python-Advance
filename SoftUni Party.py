number_guest = int(input())
vip = set()
normal = set()
for _ in range(number_guest):
    reservation = input()
    if reservation[0].isdigit():
        vip.add(reservation)
    else:
        normal.add(reservation)

guest = input()
while guest != 'END':
    if guest in vip:
        vip.remove(guest)
    elif guest in normal:
        normal.remove(guest)

    guest = input()

guest_not_come = len(vip) + len(normal)
print(guest_not_come)

for person in sorted(vip):
    print(person)
for person in sorted(normal):
    print(person)