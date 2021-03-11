from ComputationMethodsCourse.calculations.computations import func_Taylor_series, calc_divided_diff, \
    brutal_force_div_diff, x_prod_vector, newton_polynomial_values, div_diff_vector
from ComputationMethodsCourse.calculations.Diagnostics import time_check
import numpy as np
import math
import math
from decimal import Decimal
import time


a = Decimal(0)
b = Decimal(3)
h = Decimal('0.1')
eps = 10 ** (-6)
n = 1
LEN = int((b - a) // h) + 1
print(LEN)
arr = np.arange(a, b + h, step=h, dtype=float)
arr = np.round_(arr, 4)
print(arr)

formul = lambda x, n: ((-1) ** n) * ((x ** 2 / 4) ** n) / (math.factorial(n) ** 2)
approximated_by_taylor = np.zeros(LEN)


inner_points = np.zeros(len(arr)-1)
for i in range(1, len(arr)):
    inner_points[i-1] = (arr[i] + arr[i-1])/2
print(inner_points)


for j, x_i in enumerate(arr):
    alt_ans = 0
    for i in range(LEN):
        alt_ans += formul(x_i, i)
    approximated_by_taylor[j] = alt_ans

for x_i, val_i in zip(arr, approximated_by_taylor):
    print(f'For h = {x_i}: ans = {val_i}')


# Time to calculate divided differences
# x_0 = 0
# x_n = LEN-1
f_0_2 = calc_divided_diff(x_0, x_n, approximated_by_taylor, arr)
# print(f_0_2)
# f_brut = brutal_force_div_diff(x_0, x_n, arr, approximated_by_taylor)
# print(f_brut)
# print(round(f_0_2, 12) == round(f_brut, 12))

ddvec = div_diff_vector(0, arr, approximated_by_taylor)
print(f'divided differences coefs: {ddvec}')

newton_polynom_vals = newton_polynomial_values(inner_points, ddvec)

print(f'Newton\'s polynomial coefficients:')
for x_i, val_i in zip(arr, newton_polynom_vals):
    print(f'For h = {x_i}: ans = {round(val_i, 10)}')

approximated_by_taylor = np.array(approximated_by_taylor)
newton_polynom_vals = np.array(newton_polynom_vals)


measure_err = np.abs(approximated_by_taylor - newton_polynom_vals)
print(f'Max measurement error: {np.max(measure_err)}')

mean_measure_err = np.abs(approximated_by_taylor - newton_polynom_vals)
print(f'Mean measurement error: {np.mean(measure_err)}')

