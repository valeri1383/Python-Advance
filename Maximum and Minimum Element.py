n = int(input())
stack = []

for x in range(n):
    query = input().split()
    if query[0] == '1':
        x = int(query[1])
        stack.append(x)

    elif query[0] == '2':
        if stack:
            stack.pop()

    elif query[0] == '3':
        if stack:
            print(max(stack))

    elif query[0] == '4':
        if stack:
            print(min(stack))
stack = [str(x) for x in reversed(stack)]
print(', '.join(stack))