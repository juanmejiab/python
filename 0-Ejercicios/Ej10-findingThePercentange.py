if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks = student_marks[query_name]

    average_score = 0
    for x in marks:
        average_score += x

    print("{:.2f}".format(average_score/3))
