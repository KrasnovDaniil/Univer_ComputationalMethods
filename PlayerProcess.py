import numpy as np
import matplotlib.pyplot as plt
import math
from decimal import Decimal


# Calculate one term of Taylor series
def next_item(x, n, last_item):
    q_n = (-1) * (x ** 2 / 4) / (n + 1) ** 2
    a = last_item * q_n
    return a


# J_0(x_i) = f_i
# Decomposition on Taylor series J(x) function
# And solve It for each x_i value

def func_Taylor_series(x_0):
    first = (x_0 ** 2 / 4)
    ans = 0 + first
    cur_item = first
    for n in range(LEN):  # LEN = len + 1?
        cur_item = next_item(x_0, n, cur_item)
        ans += cur_item
    return ans


# calculate separate difference and store it in F_sep_dif[last_index_of_calc]
def sep_dif(a, b):
    if F_sep_diff[a][b] != 0:
        print(f'its zero {F_sep_diff[a][b]}')
        return F_sep_diff[a][b]
    elif a == b:
        print(f'Primal {J_apr[a]}')
        F_sep_diff[a][b] = J_apr[a]
    else:
        print(f'calc normal')
        F_sep_diff[a][b] = (F_sep_diff[a][b-1] - F_sep_diff[a+1][b]) / (X[b]-X[a])
    print(F_sep_diff[a][b])
    return F_sep_diff[a][b]

sep_dif(0, 3)

a = Decimal('0')
b = 3
h = Decimal('0.3')
eps = 10 ** (-6)
n = 1
LEN = int((b - a) // h) + 1  # X points amount
alt_ans = 0
print(LEN)

X = np.arange(a, Decimal(b + h), step=h, dtype=Decimal)
F_sep_diff = np.zeros(shape=(LEN, LEN))  # F(a, b)



print(F_sep_dif)

print(X)
formul = lambda x, n: ((-1) ** n) * ((x ** 2 / 4) ** n) / (math.factorial(n) ** 2)
# first_item = formul(h, 0)
J_apr = np.zeros((LEN + 1))
J_apr[0] = 0

for x_i in X:
    J_apr[n] = func_Taylor_series(x_i)
    alt_ans = 0
    # print(x_i)
    for i in range(LEN):
        alt_ans += formul(float(x_i), i)
    print(f'For h = {float(x_i)}: alt_ans = {alt_ans}, calc = {J_apr[n]}')
    n += 1
print(J_apr)


