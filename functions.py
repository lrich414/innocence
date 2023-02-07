def teacherEmail (nameSur, nameFir):
    #this prints out a pps teacher email
    firstI = nameFir[0]
    lastI = nameSur[0:5]
    answer = (f"{lastI}{firstI}@portlandschools.org")
    return answer

email = teacherEmail ("mcnally", "jacob")
print (email)
email = teacherEmail ("natarajan", "priya")
print (email)
email = teacherEmail ("shibles", "scott")
print (email)

def tempConvert (temp1):
    result = ((temp1 * 9/5) + 32)
    return result

cf = tempConvert (21)
print (f"{cf} is 21 C in Farenheit")
