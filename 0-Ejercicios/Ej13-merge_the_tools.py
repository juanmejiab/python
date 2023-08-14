import textwrap


def merge_the_tools(string, k):
    n = len(string)
    lst_merged = []
    if n % k == 0:
        for x in textwrap.wrap(string, k):
            string_merged = ""
            for y in range(len(x)):
                if x[y] not in string_merged:
                    string_merged += x[y]
            lst_merged.append(string_merged)
        print("\n".join(lst_merged))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
