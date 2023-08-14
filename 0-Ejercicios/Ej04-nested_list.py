if __name__ == '__main__':
    name_score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_score_list.append([name, score])

    name_score_list.sort(key=lambda scores: scores[1])
    grade = list(set(map(lambda grades: grades[1], name_score_list)))
    grade.sort()

    names_ordered = [x for x in name_score_list if x[1] == grade[1]]
    names_ordered.sort(key=lambda value: value[0])
    for x in names_ordered:
        print(x[0])
