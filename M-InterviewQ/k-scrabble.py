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
    
    for letter in rack:
        rack_counts[letter] = rack_counts.get(letter,0) + 1
   
    valid_scrabble_words = []
    
    '''dictionary for the each sowpods word'''
    for word in word_list:
        word_counts = {}
       
        for letter in word:
            word_counts[letter] = word_counts.get(letter,0) + 1
        
        valid_word = True
        for letter in word_counts:
            if letter not in rack_counts or word_counts[letter] > rack_counts[letter]:
                valid_word = False
                break
    
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

rack = 'SPCQEIU'
print_words_with_scores(rack)











