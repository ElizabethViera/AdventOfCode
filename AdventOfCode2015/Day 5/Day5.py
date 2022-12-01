fileContents = open("AdventOfCode2015/Day 5/input.txt")
arr = fileContents.read().split('\n')

nice = 0
for string in arr:

    # Case 1: Double Letters
    string_ind = 0
    found_double_letter = False
    for c in string[2:]:
        if c == string[string_ind]:
            found_double_letter = True
        string_ind += 1
    if not found_double_letter:
        continue

    # Case 2:
    ind = 0
    found_double_string = False
    while ind+1 < len(string):
        c1, c2 = string[ind], string[ind+1]
        if c1+c2 in string[ind+2:]:
            print(c1+c2, string[ind+1:])
            found_double_string = True
        ind += 1
    if not found_double_string:
        continue
    nice += 1

print(nice)
