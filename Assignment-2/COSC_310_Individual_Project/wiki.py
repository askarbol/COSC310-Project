import wikipedia


# first pip install wikipedia
def wordSplit(userInput):
    phrase = userInput.lower().split()
    findPhrase = False
    if phrase[0] == 'explain' and phrase[1] == 'to' and phrase[2] == 'me':  # finds key phrase asked and then sends to another method
        findPhrase = True
        return findPhrase
    else:
        return findPhrase


def wikiLookup(userInput):
    phrase = userInput.lower().split()
    empty = ""
    for i in range(3, len(phrase)):
        empty = empty + phrase[i] + " "  # sees if user entered explain to me
    try:
        empty = wikipedia.summary(empty,sentences=1)  # checks wikipedia for the users input in conjuction with the key phrase.
        return empty
    except:
        empty = "Sorry, '" + empty + "' is not specific enough for a search. Please enter the name agian but be more " \
                                     "specific. "
        return empty


# this works if you run the file but when the chat bot runs it does not perform the wikipedia action i do not know why
#val = input("ask")
#print(wikiLookup(val))
