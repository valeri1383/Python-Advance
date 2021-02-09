text = {x: len(x) for x in input().split(', ')}

result = [f'{key} -> {value}'for key, value in text.items()]

print(', '.join(result))