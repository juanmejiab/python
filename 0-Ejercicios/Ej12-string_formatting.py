def print_formatted(number):
    space = len(bin(number)[2:])
    [print(f'{num:>{space}} {oct(num)[2:]:>{space}} {(hex(num)[2:]).upper():>{space}} {bin(num)[2:]:>{space}} ')
     for num in range(1, number+1)]


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
