#[[2,7,1,19],[4,1,-1,3],[1,-3,12,31]]
input = [[2,7,1,19],[4,1,-1,3],[1,-3,12,31]]
input.sort(reverse=True)
guess= {"x":1,"y":2,"z":2}

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

def GaussJacobi(matrix,guesses):
    while True:
        x = (matrix[0][0]**-1) * (matrix[0][-1] - (matrix[0][1]*guesses["y"]) - (matrix[0][2]*guesses["z"]))
        y = (matrix[1][1]**-1) * (matrix[1][-1] - (matrix[1][0]*guesses["x"]) - (matrix[1][2]*guesses["z"]))
        z = (matrix[2][2]**-1) * (matrix[2][-1] - (matrix[2][0]*guesses["x"]) - (matrix[2][1]*guesses["y"]))
        newGuess = {"x":x,"y":y,"z":z}
        print("x=" + str(x) + ", y=" + str(y) + ", z=" + str(z))
        if guesses["x"] == newGuess["x"] and guesses["y"] == newGuess["y"] and guesses["z"] == newGuess["z"]:
            break
        else: 
            guesses = newGuess

print(diagonalSort(input))
print(GaussJacobi(diagonalSort(input),guess))