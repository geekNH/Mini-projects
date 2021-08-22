import random

print("Hello, it is a guess a number game! \n A program chosed a number, and you need to guess it. \n")
top_digit = input("Enter the max range: ")
if top_digit.isdigit():
    top_digit = int(top_digit)
    if top_digit <= 0:
        print("Enter number higher than 0 ")
        quit()
else:
    print("Enter a number not a string ")
    quit()

random_num = random.randint(0,top_digit)
tries = 0

while True:
    tries += 1
    value = input("Make a guess: ")
    if value.isdigit():
        value = int(value)
    else:
        print("Type a number next time! ")
        continue
    if value == random_num:
        print("You guessed it correct! ")
        break
    elif value > random_num:
        print("Your guess is higher than the guessed number. Try again.")
    else:
        print("Your guess is lower than the guessed number. Try again.")
        
print("You got it in", tries , " guesses")
    
