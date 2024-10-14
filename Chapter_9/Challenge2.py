import random

Nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
Verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
Adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
Prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
Adverbs = ["curiously", "extravagantly", "tantalizing", "furiously", "sensuously"]

def make_poem():
    noun1 = random.choice(Nouns)
    noun2 = random.choice(Nouns)
    noun3 = random.choice(Nouns)
    while noun1 == noun2:
        noun2 = random.choice(Nouns)
    while noun1 == noun3 or noun2 == noun3:
        noun3 = random.choice(Nouns)

    verb1 = random.choice(Verbs)
    verb2 = random.choice(Verbs)
    verb3 = random.choice(Verbs)
    while verb1 == verb2:
        verb2 = random.choice(Verbs)
    while verb1 == verb3 or verb2 == verb3:
        verb3 = random.choice(Verbs)

    adjective1 = random.choice(Adjectives)
    adjective2 = random.choice(Adjectives)
    adjective3 = random.choice(Adjectives)
    while adjective1 == adjective2:
        adjective2 = random.choice(Adjectives)
    while adjective1 == adjective3 or adjective2 == adjective3:
        adjective3 = random.choice(Adjectives)

    prep1 = random.choice(Prepositions)
    prep2 = random.choice(Prepositions)
    while prep1 == prep2:
        prep2 = random.choice(Prepositions)
    
    adverb1 = random.choice(Adverbs)
    
    if "aeiou".find(adjective1[0]) != -1:
        article = "An"
    else:
        article = "A"

    poem = (
        f"{article} {adjective1} {noun1}\n\n"
        f"{article} {adjective1} {noun1} {verb1} {prep1} the {adjective1} {noun2}\n"
        f"{adverb1}, the {noun1} {verb2}\n"
        f"the {noun2} {verb3} {prep2} a {adjective3} {noun3}"
    )

    return poem
poem = make_poem()
print(poem)
