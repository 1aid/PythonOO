"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, filename):
        self.words = []
        with open('words.txt') as file:
            for line in file:
                word = line.strip()
                if word:
                    self.words.append(word)

    def random_word(self):
        return random.choice(self.words)
