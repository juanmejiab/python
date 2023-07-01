if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    for x in range(n-1, 0, -1):
        if arr[x] == arr[x-1]:
            continue
        print(arr[x-1])
        break
