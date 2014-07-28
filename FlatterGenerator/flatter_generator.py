import random

flatters = ["sexig beast", "fina fan"]
greetings = ["hej", "tjo"]

def flatter_generator():
    name = raw_input("What is your name?")

    random_flatter = flatters[random.randint(0, len(flatters) - 1)]
    random_greeting = greetings[random.randint(0, len(greetings) - 1)]

    return "%s %s %s" %(random_greeting, name, random_flatter)

print flatter_generator()


