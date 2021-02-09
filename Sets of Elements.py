n, m = [int(x) for x in input().split(' ')]
n_set = set()
m_set = set()

for _ in range(n):
    current_number = int(input())
    n_set.add(current_number)

for _ in range(m):
    current_number = int(input())
    m_set.add(current_number)

unique_el = n_set.intersection(m_set)
print('\n'.join([str(x) for x in unique_el]))
