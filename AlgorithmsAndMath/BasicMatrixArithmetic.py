import numpy as np

Matrix1 = np.array([[1,2],
                    [3,4]])
Matrix2 = np.array([[5,6],
                    [7,8]])
result = [[0,0],[0,0]] #arrange according to desired matrix shape

def validate(m1,m2):
    return True if m1.shape == m2.shape else False

def matrixAddiction(m1,m2):
    if (validate(m1,m2)==True):
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                result[i][j] = m1[i][j] + m2[i][j]
        for r in result:
            print(r)
    else: print("Matrices do not have the same shape")
def matrixSubtraction(m1,m2):
    if (validate(m1,m2)==True):
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                result[i][j] = m1[i][j] - m2[i][j]
        for r in result:
            print(r)
    else: print("Matrices do not have the same shape")

print(validate(Matrix1,Matrix1))
matrixAddiction(Matrix1,Matrix2)
matrixSubtraction(Matrix1,Matrix2)
