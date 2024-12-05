with open('input.txt', 'r') as f:
    lines = f.readlines()
reports = []
for line in lines:
    line = list(map(int, line.split(' ')))
    index_to_remove = 0
    full = line[:]
    for index_to_remove in range(len(line)):
        is_safe = True
        line = full.copy()
        line.pop(index_to_remove)
        increasing = True if line[0] < line[1] else False
        for i in range(len(line)-1):
            if (line[i] < line[i+1] and not increasing) or (line[i] > line[i+1] and increasing) or not (1 <= abs(line[i]-line[i+1]) <= 3):
                is_safe = False
        if is_safe:
            break
    reports.append(is_safe)
    if not is_safe:
        print(full)

print(reports)
print(reports.count(True))
