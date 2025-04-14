import random
import lines
import words

print(lines.heading)

chosen_word = random.choice(words.words)
print(chosen_word)
display = []

flag = True
lives = 6
life = 0

for i in range(len(chosen_word)):
    display += '_'

while flag:
    guess = input("Guess a letter\n").lower()

    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if guess == letter:
            display[i] = guess

    if guess not in chosen_word:
        print("Wrong guess :( You lose a life")
        print(lines.lines[life])
        lives -= 1
        life += 1

    if  lives == 0:
        print(f"The word is {chosen_word}")
        print("You lost the game. Try next time.")
        flag = False
        break


    if "_" not in display:
        print(f"The word is {chosen_word}")
        print("Congratulations! You win!")
        flag = False
        break

    s = ''.join(display)
    print(s)