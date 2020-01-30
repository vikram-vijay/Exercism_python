# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.letters_of_word = set(word)

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("Game Over!")
        if char in self.letters_of_word:
            self.letters_of_word.remove(char)
            if not self.letters_of_word:
                self.status = STATUS_WIN
        else:
            self.remaining_guesses += -1
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE

    def get_masked_word(self):
        return "".join("_" if letter in self.letters_of_word else letter for letter in self.word)

    def get_status(self):
        return self.status
