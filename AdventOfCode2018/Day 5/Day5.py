from tokenize import String


letters_to_caps = {
    'a': 'A',
    'A': 'a',
    'b': 'B',
    'B': 'b',
    'c': 'C',
    'C': 'c',
    'd': 'D',
    'D': 'd',
    'e': 'E',
    'E': 'e',
    'f': 'F',
    'F': 'f',
    'g': 'G',
    'G': 'g',
    'h': 'H',
    'H': 'h',
    'i': 'I',
    'I': 'i',
    'j': 'J',
    'J': 'j',
    'k': 'K',
    'K': 'k',
    'l': 'L',
    'L': 'l',
    'm': 'M',
    'M': 'm',
    'n': 'N',
    'N': 'n',
    'o': 'O',
    'O': 'o',
    'p': 'P',
    'P': 'p',
    'q': 'Q',
    'Q': 'q',
    'r': 'R',
    'R': 'r',
    's': 'S',
    'S': 's',
    't': 'T',
    'T': 't',
    'u': 'U',
    'U': 'u',
    'v': 'V',
    'V': 'v',
    'w': 'W',
    'W': 'w',
    'x': 'X',
    'X': 'x',
    'y': 'Y',
    'Y': 'y',
    'z': 'Z',
    'Z': 'z',
}

fileContents = open("AdventOfCode2018/Day 5/input.txt")
super_long_string = fileContents.read().strip()


def explodeString(s) -> str:
    result = ''
    for c in s:
        if result == '':
            result += c
            continue
        if letters_to_caps[result[-1]] == c:
            result = result[:-1]
        else:
            result += c
    return result

minLetters = 15000
for k in letters_to_caps:
    halfRemoved1 = super_long_string.replace(k, '')
    candidate = halfRemoved1.replace(letters_to_caps[k], '')
    numberOfLetters = len(explodeString(candidate))
    if numberOfLetters < minLetters:
        minLetters = numberOfLetters

print(minLetters)