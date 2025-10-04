def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo] # store all elements less than or equal to pivot
        maiores = [i for i in array[1:] if i > pivo] # store all elements greater than pivot
        return quicksort(menores) + [pivo] + quicksort(maiores) # recursively apply quicksort to menores and maiores, and then concatenate the results
    
print(quicksort([10, 5, 2, 3]))