if __name__ == '__main__':
    name_score_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_score_list.append([name, score])

    scores = []
    for x in name_score_list:
        scores.append(x[1])

    scores.sort()

    name_score_sorted = []
    x = 0
    while x < len(scores)-1:
        if scores[x] != scores[x+1]:
            y = scores[x+1]
            for names in name_score_list:
                if y == names[1]:
                    name_score_sorted.append(names)
            break
        else:
            x += 1
    name_score_sorted.sort()

    for x in name_score_sorted:
        print(x[0])
