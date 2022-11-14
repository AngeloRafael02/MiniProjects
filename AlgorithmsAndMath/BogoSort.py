import numpy as np
import collections as col
import random

def test(lst1, lst2):
    #Compares element order
    it = iter(lst1)
    try:
        i = next(it)
        for x in lst2:
            if x == i:
                i = next(it)
    except StopIteration:
        return True
    return False

def bogoSort(arr):
    array1 = np.array(arr)
    anotherList = list(range(len(array1)))
    random.shuffle(anotherList)
    newList = [array1[i] for i in anotherList]
    while True:
        random.shuffle(newList)
        if test(array1,newList)==False:
            print(newList,arr)
        else: 
            print(newList,arr)
            break

def bubbleSort(input):
    n = len(input) #number of elements in array
    for i in range(n):
        for j in range(0,n-i-1):
            if input[j] > input[j+1]:
                input[j], input[j+1] = input[j+1],input[j]    
    return input

input = [9,8,7,6,5,4,3,2,1]
bogoSort(input)
