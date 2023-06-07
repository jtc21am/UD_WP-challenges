#Txt file header: AnimalName,AnimalType,NumLegs,Sound

#define an animal class with attributes, name, type, numlegs, sound

#define a monster class with attributes name, numlegs, head, body, and sound (both the name and the sound will come from the head and body animal A+B) numlegs = number of legs which match the head)

#define a function called createallmonsters -> take in # legs as arguement
# make animals based on number of legs input and save into a list, use an if statement to check the # of legs to ensure we only make animals with correct #, not all 
#make an empty list for monsters, 
# use nested loops to iterate over the animal list one for the head, one for the body, if the head =!body, add the joined new monster to the monster list
# return monster list

# define random monster
# call createallmonsters(input of # of legs), save in new random monster list
#if the list is empty, or len == 0, return Value Error
# return 1 random monster from this list -- use function random

import random

class Animal:
    def __init__(self, name, type, numLegs, sound):
        self.name = name
        self.type = type
        self.numLegs = numLegs
        self.sound = sound

# class Monster: # type hint the class
#     def __init__(self, head, body):
#         if head.numLegs != body.numLegs:
#             raise ValueError("The head and body have different number of legs")
#         self.name = head.name + body.name
#         self.numLegs = head.numLegs
#         self.head = head
#         self.body = body
#         self.sound = head.sound + body.sound

class Monster(Animal):
    def __init__(self, head, body):
        if head.numLegs != body.numLegs:
            raise ValueError("Head and body have different number of legs")
        super().__init__(head.name + body.name, head.type, head.numLegs, head.sound + body.sound)
        self.head = head
        self.body = body

# cat = Animal("cat", 'pet',4, "meow")
# dog = Animal("dog", 'pet',4, "woof")
# bird = Animal("bird", 'pet',2, "tweet")

# # Create a Monster object with the cat as the head and the bird as the body
# catBirdMonster = Monster(cat, bird)

# # Print out the attributes of the Monster object
# print("Name:", catBirdMonster.name)
# print("Number of legs:", catBirdMonster.numLegs)
# print("Sound:", catBirdMonster.sound)
# print("Head:", catBirdMonster.head.name)
# print("Body:", catBirdMonster.body.name)

#define a function called createallmonsters -> take in # legs as arguement
# make animals based on number of legs input and save into a list, use an if statement to check the # of legs to ensure we only make animals with correct #, not all 
#make an empty list for monsters, 
# use nested loops to iterate over the animal list one for the head, one for the body, if the head =!body, add the joined new monster to the monster list
# return monster list

def create_all_monsters(numLegs: int):
    animals_with_input_legs = []
    with open('animals.txt') as animalfile:
        next(animalfile)
        for line in animalfile:
            name, type, legs, sound = line.strip().split(',')
            legs = int(legs)
            if legs == numLegs:
                animals_with_input_legs.append(Animal(name, type, legs, sound))
    
    monsters_with_equal_legs = []
    for i, head in enumerate(animals_with_input_legs):
        for j, body in enumerate(animals_with_input_legs):
            if i != j and head.numLegs == body.numLegs:
                monsters_with_equal_legs.append(Monster(head,body))
    return monsters_with_equal_legs

# monster8 = create_all_monsters(8)
# for x in monster8:
#     print(x.name)


def get_random_monster(numLegs):
    random_monsters = create_all_monsters(numLegs)
    if len(random_monsters) == 0:
        raise ValueError(f'No monster with {numLegs} are found')
    return random.choice(random_monsters)

print(get_random_monster(8))
print(get_random_monster(4))


#  Monster(OctopusScorpion)
