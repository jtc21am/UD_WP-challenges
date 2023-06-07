import random

class Animal:
    def __init__(self, name, type, numLegs, sound):
        self.name = name
        self.type = type
        self.numLegs = numLegs
        self.sound = sound

class Monster:
    def __init__(self, head, body):
        if head.numLegs != body.numLegs:
            raise ValueError("Head and body have different number of legs")
        self.name = head.name + body.name
        self.numLegs = head.numLegs
        self.head = head
        self.body = body
        self.sound = head.sound + body.sound

def createAllMonsters(numLegs):
    animals = []
    with open('animals.txt') as f:
        next(f)
        for line in f:
            name, type, legs, sound = line.strip().split(',')
            legs = int(legs)
            if legs == numLegs:
                animals.append(Animal(name, type, legs, sound))
    monsters = []
    for i, head in enumerate(animals):
        for j, body in enumerate(animals):
            if i != j and head.numLegs == body.numLegs:
                monsters.append(Monster(head, body))
    return monsters

def getRandomMonster(numLegs):
    monsters = createAllMonsters(numLegs)
    if len(monsters) == 0:
        raise ValueError("No monsters with %d legs found" % numLegs)
    return random.choice(monsters)


monsters = createAllMonsters(8)
print([monster.name for monster in monsters])
# Output: ['OctopusScorpion', 'ScorpionOctopus']
print()

monster = getRandomMonster(8)
print(monster.name)
# Output: either 'OctopusScorpion' or 'ScorpionOctopus'

