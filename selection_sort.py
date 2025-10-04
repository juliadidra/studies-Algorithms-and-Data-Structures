
#Example of selection sort algorithm

def searchMinorElement(arr):
    minor = arr[0] # get the first element
    minorIndex = 0 # initialize with the minor index, which is 0

    for i in range(1, len(arr)): # iterate trhough the array (starting from 1)
        if arr[i] < minor: # compares if the current element is less than the minor 

            minor = arr[i] # if the condition is true, the current element is the new minor
            minorIndex = i #update the minor index with the current index
    return minorIndex

def selectionSort(arr):
    newArr = []

    for i in range(len(arr)): # iterate through the array
        minor = searchMinorElement(arr) #find the minor element 
        newArr.append(arr.pop(minor)) # remove the minor element of the array and append it to the new array, the values will be added in ascending order
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))