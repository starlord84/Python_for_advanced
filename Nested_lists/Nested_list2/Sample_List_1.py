'''На вход программе подается число nn. Напишите программу, которая создает и выводит построчно список, состоящий из nn списков 
[[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].'''
'''
Sample Input 1:

3
Sample Output 1:

[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
'''
n = int(input())
matrix = [[j for j in range(1, n + 1)] for i in range(1, n + 1)]
print(*matrix, sep='\n')