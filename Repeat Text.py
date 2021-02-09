try:
    text = input()
    sequence = int(input())
    text = text * sequence
    print(text)

except ValueError:
    print('Variable times must be an integer')



