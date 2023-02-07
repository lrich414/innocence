import random
target = random.randint(1,100)
playing = True
userInput = input ("Guess the magic number (between 1 and 100)")
if userInput == "q":
    playing = False
else:
    userInput = int (userInput)
while playing:
    if target == userInput:
        print ("You Win! the magic number is...")
        print (target)
        print ("You guessed the magic number in guesses")
    playing = False
    if target == userInput:
        print ("Would you like to play again? (y/n)")
    if userInput == "y":
        playing = True
    if userInput == "n":
        playing = False
    elif target < userInput:
        print ("The magic number is lower")
        if userInput == "q":
            playing = False
            print ("yeah you better run, you're such a loser, always giving up on everything, tell me does your mother know about what a loser you are, does she know she gave birth to a loser? I hope your mom dies, loser birther.")
    elif target > userInput:
        print ("The magic number is higher")
        if userInput == "q":
            playing = False
            print ("yeah you better run, you're such a loser, always giving up on everything, tell me does your mother know about what a loser you are, does she know she gave birth to a loser? I hope your mom dies, loser birther.")
        else:
            print ("Please enter a valid number")
    if playing == True:
        userInput = input ("Guess the magic number (between 1 and 100)")
        userInput = int(userInput)
