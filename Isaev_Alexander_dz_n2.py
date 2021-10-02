#2 задание
i= 1
a = []
def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum
for i in range(1,1000,2):
    i = i**3
    if sum_of_digits(i) % 7==0:
        a.append(i)
print(a)