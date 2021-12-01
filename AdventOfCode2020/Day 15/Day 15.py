fileContents = open("Day 15/input")
arr = fileContents.read().split('\n')

arr = [int(i) for i in arr]
current_num_index = 0
spoken_words = {}

for i in arr:
    if i in spoken_words:
        spoken_words[i].append(current_num_index)
    else:
        spoken_words[i] = [current_num_index]
    current_num_index += 1

last_spoken_word = arr[-1]
print(last_spoken_word)
while(current_num_index < 30000000):
    if len(spoken_words[last_spoken_word]) == 1:
        last_spoken_word = 0
    else:
        last_spoken_word = spoken_words[last_spoken_word][-1] - \
            spoken_words[last_spoken_word][-2]
    if last_spoken_word in spoken_words:
        spoken_words[last_spoken_word].append(current_num_index)
    else:
        spoken_words[last_spoken_word] = [current_num_index]
    current_num_index += 1

print(current_num_index, last_spoken_word)
