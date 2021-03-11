from decimal import Decimal

a = Decimal('0')
b = Decimal('3')
h = Decimal('0.1')

res = (b-a)/h

res2 = Decimal.__truediv__((b-a), h)

print(int(res))
print(int(res2))