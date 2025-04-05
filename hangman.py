import random

# Word list for the game
word_list = ['python', 'hangman', 'developer', 'keyboard', 'computer', 'program']

# Choose a random word from the list
word = random.choice(word_list).lower()
guessed_letters = []
tries = 6

print("🎯 Welcome to Hangman!")
print("_ " * len(word))

while tries > 0:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Enter a single alphabetical letter.")
        continue

    if guess in guessed_letters:
        print("❗ You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess!")
    else:
        tries -= 1
        print(f"❌ Wrong guess! Tries left: {tries}")

    # Display current word progress
    display_word = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(display_word))

    # Win condition
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break
else:
    print("💀 Game Over! The word was:", word)
