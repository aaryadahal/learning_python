import os  # for clearing screen
import time  # pausing after letters

text_1 = "Welcome! In this game, you need two players. One sets a random number, and the other player tries to guess it. The first person sets things like how many guesses and which number. Hints can be provided."
text_2 = "The first player may proceed now."

for letter in text_1:
    print(letter, end="", flush=True)
    time.sleep(0.01)
print()

for letter in text_2:
    print(letter, end="", flush=True)
    time.sleep(0.01)
print()

secret_number = int(input("Enter a secret number:"))
times = int(input("How many chances do you want to provide?:"))
attempts_hint = 0
decision = input("Do you want to provide hints? (Yes/No)")

if decision.upper() == "YES":
    while True:
        attempts_hint = int(input("After how many attempts do you want to provide hints?:"))
        if attempts_hint < times:
            break

    hints = []
    print(f"Provide {times - attempts_hint} hints:")
    for i in range(times - attempts_hint):
        asking = input(f"Hint {i + 1}: ")
        hints.append(asking)

# Clear the screen (platform-specific command)
os.system('clear')

print("The game will start in 5 seconds. The second player should be ready.")
time.sleep(5)
os.system('clear')

text_3 = f"Welcome 2nd user. You now have to guess the number in {times} attempts. After {attempts_hint} attempts, you will receive a hint as per the 1st user's stipulations. Best of luck!"
text_4 = f"Welcome 2nd user. You now have to guess the number in {times} attempts. You won't receive any hints as the 1st user denied it. Best of luck!"

if decision.upper() == "YES":
    text_4 = text_3
for letter in text_4:
    print(letter, end="", flush=True)
    time.sleep(0.01)
print()

for i in range(times):
    if decision.upper() == "YES" and attempts_hint==0:
        print("Hint:", hints[i])
    elif decision.upper() == "YES" and i >= attempts_hint:
        print("Hint:", hints[i - attempts_hint])
    guess = int(input(f'Guess {i + 1}:'))
    if guess == secret_number:
        print("Congratulations, you guessed it!")
        break
    else:
        print(f"oops, wrong answer! You have {times - i - 1} chances remaining.")