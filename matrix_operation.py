def matrixInput(row, column):
    matrix = []
    for i in range(row):
        lit = []
        for j in range(column):
            num = int(input('Enter the element of the matrix: '))
            lit.append(num)
        matrix.append(lit)
    return matrix


def addMatrix(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result


print('Enter the first matrix: ')
matrix1 = matrixInput(2, 3)

print('Enter the second matrix: ')
matrix2 = matrixInput(2, 3)


resultant_matrix = addMatrix(matrix1, matrix2)
# print(addMatrix(matrix1, matrix2))

with open('output.txt', 'w') as fp:
    fp.write('The resultant sum is: \n')
    for row in resultant_matrix:
        fp.write(' '.join(map(str, row)) + '\n')
