array = [10,2,6,3,8,5,9]

def bubbleSort(input):
    n = len(input) #number of elements in array
    for i in range(n):
        for j in range(0,n-i-1):
            if input[j] > input[j+1]:
                input[j], input[j+1] = input[j+1],input[j]

if __name__ == "__main__":
  bubbleSort(array)
  print("Sorted array is:")
  for i in range(len(array)):
      print("%d" % array[i], end=" ")