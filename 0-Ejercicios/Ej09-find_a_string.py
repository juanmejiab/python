def count_substring(string, sub_string):
    count = 0
    for x in range(len(string)):
        for y in range(len(sub_string)):
            if x < len(string) and string[x] == sub_string[y]:
                x += 1
                if y == len(sub_string)-1:
                    count += 1
                continue
            break
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
