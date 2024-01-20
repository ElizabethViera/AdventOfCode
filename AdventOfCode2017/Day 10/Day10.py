nums = [i for i in range(5)]
current_pos = 0
skip_size = 0
original_len = len(nums)

fileContents = open("AdventOfCode2017/Day 10/input.txt")
lengths = fileContents.read().split(",")
for l in lengths:
    print(nums)
    length = int(l)
    if current_pos + length > original_len:
        extra_length = (current_pos+length) - original_len 
        nums = nums + nums[:extra_length]
    prefix = nums[:current_pos]
    reversed_ = nums[current_pos+length-1:current_pos:-1] 
    suffix = nums[current_pos+length:]
    nums = prefix + reversed_ + suffix
    print(prefix)
    print(reversed_)
    print(suffix)
    
    if len(nums) > original_len:
        end = nums[original_len:]
        nums = end + nums[len(end):]
    current_pos += length + skip_size
    current_pos %= original_len
    skip_size += 1
print(nums[0]*nums[1])