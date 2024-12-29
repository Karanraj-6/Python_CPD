n = int (input())

matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split())))
for j in range (n):
    for k in range(j,n):
        matrix[j][k] , matrix[k][j] = matrix[k][j],matrix[j][k]
for i in matrix:
    i.reverse()
print(matrix)