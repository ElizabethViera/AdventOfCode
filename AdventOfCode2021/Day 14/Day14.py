fileContents = open("Day 14/input.txt")
maps = fileContents.read().split('\n')

mappings = {}

for pair in maps:
    LHS = pair.split(' ')[0]
    RHS = pair.split(' ')[-1]
    mappings[(LHS, 1)] = {LHS[0] + RHS: 1, RHS + LHS[1]: 1}


initialString = '** REDACTED **'
initialPairs = [initialString[i] + initialString[i+1]
                for i in range(len(initialString)-1)]


def calculateRecursiveGrowth(pair, n):
    if (pair, n) in mappings:
        return mappings[(pair, n)]
    else:
        return calculateOneMore(calculateRecursiveGrowth(pair, n-1))


def calculateOneMore(pairsDict):
    new_result = {}
    for pair in pairsDict:
        resulting_pairs = mappings[(pair, 1)]
        for resulting_pair in resulting_pairs:
            if resulting_pair not in new_result:
                new_result[resulting_pair] = 0
            new_result[resulting_pair] += pairsDict[pair]
    return new_result


letter_count = {'N': 0, 'C': 0, 'B': 1, 'H': 0,
                'O': 0, 'F': 0, 'S': 0, 'P': 0, 'V': 0, 'K': 0}

for pair in initialPairs:
    result = calculateRecursiveGrowth(pair, 40)

    for result_pair in result:
        letter_count[result_pair[0]] += result[result_pair]

letter_count = sorted(letter_count.values())
print(letter_count[-1] - letter_count[0])
