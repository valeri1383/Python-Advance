from collections import deque

name = input()
name_deque = deque()

while name != 'End':
    if name == 'Paid':
       while len(name_deque) > 0:
           print(name_deque.popleft())
    else:
        name_deque.append(name)

    name = input()

print(f"{len(name_deque)} people remaining.")