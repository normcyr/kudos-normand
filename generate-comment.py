import random

# list of popular English adjectives
with open('dict/english-adjectives') as adjectivesfile:
    adjectives = adjectivesfile.read().split()
lengthofadjectivefile = len(adjectives)

# list of popular English nouns
with open('dict/english-nouns') as nounssfile:
    nouns = nounssfile.read().split()
lengthofnounsfile = len(nouns)

positionadj = random.randrange(0, lengthofadjectivefile)
anadjective = adjectives[positionadj]
positionnoun = random.randrange(0, lengthofnounsfile)
anoun = nouns[positionnoun]
twowords = anadjective + " " + anoun
randomcomment = "What a " + twowords + " of an exercise dude!"

print(randomcomment)
