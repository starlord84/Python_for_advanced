'''Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной и побочной диагонали,
 при этом каждый элемент должен остаться в том же столбце
(то есть в каждом столбце нужно поменять местами элемент на главной диагонали и на побочной диагонали).'''
'''Sample Input 1:

3
1 2 3
4 5 6
7 8 9
Sample Output 1:

7 2 9 
4 5 6 
1 8 3 '''
n = int(input())
matr = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i == j) or (i == n - 1 - j):
            print(matr[n - 1 - i][j], end=' ')
        else:
            print(matr[i][j], end=' ')
    print()

