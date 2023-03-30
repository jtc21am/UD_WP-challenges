'''Nested for loops
What are all of the names that were top 40 baby names in both 1880 and 2020?'''

#open both files individually as read only
#(Create 2 sets so I can run the intersection method)
# create a new set and save the intersection of the two files  into the newly created set
# print new set 

with open('baby_names_1880_short.txt') as baby_names_1880:
    names_1880 = {line.strip() for line in baby_names_1880.readlines()}


with open('baby_names_2020_short.txt') as baby_names_2020:
    names_2020 = set(line.strip() for line in baby_names_2020.readlines())


# common_names = (baby_names_1880 & baby_names_2020)
common_names = (names_1880 & names_2020)
print(list(common_names))