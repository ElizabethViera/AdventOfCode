fileContents = open("AdventOfCode2017/Day 14/input.txt")
arr = fileContents.read().split('\n')

def hash(fileContents: str):
    nums = [i for i in range(256)]
    current_pos = 0
    skip_size = 0
    original_len = len(nums)

    all_lengths = []
    for c in fileContents:
        all_lengths.append(ord(c))
    extra = [17, 31, 73, 47, 23]
    for e in extra:
        all_lengths.append(e)
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
    return chunks
    
def hexify(chunks):
    result = ''
    for chunk in chunks:
        i = 0
        for item in chunk:
            i ^= item
        hexed = hex(i).split('x')[1]
        if len(hexed) == 1:
            hexed = '0' + hexed
        result += hexed
    result_as_bits = ''
    for c in result:
        s = int(c, base=16)
        r = f'{s:04b}'
        result_as_bits += r
    return result_as_bits

n = ''
n += '0'*129
n += '\n'
for a in arr:
    chunks = hash(a)
    n += '0' + hexify(chunks) + '0'
    n += '\n'

n += '0'*129
n += '\n'

print(n)

