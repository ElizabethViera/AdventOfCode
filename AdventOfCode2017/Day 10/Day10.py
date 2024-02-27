nums = [i for i in range(256)]
current_pos = 0
skip_size = 0
original_len = len(nums)

fileContents = open("AdventOfCode2017/Day 10/input.txt")
lengths = fileContents.read()
all_lengths: list[int] = []
for l in lengths:
    length = int(ord(l))
    all_lengths.append(length)
add_these = [17,31,73,47,23]
for this in add_these:
    all_lengths.append(this)

print(all_lengths)
for i in range(64):
    for length in all_lengths:
        if current_pos + length > original_len:
            extra_length = (current_pos+length) - original_len 
            nums = nums + nums[:extra_length]
        prefix = nums[:current_pos]
        reversed_ = nums[current_pos:current_pos+length][::-1] 
        suffix = nums[current_pos+length:]
        nums = prefix + reversed_ + suffix
        
        if len(nums) > original_len:
            end = nums[original_len:]
            nums = end + nums[len(end):]
            nums = nums[:original_len]
        current_pos += length + skip_size
        current_pos %= original_len
        skip_size += 1

chunks = list(zip(*(iter(nums),) * 16))
for chunk in chunks:
    i = 0
    for item in chunk:
        i ^= item
    print ("i", hex(i))