#NOTE: only works on 3 x 3 Matrices
input = [[2,7,1,19],[4,1,-1,3],[1,-3,12,31]]
input.sort(reverse=True)
guess= {"x":1,"y":2,"z":3}
loop = 6

def diagonalSort(array,m=3,n=3):
    for i in range(m):
        sm = array[i][i]
        pos = i
        for j in range(i+1,n):
            if sm > array[j][j]:
                sm = array[j][j]
                pos = j
        array[i][i], array[pos][pos] = array[pos][pos], array[i][i]
    return array

def accuracy(old, new):
    return str(abs((new-old)/new)*100)

def GaussJacobi(matrix,guesses,iteration):
    while iteration > 0:
        x = (matrix[0][-1]*(matrix[0][0]**-1)) - ((matrix[0][1]*(matrix[0][0]**-1))*guesses["y"]) - ((matrix[0][2]*(matrix[0][0]**-1))*guesses["z"]) 
        y = (matrix[1][-1]*(matrix[1][1]**-1)) - ((matrix[1][0]*(matrix[1][1]**-1))*guesses["x"]) - ((matrix[1][2]*(matrix[1][1]**-1))*guesses["z"])
        z = (matrix[2][-1]*(matrix[2][2]**-1)) - ((matrix[2][0]*(matrix[2][2]**-1))*guesses["x"]) - ((matrix[2][1]*(matrix[2][2]**-1))*guesses["y"])
        newGuess = {"x":x,"y":y,"z":z}
        print("x=" + str(x) + ", y=" + str(y) + ", z=" + str(z))
        print(accuracy(newGuess["x"],guesses["x"]) + " : " + accuracy(newGuess["y"],guesses["y"]) + " : " + accuracy(newGuess["z"],guesses["z"]) )
        if guesses["x"] == newGuess["x"] and guesses["y"] == newGuess["y"] and guesses["z"] == newGuess["z"]:
            return "Answer: x=" + str(x) + ", y=" + str(y) + ", z=" + str(z)
        else: 
            guesses = newGuess
        iteration -= 1

print(diagonalSort(input))
print(GaussJacobi(diagonalSort(input),guess,loop))