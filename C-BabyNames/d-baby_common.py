'''Nested for loops
What are all of the names that were top 40 baby names in both 1880 and 2020?'''

#open both files individually as read only
#(Create 2 sets so I can run the intersection method)
# create a new set and save the intersection of the two files  into the newly created set
# print new set 

# with open('baby_names_1880_short.txt') as baby_names_1880:
#     names_1880 = set(line.strip() for line in baby_names_1880.readlines())
# with open('baby_names_2020_short.txt') as baby_names_2020:
#     names_2020 = {(line.strip() for line in baby_names_2020.readlines()}
# common_names = (names_1880 & names_2020)
# print(list(common_names))


names1880 = open("baby_names_1880_short.txt","r")
names2020 = open("baby_names_2020_short.txt","r")

for name_1880 in names1880:
    for name_2020 in names2020:
        if name_1880 == name_2020:
            print(name_1880.strip())
    names2020.seek(0)
names1880.close()
names2020.close()

# # Create a String-->str
# print("\nTest 1")
# test1 = "()())()"
# print(f'Initially, the datatype of string : {(type(test1))}')
# print("Contents of string : " + test1)
# # Remove contents of duplicates, type still str
# print("\nAfter the conversion, the contents are : ", (set(test1)))
# print(f"The datatype of string : {(type(test1))}")


# # Create a String-->str
# print("\nTest 2")
# test2 = "()())()"
# print(f'Initially, the datatype of string : {(type(test2))}')
# print("Contents of string : " + test2)
# # Create set of original String 
# print("\nAfter the conversion, the contents are:")
# print({test2})
# print(f"The datatype of string : {type(test2)}")

# print("\nTest 3")
# test3 = "()())()"
# print(f'Initially, the datatype of string : {(type(test3))}')
# print("Contents of string : " + test3)

# # convert String to Set
# test3 = set(test3)
# print(f"\nAfter the conversion, the contents are  : {(type(test3))}")
# print("Contents of string : ", test3)