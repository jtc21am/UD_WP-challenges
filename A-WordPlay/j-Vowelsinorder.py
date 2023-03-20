'''For loops and if conditions
What are all of the words that have all 5 vowels, in alphabetical order?'''

# Open text file, "r" open for reading (default)
# The readlines() method returns a list containing each line in the file as a list item.
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters space is the default leading character to remove

# The time and space to remove the consonants is much lower than a loop using Bytes conversion. Bytes returns an bytes object and is the immutable version of bytearray.
# non_vowels = bytes(set(range(0x100)) - set(b'aeiou'))

# Use .decode method: To convert back to str by using decode i.e. b'aaeeiioo'.decode("ascii").

# Remove duplicate vowels and test if vowels are in alphabetical order

#  Move to next word if:
#    Use .find method --> A is not in first position (0)
#    if length of stripped word without consonants is less than or equal to 4 -- th

#  Otherwise remove duplicate vowels by .join and test if vowels are in alpha order

sowpods = open("sowpods.txt","r")
word_in_list = sowpods.readline().strip()

while(word_in_list):
  non_vowels = bytes(set(range(0x100)) - set(b'AEIOU'))
  stripped_word= word_in_list.encode('ascii', 'ignore').translate(None, non_vowels).decode("ascii")
 
  if stripped_word.find('A') !=0 or len(stripped_word) <= 4:
    word_in_list = sowpods.readline().strip()

  elif len(stripped_word) >= 5:
    stripped_word = "".join(dict.fromkeys(stripped_word))
    if stripped_word=='AEIOU':
          print(word_in_list)
    word_in_list = sowpods.readline().strip()
