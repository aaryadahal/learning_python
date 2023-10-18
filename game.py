import os #for clearing screen
import time #pausing after letters

text_1 = "Welcome! In this game you need two players, one to write a random number and another to guess it. The first person sets up things like how many guesses and which number. He/She can give hints if they want."
text_2 = "First person may proceed now."

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
        asking = input(">")
        hints.append(asking)

# Clear the screen (platform-specific command)
os.system('clear')

print("The game will start in 5 seconds. The second player should be ready.")
time.sleep(5)
os.system('clear')

text_3 = f"Welcome 2nd user. You now have to guess the number in {times} attempts. After {attempts_hint} attempts, you will receive a hint as per 1st user's stipulations. Best of luck!"
text_4 = f"Welcome 2nd user. You now have to guess the number in {times} attempts. You won't receive any hints as the 1st user denied it. Best of luck!"

if decision.upper() == "YES":
    text_4 = text_3
for letter in text_4:
    print(letter, end="", flush=True)
    time.sleep(0.01)
print()

for i in range(times):
    guess = int(input(f'Guess {i + 1}:'))
    if guess == secret_number:
        print("Congratulations, You guessed it!")
        break
    else:
        print(f"Woops, wrong answer! You have {times - i - 1} chances remaining.")
    if decision.upper() == "YES":
        if i + 1 < attempts_hint:
            continue
        if times - i - 1 == 0:
            break
        print("Hint:",end="")
        print(hints[attempts_hint - (i + 1)])
