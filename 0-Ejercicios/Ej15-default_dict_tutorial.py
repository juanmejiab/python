from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

d['group_a'].append([input() for _ in range(n)])
d['group_b'].append([input() for _ in range(m)])

letters_group_a = d['group_a'][0]
letters_group_b = d['group_b'][0]
indexes = []

for x in letters_group_b:
    for index, value in enumerate(letters_group_a):
        if value == x:
            indexes.append(str(index+1))
        elif x not in letters_group_a:
            indexes.append('-1')
            break
    print(' '.join(indexes))
    indexes.clear()
