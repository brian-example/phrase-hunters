class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        print(" ".join(
            f"{letter.upper()}" 
            if letter in guesses else " " 
            if letter == " " else "_" 
            for letter in self.phrase
        ))

    def check_letter(self, guess):
        return guess in self.phrase

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True
