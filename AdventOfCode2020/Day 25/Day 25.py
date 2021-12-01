card_public_key = First number!
door_public_key = Second number!
subject_number = 7

value = 1
for i in range(50000000):
    value *= subject_number
    value %= 20201227
    if value == card_public_key:
        print(i, "card")
    if value == door_public_key:
        print(i, "door")

value = 1
for i in range(10985209):
    value *= door_public_key
    value %= 20201227
print(value, "door public key with card subject")


value = 1
for i in range(925199):
    value *= card_public_key
    value %= 20201227
print(value, "card public key with card subject")
