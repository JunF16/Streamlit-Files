import random

# Randomly generate a funny short story
subjects = ["The cat", "A robot", "An alien", "My grandma", "A ninja", "The teacher"]
verbs = ["found", "lost", "ate", "destroyed", "invented", "painted"]
objects = ["a time machine", "a secret recipe", "an ancient map", "a flying car", "a mysterious gadget", "a magic wand"]
places = ["in the backyard", "on the moon", "under the bed", "at the museum", "inside a volcano", "in the attic"]

def generate_story():
    story = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)} {random.choice(places)}."
    return story