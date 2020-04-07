import json
import pokeSorter
import nationalDex

pokemonList = nationalDex.pokemonList

# open json
with open('some.json', 'r') as myfile:
    data = myfile.read()

myJson = json.loads(data)

poke = myJson["pokemon"]

with open("myPokemon.txt") as fp:
    line = fp.readline()
    while line:
        pokeSorter.sorter(line.strip())
        line = fp.readline()

        cardName = pokeSorter.cardName
        cardAmount = pokeSorter.cardAmount
        pokeJson = pokeSorter.pokeJson

        for i in range(len(pokemonList)):

            # if element is string and card contains element name, create directory
            if (isinstance(poke[i], str) and str(poke[i]).lower() in cardName.lower()):
                poke[i] = pokeJson
                print("created new directory with " + cardName)
                break
            # if card name is in directory, add quantities
            elif (cardName.lower() in str(poke[i]).lower()):
                poke[i][cardName] += cardAmount
                print("added " + str(cardAmount) + " cards to " + cardName)
                break
            # if the directory has been made but card hasn't been added
            elif str((pokemonList[i]).lower() in str(pokeJson).lower()) != "False":
                poke[i].update(pokeJson)
                print("added " + cardName + " to directory")
                break
            # else:

# update the actual json file
with open('some.json', 'w') as mynewfile:
    json.dump(myJson, mynewfile)
















#
