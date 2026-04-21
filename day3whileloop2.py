secret = 7
guess = 0

while guess != secret:
    guess = int(input("Enter your guess: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
print("correct! you got it!")            