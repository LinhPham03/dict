list = input('Nhập 1 list số: ')
order = []
for i in list:
    if i not in order:
        order.append(i)
order.sort()
print(order)
print("Hai số lớn nhất trong dãy là: ",order[-2], "và", order[-1])