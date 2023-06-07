letter_scores = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10
}

def calculate_score(word):
    return sum(letter_scores[letter] for letter in word.lower())

def get_possible_words(rack, word_list):
    '''dictionary for the rack'''
    rack_counts = {}
    wildcards = []

    for letter in rack:
        if letter == '_':
            wildcards.append(letter)
        else:
            rack_counts[letter] = rack_counts.get(letter,0) + 1
    print('wildcard',wildcards)
    valid_scrabble_words = []
    
    '''dictionary for the each sowpods word'''
    for word in word_list:
        word_counts = {}
        remaining_wildcards = list(wildcards)

        for word in word_list:
            word_counts = {}
            used_wildcards = 0

            # Count occurrences of each letter in the word
            for letter in word:
                if letter in rack_counts and word_counts.get(letter, 0) < rack_counts[letter]:
                    word_counts[letter] = word_counts.get(letter, 0) + 1
                elif wildcards and used_wildcards < len(wildcards):
                    # Use a wildcard as the missing letter
                    word_counts[letter] = word_counts.get(letter, 0) + 1
                    used_wildcards += 1

            # Check if the word can be formed using the available letters and wildcards
        valid_word = all(word_counts.get(letter, 0) <= rack_counts.get(letter, 0) + wildcards.count('_') for letter in word_counts)

        if valid_word:
            valid_scrabble_words.append(word)

        return valid_scrabble_words


def print_words_with_scores(rack):

    valid_scrabble_words = get_possible_words(rack, word_list)
    sorted_words = sorted(valid_scrabble_words, key=lambda word: calculate_score(word), reverse=True)
    for word in sorted_words:
        score = calculate_score(word)
        print(f'{score} {word}')


with open('sowpods.txt', 'r') as file:
    word_list = [line.strip() for line in file]

rack = 'SPCQE_U'
print_words_with_scores(rack)






