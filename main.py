import json
from algorithms import *
import random

brain = []


def loadBrain():  # Loading my written Json file that stores the Chat Bot dictionary
    with open("data.json") as brain:
        data = json.load(brain)
        return data


def getUserInput():  # Get user's chat message
    user_input = input("Guest: ")
    return user_input


def tokenizeSentence(sentence):
    sentence = sentence.split(" ")
    words = [word.lower() for word in sentence]
    return words


def word_match_checker(dict, word):
    word = word.lower()  # convert to lower case so capitalizing isn't a step
    results = {w: lcs(w, word) for w in dict}
    results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1], reverse=True)}
    # print(results)
    commonality = list(results.items())[0][1]  # get LCS of assumed answer
    if commonality > len(word) / 2:  # if common letters is < half entry length
        return list(results.values())[1], list(results.keys())[0]
    else:
        return 0


def variation_tags(groups, target):
    result = {"score": 0, "statement": ""}
    for variation in groups:
        res = word_match_checker(variation["variations"], target)
        if res != 0:
            if result["score"] < res[0] and target.lower() in res[1].lower():
                result["score"] = res[0]
                result["statement"] = res[1]

    return result
    # print("----------------------------------")
    # return result


def findResponse(prompt):
    if prompt != "":
        for intent in brain:
            if prompt in intent["variations"]:
                return intent["responses"]
    else:
        return []


def varyResponse(responses):
    if len(responses) > 0:
        num = random.randint(0, len(responses) - 1)
        return responses[num]
    else:
        return "I do not understand that"


def main():
    # data to work with
    global brain
    brain = loadBrain()["data"]


if __name__ == "__main__":
    main()
    while True:
        message = getUserInput()
        responses = findResponse(variation_tags(brain, message)["statement"])
        response = varyResponse(responses)
        print("Bot: ", response)
