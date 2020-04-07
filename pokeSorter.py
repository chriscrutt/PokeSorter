import json

def sorter(card):

    # seperate first part with quantity
    aString = card[:4]
    bString = card[4:]

    # get amount in form of array
    cardAmountArray = [int(s) for s in aString.split() if s.isdigit()]

    # set amount from the amountArray
    global cardAmount
    cardAmount = cardAmountArray[0]

    # take out the number and space
    aStringNew = aString.replace(str(cardAmount) + " ", "")

    # put the string back together
    global cardName
    cardName = aStringNew + bString

    # create snippet and convert to json
    global pokeJson
    pokeJson = "{\"" + cardName + "\"" + ": " + str(cardAmount) + "}"

    pokeJson = json.loads(pokeJson)

    # print(pokeJson)

# sorter("1 Squirtle [XD]")
