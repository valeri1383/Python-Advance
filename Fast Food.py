from collections import deque

quantity = int(input())
orders = deque(int(x) for x in input().split())
print(max(orders))
finished = True

while orders:
    current_order = orders.popleft()
    if quantity >= current_order:
        quantity -= current_order
    else:
        finished = False
        orders.appendleft(current_order)
        break

if finished:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(str(x) for x in orders)}")