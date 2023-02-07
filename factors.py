userInput = int(input("ENTER A NUMBER"))
def numFactors(n):
    numbers = range(1,n+1)
    list = []
    for num in numbers:
        if userInput % num == 0:
            list.append(num)
    return list
def numThreeFive(n):
    if userInput % 3 == 0:
        threeFive = True
    if userInput % 5 == 0:
        threeFive = True
    else:
        threeFive = False
    return threeFive
def numFib(n):
    n1 = 0
    n2 = 1
    n3 = (n1 + n2)



print(f"The factors of {userInput} are {numFactors(userInput)}")
print (f"(t/f) {userInput} is divisible by 3 or 5?")
print(numThreeFive(userInput))
