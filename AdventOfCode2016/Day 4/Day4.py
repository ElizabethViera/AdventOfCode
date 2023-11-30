
fileContents = open("AdventOfCode2016/Day 4/input.txt")
arr = fileContents.read().split("\n")

def check_checksum(s, checksum):
    character_count = dict()
    for c in s:
        if c not in character_count:
            character_count[c] = 0
        character_count[c] += 1

    sorted_characters = sorted(character_count.items(), key=lambda x:(-1*x[1], x[0]))
    result = ""
    for character in sorted_characters[:5]:
        result += character[0]
    return result == checksum

alphabet = "abcdefghijklmnopqrstuvwxyz"

def decryptRoom(s, n):
    result = ""
    for c in s:
        if c == "-":
            result += " "
        else:
            indexOfAlphabet = alphabet.index(c)
            result += alphabet[(indexOfAlphabet + n)%26]
    return result


total = 0
for line in arr:
    checksum = line[-6:-1]
    room_code = line[:-7].split('-')[-1]
    everything_else = ''.join(line[:-7].split('-')[:-1])
    if check_checksum(everything_else, checksum):
        result = decryptRoom(everything_else, int(room_code))
        if result == "northpoleobjectstorage":
            print(room_code)



print(total)


