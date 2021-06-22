n = int(input())
x = float(input())

i = 1
list_koeff = []

for i in range(1, n + 2):
    list_koeff.append(float(input()))

list_x = [x]
itog_list = [list_koeff[-1]]

for i in range(2, n + 2):
    itog_list.append(itog_list[-1] + list_koeff[-i] * list_x[-1])
    list_x.append(list_x[-1] * x)

print(itog_list[-1])
