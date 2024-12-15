import random

# Word bank from which a random word will be chosen
word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']
word = random.choice(word_bank)  # Choose a word randomly
guessedWord = ['_'] * len(word)  # Create a list to represent guessed letters
attempts = 10  # Number of allowed attempts

# Main game loop
while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord))
    guess = input('Guess a letter: ').lower()

    if guess in word:  # Check if the guessed letter is in the word
        for i in range(len(word)):
            if word[i] == guess:  # Update guessedWord with the correct guess
                guessedWord[i] = guess
        print('Great guess!')
    else:
        attempts -= 1  # Deduct an attempt for a wrong guess
        print('Wrong guess! Attempts left: ' + str(attempts))

    if '_' not in guessedWord:  # Check if the word has been fully guessed
        print('\nCongratulations!! You guessed the word: ' + word)
        break
else:
    print('\nYou\'ve run out of attempts! The word was: ' + word)