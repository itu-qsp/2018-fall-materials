import re
import random
import eliza_language as lang


def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in lang.REFLECTIONS:
            tokens[i] = lang.REFLECTIONS[token]
    return ' '.join(tokens)


def analyze(statement):
    for pattern, responses in lang.PSYCHOBABBLE:
        match = re.match(pattern, statement.rstrip(".!"))
        if match:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])


def talk_to_me():
    print("I keep telling you I'm not a real therapist!")

    while True:
        statement = input("> ")
        print(analyze(statement))

        if statement == "Stop it! I have had enough!":
            break


if __name__ == "__main__":
    talk_to_me()
    
# Eliza gets her answers from the file eliza_language.py
#     [r'quit',
#     ["Thank you for talking with me.",
#      "Good-bye.",
#      "Thank you, that will be $150.  Have a good day!"]],