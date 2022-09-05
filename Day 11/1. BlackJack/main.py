import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = random.choices(cards, k=2)
computer_cards = random.choices(cards, k=2)
user_score = 0
computer_score = 0
for card in user_cards:
    user_score += card

for card in computer_cards:
    computer_score += card
print(f"User Score: {user_score}, User cards: {user_cards}")
print(f"Computer Score: {computer_score}, Computer cards: {computer_cards}")

if user_score == 21:
    print("You win. BlackJack")
elif computer_score == 21:
    print("You lose. Computer has BlackJack ")
elif user_score > 21:
    for card in user_cards:
        if card == 11:
            card = 1
            if user_score > 21:
                print("You lose")

else:
    another_card = input("Do u want to get another card?")
    if another_card == 'y':
        user_cards.append(random.choice(cards))
        user_score = 0
        for card in user_cards:
            user_score += card
        print(f"User score: {user_score}, User cards: {user_cards}")
    elif another_card == 'n' and computer_score < 17:
        computer_cards.append(random.choice(cards))
        print(f"Computer score: {computer_score}, Computer cards: {computer_cards}")
        if computer_score > 21:
            print("Computer win")
        elif user_score > computer_score:
            print("User win")
        elif user_score < computer_score:
            print("Computer win")
        elif user_score == computer_score:
            print("Draw")
