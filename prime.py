field = range (1,101)
def prime(n):
    status = True
    if n < 2:
        status = False
    else:
        for x in field:
            if n % x == 0:
                status = False
    return status
for n in range(2,n):
    if prime(n):
        if n == 97:
            print(n)
        else:
            print(n)
