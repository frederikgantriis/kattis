amount = int(input())

tmp = input().split()

numbers = []

count = 0

for i in range(amount):
    numbers.append(int(tmp[i]))

tmp2 = numbers

numbers.sort(reverse=True)

for i in range(amount):
    if numbers[i] != tmp2[i]:
        count += 1

print(count)




