#day 1
left = []
right = []
differences = []
with open('input.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        l, r = line.strip().split('   ')
        left.append(int(l))
        right.append(int(r))

left.sort()
right.sort()
for i in range(len(left)):
    differences.append(abs(left[i]-right[i]))

print(sum(differences))
