maximum = int( raw_input("What is the maximum number you want to set the bar at?)"))
minimum = int (input("Min"))
guess

def Guess():
    guess =( (maximum + minimum)/2)
    response = input("If your number is greater then - g, if less - l, if equals - e")

if response == "g":
    minimum = guess
    Guess():

elif response == "l":
    maximum = guess
    Guess():

else:
    print("Thats it!")


