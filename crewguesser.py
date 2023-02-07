mcnaljCrewbies = ["Lucas", "Iona", "Titan"]
correct = []
guess = []
tries = 3
length = len(mcnaljCrewbies)
while len(mcnaljCrewbies) > 0 and tries > 0:
    userInput = input("Please enter the name of a crewbie:")
    if mcnaljCrewbies.count(userInput) > 0:
        print ("That crewbie is on the list!")
        mcnaljCrewbies.remove(userInput)
        correct.append(userInput)
    elif mcnaljCrewbies.count(userInput) == 0:
        tries = tries - 1
        print ("do better")
while len(mcnaljCrewbies) <= 0:
    print ("YOU WIN?")
    message = input("Want to play again?(y/n)")
    if message == 'y':
        tries = 3
        mcnaljCrewbies = correct
    elif message == 'n':
        exit
