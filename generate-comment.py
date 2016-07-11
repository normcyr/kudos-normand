import random

# list of popular English adjectives
with open('dict/english-adjectives') as adjectivesfile:
    adjectives = adjectivesfile.read().split()
# list of popular English nouns
with open('dict/english-nouns') as nounssfile:
    nouns = nounssfile.read().split()

twowords = random.choice(adjectives) + " " + random.choice(nouns)
randomcomment = "What a " + twowords + " of an exercise dude!"

print(randomcomment)
