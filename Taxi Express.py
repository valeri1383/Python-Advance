from collections import deque

customers = deque([int(x) for x in input().split(', ')])
taxis = [int(x) for x in input().split(', ')]
total_time = 0

while customers and taxis:
    first_customer = int(customers[0])
    last_taxi = int(taxis[-1])
    if last_taxi >= first_customer:
        total_time += first_customer
        customers.popleft()
        taxis.pop()

    else:
        taxis.pop()

if not customers:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
else:
    print(f'Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join([str(x) for x in customers])}')