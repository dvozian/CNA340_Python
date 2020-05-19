P = int(input())
R = int(input())
T = int(input())

interest = P*(1 + (R / 100)**T)
print('Compound interest is %.2f'%interest)
