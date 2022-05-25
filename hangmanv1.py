#Rodrigo Drumond Valente
#Hangman (Version 1)

chose_word = input("Type a word (to guess):").lower()
guess = []
result = False
plays = 0
chances = 0

while not result:
    iterable = 0
    if plays == 0:
        for i in range(len(chose_word)):
            guess.append("_")
        print(f"Word: {guess}\nChances: {chances}")
    letter = input("Type a letter:").lower()
    for i in range(len(chose_word)):
        if letter == chose_word[i]:
            position = i
            guess[position] = letter
            iterable += 1
    if iterable == 0:
        chances += 1
    if (set(guess) == set(chose_word)):
        result = True
        print(f"You guessed it right!")
    if chances == 6:
        result = True
        print(f"No more chances! Word: {chose_word}")
    print(f"Word: {guess}\nChances: {chances}")
    plays += 1




