from collections import deque

materials = [int(x) for x in input().split()]
magic_values = deque([int(x) for x in input().split()])
toys = {150: {'Doll': 0}, 250: {'Wooden train': 0}, 300: {'Teddy bear': 0}, 400: {'Bicycle': 0}}
toy_name = ''

while materials and magic_values:
    last_material = materials[-1]
    first_magic = magic_values[0]
    total = last_material * first_magic

    if last_material == 0 or first_magic == 0 or last_material and first_magic == 0:
        if last_material == 0:
            materials.pop()
        elif first_magic == 0:
            magic_values.popleft()

    elif total in toys:
        if total == 150:
            toy_name = 'Doll'
        elif total == 250:
            toy_name = 'Wooden train'
        elif total == 300:
            toy_name = 'Teddy bear'
        elif total == 400:
            toy_name = 'Bicycle'
        toys[total][toy_name] += 1
        materials.pop()
        magic_values.popleft()

    elif total < 0:
        total = last_material + first_magic
        materials.pop()
        magic_values.popleft()
        materials.append(total)

    elif total not in toys and total >= 0:
        magic_values.popleft()
        last_material += 15
        materials.pop()
        materials.append(last_material)

if toys[150]['Doll'] > 0 and toys[250]['Wooden train'] > 0 or toys[300]['Teddy bear'] and toys[400]['Bicycle']:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f'Materials left: {", ".join([str(x) for x in materials])}')
if magic_values:
    print(f'Materials left: {", ".join([str(x) for x in magic_values])}')

for value in toys:
    for k, v in toys[value].items():
        if v > 0:
            print(f'{k}: {v}')

