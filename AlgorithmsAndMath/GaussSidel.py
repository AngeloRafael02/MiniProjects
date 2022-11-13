#NOTE: only works on 3 x 3 Matrices
input = [[26,2,2,12.6],[3,27,1,-14.3],[2,3,17,6]]
guess= {"x":1,"y":1,"z":1}
loop = 7

def accuracy(old, new):
    return str(abs((new-old)/new)*100)

def GaussSeidel(matrix,guesses,iteration):
    # Has pitfalls: not guarantee accurate if input is not diagonally dominant
    while iteration > 0:
        x = ((matrix[0][-1])-(matrix[0][1]*guesses["y"])-(matrix[0][2]*guesses["z"]))/matrix[0][0]
        y = ((matrix[1][-1])-(matrix[1][0]*x)-(matrix[1][2]*guesses["z"]))/matrix[1][1]
        z = ((matrix[2][-1])-(matrix[2][0]*x)-(matrix[2][1]*y))/matrix[2][2]
        newGuess = {"x":x,"y":y,"z":z}
        print("x=" + str(x) + ", y=" + str(y) + ", z=" + str(z))
        print(accuracy(newGuess["x"],guesses["x"]) + " : " + accuracy(newGuess["y"],guesses["y"]) + " : " + accuracy(newGuess["z"],guesses["z"]) )
        if guesses["x"] == newGuess["x"] and guesses["y"] == newGuess["y"] and guesses["z"] == newGuess["z"]:
            return "Answer: x=" + str(x) + ", y=" + str(y) + ", z=" + str(z)
        else: 
            guesses = newGuess
        iteration -= 1

print(GaussSeidel(input,guess,loop))