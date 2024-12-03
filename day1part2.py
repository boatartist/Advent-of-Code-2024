left = []
right = []
similarity_score = 0
with open('input.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        l, r = line.strip().split('   ')
        left.append(int(l))
        right.append(int(r))

left.sort()
right.sort()
for i in range(len(left)):
    similarity_score += left[i] * right.count(left[i])

print(similarity_score)
