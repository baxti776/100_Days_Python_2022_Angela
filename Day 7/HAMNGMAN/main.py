import random
from HANGMAN import stages
from HANGMAN_words import word_list

# word_list = ["box", "toy", "girl", "bitch"]
random_word = random.choice(word_list)
word_space_list = []
word_len = len(random_word)
lives = 6
end_of_game = False
space = "_"
print(f'{random_word} is your random_word')

# guess_letter = input("Enter your letter: ")
# guess_letter = guess_letter.lower()

for _ in range(word_len):
    word_space_list += space

while not end_of_game:
    guess_letter = input("Enter your letter: ").lower()

    for position in range(word_len):
        letter = random_word[position]

        if letter == guess_letter:
            word_space_list[position] = letter

    if guess_letter not in random_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    print(word_space_list)
    if space not in word_space_list:
        end_of_game = True
        print("You win ")
    print(stages[lives])
