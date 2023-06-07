# Revisiting for loops, if conditions, and using lists as storage
# [ ] What are all of the words that have only “E”s for vowels and are at least 15 letters long?

with open('sowpods.txt') as sowpods:
    sowpods_words = (line.strip().upper() for line in sowpods)

    vowels = set("AEIOUY")

    u_only_words = [word.strip() for word in sowpods_words if len(word.strip()) >= 15 and (vowels & set(word.strip()) == {'E'})]
    print(u_only_words)
