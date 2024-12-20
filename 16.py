from random import *
n=int(input('n='))
m=int(input('m='))
matr=[[randint(-10,10) for j in range(m)] for i in range(n)]
print('Current matrix:')
print(matr)
for i in range(len(matr)):
    ma=max(matr[i])
    ma_i=matr[i].index(ma)
    matr[i].append(matr[i].pop(ma_i))
print('New matrix:')
print(matr)
