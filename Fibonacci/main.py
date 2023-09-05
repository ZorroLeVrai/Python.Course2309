def fibo1(nb):
    if nb < 2:
        return nb
        
    nm2 = 0
    nm1 = 1
    for i in range(2, nb+1):
        result = nm2 + nm1
        nm2 = nm1
        nm1 = result
    
    return nm1


# def fibo2(nb):
    if nb < 2:
        return nb
        
    nm2 = 0
    nm1 = 1
    for i in range(2, nb+1):
        nm2, nm1 = nm1, nm2 + nm1
    
    return nm1

print(fibo1(4))
#print(fibo2(15))