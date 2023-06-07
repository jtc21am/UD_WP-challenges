import sys
import collections

LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2,
    'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1,
    'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def get_word_score(word):
    """Returns the Scrabble score of a word."""
    return sum(LETTER_VALUES.get(letter, 0) for letter in word)

def get_word_combinations(rack):
    """Returns all possible word combinations from a rack."""
    counter = collections.Counter(rack)
    words = set()
    with open('sowpods.txt') as f:
        for word in f:
            word = word.strip().lower()
            if len(word) <= len(rack) and set(word).issubset(set(rack)):
                word_counter = collections.Counter(word)
                if all(word_counter[letter] <= counter[letter] for letter in word_counter):
                    words.add(word)
    return words

def main():
    if len(sys.argv) != 2:
        print("Usage: python t-scrabble.py <RACK>")
        sys.exit(1)
    rack = sys.argv[1].lower()
    words = get_word_combinations(rack)
    words_scores = [(word, get_word_score(word)) for word in words]
    words_scores.sort(key=lambda x: x[1], reverse=True)
    for word, score in words_scores:
        print(f"{score} {word}")

if __name__ == '__main__':
    main()