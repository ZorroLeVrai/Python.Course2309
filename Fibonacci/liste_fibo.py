def create_fibo(n):
    if (n == 0):
        return [0]
    
    if (n == 1):
        return [0,1]
    
    result = [0,1]
    for i in range(2, n+1):
        result.append(result[i - 2] + result[i - 1])

    return result
    
print(create_fibo(4))