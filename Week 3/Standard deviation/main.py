list_vvoda = []

while True:
    list_vvoda.append(int(input()))
    if list_vvoda[-1] == 0: break

list_sum = [0]
list_vvoda = list_vvoda[:-1]
for i in list_vvoda:
    list_sum.append(list_sum[-1] + i)
    
s = list_sum[-1] / len(list_vvoda)

list_enumerator = [0]

for i in list_vvoda:
    list_enumerator.append(list_enumerator[-1] + ((i - s) ** 2))

print((list_enumerator[-1] / (len(list_vvoda) - 1)) ** 0.5)
