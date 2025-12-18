fileContents = open("Day 11/input.txt")
arr = fileContents.read().split("\n")
# print(arr)

connections = dict()

for line in arr:
    key = line.split(": ")[0]
    values = line.split(": ")[1].split()
    connections[key] = values


# starting with (svr, 1),
# connections[svr]
def computeNextLayer(sources: list[tuple[str, int]]):
    next_sources: dict[str, int] = dict()
    for source in sources:
        # a source is a location, and a number of ways to get to that location
        next_layer = connections[source[0]]
        for child in next_layer:
            if child not in next_sources:
                next_sources[child] = 0
            next_sources[child] += source[1]
    # print(next_sources)
    return [(k, next_sources[k]) for k in next_sources]


def something(inp, num):
    to_compute = [(inp, num)]
    already_computed = dict()
    already_computed["out"] = 0
    already_computed["dac"] = 0
    already_computed["fft"] = 0

    while to_compute != []:
        next_layer = computeNextLayer(to_compute)
        to_compute = []
        for item in next_layer:
            if item[0] == "out":
                already_computed["out"] += item[1]
            elif item[0] == "dac":
                already_computed["dac"] += item[1]
            elif item[0] == "fft":
                already_computed["fft"] += item[1]
            else:
                if item[0] not in already_computed:
                    already_computed[item[0]] = 0
                already_computed[item[0]] += item[1]
                to_compute.append((item[0], item[1]))

    return already_computed


first = something("svr", 1)
r1, r2 = first["dac"], first["fft"]
print(r1, r2)

second1 = something("dac", r1)["fft"]
second2 = something("fft", r2)["dac"]

print(second1, second2)

third = something("dac", second2)["out"]
print(third)


"""
from svr:
dac = 445017736117040
fft = 16740

from svr to fft to dac is 818780920560

"""
