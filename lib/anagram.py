# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Store the word in lowercase for case-insensitive comparison

    def match(self, word_list):
        # Sort the original word for comparison
        sorted_word = sorted(self.word)

        # Return words that match when sorted
        return [word for word in word_list if sorted(word.lower()) == sorted_word and word.lower() != self.word]
