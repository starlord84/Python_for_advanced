'''Напишите программу, которая считывает натуральное число nn и выводит первые nn чисел последовательности Трибоначчи.'''
'''Sample Input 1:

10
Sample Output 1:

1 1 1 3 5 9 17 31 57 105'''
n = int(input())
f1, f2, f3 = 1, 1, 1
for i in range(n):
    print(f1, end=' ')
    f1, f2, f3 = f2, f3, f1+f2+f3