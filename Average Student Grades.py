n = int(input())
score = {}
for _ in range(n):
    token = input().split(' ')
    name = token[0]
    grade = float(token[1])
    if name not in score:
        score[name] = []
    score[name].append(grade)


for name, grades in score.items():
    avg = sum(grades) / len(grades)
    mark_str = [f'{grade:.2f}' for grade in score[name]]
    print(f'{name} -> {" ".join(mark_str)} (avg: {avg:.2f})')
