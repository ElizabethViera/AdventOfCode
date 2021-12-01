import re
fileContents = open("Day 7/input")
arr = fileContents.read().split('\n')
color_lines = {}

bag_set = set(["shiny gold"])
for i in range(0, 1001):
    for i, line in enumerate(arr):
        bag_arr = line.split("bag")
        left_color = bag_arr[0].strip()
        colors_index = i
        color_lines[left_color] = colors_index
        for bag in range(1, len(bag_arr) - 1):
            if bag_arr[bag] == "s contain no other ":
                continue
            else:
                new_colors = set()
                for bag_color in bag_set:
                    if bag_color in bag_arr[bag]:
                        new_colors.add(left_color)
                for c in new_colors:
                    bag_set.add(c)
print(len(bag_set) - 1)

frontier = ["shiny gold"]
total_bags_needed = 0
while(len(frontier) > 0):
    # print(frontier)
    current_color = frontier.pop()
    current_index = color_lines[current_color]
    current_line = arr[current_index]
    j = current_line.split("contain ")
    k = re.split("bag|bags", j[1])[:-1]
    # print(k)
    for bag_type in k:
        bag_words = bag_type.strip().split(" ")
        # print(bag_words)
        if "no" in bag_words:
            continue
        next_color = bag_words[-2] + " " + bag_words[-1]
        # print(bag_words)
        number_of_bags = int(bag_words[-3])
        total_bags_needed += number_of_bags
        for i in range(number_of_bags):
            frontier.append(next_color)

print(total_bags_needed)
