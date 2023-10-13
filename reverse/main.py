amount = int(input())

numbers = []

for i in range(amount):
    numbers.append(input())


for i in range(amount):
    print(numbers[amount-i-1])