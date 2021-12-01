fileContents = open("Day 16/input")
arr = fileContents.read().split('\n')

fields = []
my_ticket = [139, 113, 127, 181, 53, 149, 131, 239, 137,
             241, 89, 151, 109, 73, 157, 59, 107, 83, 173, 179]
other_tickets = []

fields_bool = False

for line in arr:
    if line == "":
        fields_bool = True

    elif not fields_bool:
        fields.append(line)
    else:
        other_tickets.append([int(val) for val in line.split(',')])

value_set = set()
for line in fields:
    field_name = line.split(":")[0]
    values = line.split(": ")[1].split(" or ")
    for value in values:
        range_val = value.split("-")
        for i in range(int(range_val[0]), int(range_val[1])+1):
            value_set.add(i)

total = 0
valid_tickets = []
for ticket in other_tickets:
    ticket_valid = True
    for v in ticket:
        if int(v) not in value_set:
            ticket_valid = False
    if ticket_valid:
        valid_tickets.append(ticket)

for t in valid_tickets:
    for i, v in enumerate(t):
        if v > 437 and v < 452:
            print("not class: ", v, i)

answer = 1
a = [131, 239, 109, 73, 157, 173]
print(131*239*109*73*157*173)
