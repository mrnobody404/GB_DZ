

list_price = [570.8, 46.51, 97,10.1,6,7,88.4]
new_list = []
for i in range(0, len(list_price)):
    cop = list_price[i] % 1 * 100
    rub = list_price[i] //1
    comp = f'{rub:02f} рублей {cop:02f} копеек'
    print(comp)
list_price.sort()
print(list_price)
list_price.sort(reverse=True)
print(list_price)
top5 = list_price[:5]
print(top5)

