def fat(x):
    if x == 1:
        return 1
    else:
        print(x)  
        return x * fat(x-1)

print(fat(5))  # Output: 120