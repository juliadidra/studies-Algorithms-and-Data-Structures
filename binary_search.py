def binary_search(list, item):
    low = 0
    high = len(list) - 1 ## last index

    while low <= high:
        mid = (low + high) // 2 ## value of mid index
        guess = list[mid] # the value at mid index

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1 
        else:
            low = mid + 1
    return None
    
my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))  # Output: 1