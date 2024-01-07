import random

from phrasehunter.phrase import Phrase


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase("Just Google it"),
            Phrase("A bug or feature"),
            Phrase("Piece of cake"),
            Phrase("Perfect storm"),
            Phrase("Data is king")
        ]
        self.active_phrase = None
        self.guesses = [" "]
        self.tries = 5
        self.hearts = ["\U00002665 "] * self.tries

    def start(self):
        self.welcome()
        self.active_phrase = self.get_random_phrase()
        while self.missed < self.tries and not self.active_phrase.check_complete(self.guesses):
            self.active_phrase.display(self.guesses)
            print("\n")
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            if not self.active_phrase.check_letter(user_guess):
                self.missed += 1
                self.hearts[-self.missed] = "\U00002661 "
        self.game_over()

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        print(r"""

   ___ _                                             _                
  / _ \ |__  _ __ __ _ ___  ___    /\  /\_   _ _ __ | |_ ___ _ __ ___ 
 / /_)/ |_ \| '__/ _` / __|/ _ \  / /_/ / | | | '_ \| __/ _ \ '__/ __|
/ ___/| | | | | | (_| \__ \  __/ / __  /| |_| | | | | | | __/ |  \__ \
\/    |_| |_|_|  \__,_|___/\___| \/ /_/  \__,_|_| |_|\__\___|_|  |___/
""")
        print("Try to guess the phrase one letter at a time.")
        print(f"If you guess wrong {self.tries} times, you lose!\n")

    def get_guess(self):
        print(*self.hearts, sep=" ")
        guess = input("Enter a letter: ").lower()
        print("\n")
        if guess in self.guesses:
            print(f'You already guessed "{guess.upper()}".\n')
            return self.get_guess()
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            return self.get_guess()
        return guess

    def game_over(self):
        if self.missed == self.tries:
            print(*self.hearts, sep=" ")
            print("\nYou lost!\n")
            self.reset()

        elif self.active_phrase.check_complete(self.guesses):
            print(*self.hearts, sep=" ")
            self.active_phrase.display(self.guesses)
            print("\nYou won!\n")
            self.reset()

    def reset(self):
        play_again = input("Would you like to play again? (y/n) ").lower()
        if play_again == "y":
            self.missed = 0
            self.guesses = [" "]
            self.hearts = ["\U00002665 "] * self.tries
            self.start()
        else:
            print("\nThanks for playing!")
            exit()
