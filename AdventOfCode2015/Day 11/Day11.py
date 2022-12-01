

def isValid(s):
    return containsStraight(s) and doesNotContainProhibited(s) and hasPairs(s)

def containsStraight(s):
    straights = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvx', 'vxy', 'xyz']
    for straight in straights:
        if straight in s:
            return True
    return False

def doesNotContainProhibited(s):
    return not('l' in s or 'o' in s or 'i' in s)

def hasPairs(s):
    pairs = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'jj', 'kk', 'mm', 'nn', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']
    count = 0
    for pair in pairs:
        if pair in s:
            count += 1
        if count == 2:
            return True
    return False

alphabet = 'abcdefghijklmnopqrstuvwxyz'
chars_to_nums = {}
nums_to_chars = {}
for i in range(26):
    chars_to_nums[alphabet[i]] = i+1
    nums_to_chars[i+1] = alphabet[i]
print(chars_to_nums)

def increment(s):
    # flip to increment
    s = s[::-1]
    result = ""
    for i, c in enumerate(s):
        new_index = chars_to_nums[c] + 1
        if new_index != 27:
            result += nums_to_chars[new_index]
            result += s[i+1:]
            break
        else:
            # we will continue to the next digit
            new_index = 1
            result += nums_to_chars[new_index]
    return result[::-1]

current_string = 'vzbxxyzz'

def find_next_password(current_string):
    while(True):
        new_string = increment(current_string)
        if isValid(new_string):
            return new_string
        current_string = new_string

print(find_next_password(current_string))