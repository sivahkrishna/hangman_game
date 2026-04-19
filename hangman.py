import random

word_list = ["python", "apple", "train", "chair", "cloud"]
word = random.choice(word_list)

guessed_letters = []
attempts = 6

display = ["_"] * len(word)
print("Welcome to Hangman Game!")

while attempts > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠️ Already guessed!")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("✅ Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        break

    else:
        print("❌ Wrong!")
        attempts -= 1


if "_" not in display:
    print("\n🎉 You Lost! Word is:", word)
else:
    print("\n💀 You Won! Word was:", word)