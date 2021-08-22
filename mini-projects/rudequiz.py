name = input("Please enter your name: ")

print(f"Hello {name}, welcome to Mini-Quiz! \n There will be five multiple choice questions. \n You need to choose correct answer, type the chosen option and hit 'Enter' button. \n Good luck! \n ")

start = input("Do you want to start the game? ")

if start.lower() != "yes":
    print("Then why you run it at the first place, you son of a b*tch!? Have a great day!;)  ")
    quit()

correct = 0
wrong = 0

q1 = input("What is the capital of Hungary? \n a) Budapest \n b) London \n c) Riga \n")
if q1 == "a":
    print("Correct!\n")
    correct += 1
else:
    print("Wrong, you stupid peace of shit!\n")
    wrong += 1

q2 = input("What is the capital of New Zealand? \n a) Kingston \n b) Wellington \n c) Puddington \n")
if q2 == "b":
    print("Correct!\n")
    correct += 1
else:
    print("Wrong, you stupid peace of shit!\n")
    wrong += 1
q3 = input("What is the capital of Indonesia? \n a) KL \n b) Jakarta \n c) Almaty \n")
if q3 == "b":
    print("Correct!\n")
    correct += 1
else:
    print("Wrong, you stupid peace of shit!\n")
    wrong += 1


if correct>wrong:
    print(f"You passed the quiz with {correct} correct answers out of 3 \n")
    print("With " +str((correct / 3)*100)+ "% correct answers.")
else:
    print("You dumb peace of shit go fuck yourself")
