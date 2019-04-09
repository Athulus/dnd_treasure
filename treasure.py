import treasure_tables as tables
import random
import re
import operator

def parseCoin(expression: str):
    quantity, *e = re.split("[dx]",expression)
    quantity = int(quantity)
    diesize = 0
    multiplier = 1
    if len(e) >= 1:
        diesize = int(e[0])
    if len(e) >=2:
        multiplier = int(e[1])
    sum = 0
    for i in range(quantity):
        sum += random.randrange(1,diesize+1)
    return sum * multiplier

def parseCoins(coins:list):
    cp = parseCoin(coins[0])
    sp = parseCoin(coins[1])
    ep = parseCoin(coins[2])
    gp = parseCoin(coins[3])
    pp = parseCoin(coins[4])
    return [cp,sp,ep,gp,pp]

def parseGems(expression:str):
    quantity, *e = re.split("[dx]",expression)
    quantity = int(quantity)
    diesize = 0
    multiplier = 1
    if len(e) >= 1:
        diesize = int(e[0])
    if len(e) >=2:
        multiplier = int(e[1])
    sum = 0
    description = random.choice(tables.gemDescriptions[multiplier])
    for i in range(quantity):
        sum += random.randrange(1,diesize+1)
    return f"A collection of {description} worth {sum * multiplier} gold coins"

def parseArt(expression:str):
    quantity, *e = re.split("[dx]",expression)
    quantity = int(quantity)
    diesize = 0
    multiplier = 1
    if len(e) >= 1:
        diesize = int(e[0])
    if len(e) >=2:
        multiplier = int(e[1])
    sum = 0
    description = random.choice(tables.artDescriptions[multiplier])
    for i in range(quantity):
        sum += random.randrange(1,diesize+1)
    return f"A {description} worth {sum * multiplier} pieces of gold"

def parseMagicItems(expression:str):
    quantity, diesize, magicTable = re.split("[dx]",expression)
    quantity = int(quantity)
    diesize = int(diesize)
    sum = 0
    for i in range(quantity):
        sum += random.randrange(1,diesize+1)
    items = ""
    for i in range(sum):
        d100 = random.randrange(100)
        items += tables.magicItems[magicTable][d100] + "\n"
    return items

def horde():
    cr = int(input("what is the CR you are using to determine this hoard? integers between 0 and 25 only please "))
    coins = parseCoins(tables.hoard[cr]["coins"])
    d100 = random.randrange(100)
    art = parseArt(tables.hoard[cr]['valuables'][d100]['art'])
    gems = parseGems(tables.hoard[cr]['valuables'][d100]['gems'])
    items = parseMagicItems(tables.hoard[cr]['valuables'][d100]['magic'])
    #TODO form the output into a pretty string
    print(coins)
    print(art)
    print(gems)
    print(items)



def individual(coins = [0,0,0,0,0]):
    cr = int(input("what is the CR of your creature? integers between 0 and 25 only please "))
    quantity = int(input("how may creatures are CR " + str(cr)))
    for i in range(quantity):
        d100 = random.randrange(100)
        coinExpressions = tables.individual[cr][d100]
        coins = list(map(operator.add, coins, parseCoins(coinExpressions)))
    end = input("More creatures? ")
    if end == "yes":
        individual(coins)
        return
    print(f"{coins[0]} copper pieces, {coins[1]} silver pieces, {coins[2]} 'electrum' pieces, {coins[3]} gold pieces, {coins[4]} platinum pieces")

treasure_type = input("individual or horde?(h/i)")
if treasure_type == "h":
    horde()
else:
    individual()
