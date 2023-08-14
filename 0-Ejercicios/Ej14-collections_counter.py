from collections import Counter

if __name__ == '__main__':
    shoes = int(input())
    shoes_size = Counter(map(int, input().split()))
    customers = int(input())
    money = 0

    for _ in range(customers):
        shoe_price = list(map(int, input().split()))
        if shoes_size[shoe_price[0]] > 0:
            shoes_size[shoe_price[0]] -= 1
            money += shoe_price[1]

    print(money)
