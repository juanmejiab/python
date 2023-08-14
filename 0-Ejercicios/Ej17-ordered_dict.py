from collections import OrderedDict

products = OrderedDict()


def append_items(key, value):
    if key in products:
        products[key] += int(value)
    else:
        products[key] = int(value)


for _ in range(int(input())):
    items = input().split()

    if len(items) > 2:
        key = f'{items[0]} {items[1]}'
        append_items(key, items[2])
    else:
        append_items(items[0], items[1])

for key, value in products.items():
    print(key, value)
