P_interest = int(input())
X_rub = int(input())
Y_kop = int(input())
K_years = int(input())

P_interest_new = (P_interest / 100)
list_sum = [(X_rub * 100) + Y_kop]

for i in range(K_years):
    list_sum.append(int(list_sum[-1] + list_sum[-1] * P_interest_new))

print(list_sum[-1] // 100, list_sum[-1] % 100)
