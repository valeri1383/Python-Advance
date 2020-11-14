sequence = [int(x) for x in input().split(' ')]
capacity = int(input())
rack_counter = 0
cloth_sum = 0

while sequence:
    current_cloth = sequence.pop()
    cloth_sum += current_cloth
    if cloth_sum == capacity:
        rack_counter += 1
        cloth_sum = 0
    elif cloth_sum > capacity:
        sequence.append(current_cloth)
        rack_counter += 1
        cloth_sum = 0
if cloth_sum:
    rack_counter += 1

print(rack_counter)


