if __name__ == '__main__':
    N = int(input())
    arr = []

    for _ in range(N):
        operation = input().split()
        if operation[0] == "insert":
            arr.insert(int(operation[1]), int(operation[2]))
        elif operation[0] == "print":
            print(arr)
        elif operation[0] == "remove":
            arr.remove(int(operation[1]))
        elif operation[0] == "append":
            arr.append(int(operation[1]))
        elif operation[0] == "sort":
            arr.sort()
        elif operation[0] == "pop":
            arr.pop()
        elif operation[0] == "reverse":
            arr.reverse()
