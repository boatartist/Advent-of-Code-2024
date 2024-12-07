with open('input.txt', 'r') as f:
    data = f.read().strip()

num_rules = data.count('|')
rules = data.split('\n')[:num_rules]
rules = list(map(lambda x: x.split('|'), rules))
updates = data.split('\n')[num_rules+1:]
total = 0
for line in updates:
    line = line.split(',')
    correct = True
    for i in range(len(line)):
        num = line[i]
        before = line[:i]
        after = line[i+1:]
        for item in before:
            if [num, item] in rules:
                correct = False
                break
        if correct:
            for item in after:
                if [after, num] in rules:
                    correct = False
                    break
        if not correct:
            break
    if correct:
        index = len(line)//2
        total += int(line[index])

print(total)
