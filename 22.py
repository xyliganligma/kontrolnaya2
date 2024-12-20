from random import *
from heapq import nlargest
n=int(input('n='))
m=int(input('m='))
matr=[[randint(-10,10) for j in range(m)] for i in range(n)]
print('Current matrix:')
print(matr)
niggative_count=sum(len([x for x in matr[i] if x<0]) for i in range(len(matr)))
print('The amount of negative quantities:')
print(niggative_count)
niggative_matr=[]
for row in matr:
    for element in row:
        if element <0:
            niggative_matr.append(element)
nigga=int(input('Input the quantity of maximal niggative numbers:'))
negga=nlargest(nigga,niggative_matr)
print('New matrixes:')
print(niggative_matr, negga)
print('I dont know why but i cant use Russian langiage here. I wanted to say that I didnt understand the task well so I hope the code is correct')


