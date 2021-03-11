import numpy as np
import math



'''Calculate one term of Taylor series'''
def taylor_item(x, n, last_item):
    q_n = (-1) * (x ** 2 / 4) / (n + 1) ** 2
    a = last_item * q_n
    return a


'''J_0(x_i) = f_i
Decomposition on Taylor series J(x) function
And solve It for each x_i value
'''
def func_Taylor_series(x_0, LEN):
    first = (-1) * (x_0 ** 2 / 4)
    ans = 0 + first
    cur_item = first
    for n in range(LEN):
        cur_item = taylor_item(x_0, n, cur_item)
        ans += cur_item
    return ans


'''Calculate divided difference between a and b'''
def calc_divided_diff(a, b, polynom_vals, X_arr):
    if a == b:
        return polynom_vals[b]  # value of J_0 at b point
    return (calc_divided_diff(a + 1, b, polynom_vals, X_arr) - calc_divided_diff(a, b - 1, polynom_vals, X_arr)) / (X_arr[b] - X_arr[a])


# Receive indices of X as x_0 and x_n accordingly
def brutal_force_div_diff(x_0, x_n, _X, f_vals):
    res = 0
    for j in range(x_0, x_n+1):
        denum = 1
        new_set = np.arange(x_0, x_n+1)
        new_set = np.delete(new_set, j-x_0)
        for k in new_set:
            denum *= (_X[j] - _X[k])
        res += f_vals[j] / denum
    return res


def x_prod_vector(x, _X):
    res = [1]
    cur_val = 1
    for x_i in _X[:-1]:  # нахер я это сделал?
        cur_val *= (x - x_i)
        res.append(cur_val)
    return np.array(res)


def newton_polynomial_values(_X, div_diff_vec):
    npv = []
    for x_i in _X:
        val = x_prod_vector(x_i, _X)
        val = np.dot(val, div_diff_vec)
        npv.append(val)
    return npv


def div_diff_vector(x_0, _X, f_vals):
    arr = []
    for x_i in range(x_0, len(_X)+1):
        val = brutal_force_div_diff(x_0, x_i, _X, f_vals)
        arr.append(val)
    return arr

