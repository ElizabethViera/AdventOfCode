fileContents = open("input")
arr = fileContents.read().split('\n')

passport = {}
validPassports = 0

requiredKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
acceptedNumChars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                    "a", "b", "c", "d", "e", "f"]
acceptedEyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
acceptedNums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def validatePassport(passport):
    print("Start Validate")
    for requiredKey in requiredKeys:
        if requiredKey in passport:
            print(requiredKey, passport[requiredKey])
            if requiredKey == "byr":
                try:
                    byr = int(passport["byr"])
                    if byr < 1920 or byr > 2002 or len(passport["byr"]) != 4:
                        return 0
                except Exception:
                    return 0
            if requiredKey == "iyr":
                try:
                    iyr = int(passport["iyr"])
                    # print("iyr is equal to", iyr)
                    if iyr < 2010 or iyr > 2020 or len(passport["iyr"]) != 4:
                        return 0
                except Exception:
                    return 0
            if requiredKey == "eyr":
                try:
                    eyr = int(passport["eyr"])
                    if eyr < 2020 or eyr > 2030 or len(passport["eyr"]) != 4:
                        return 0
                except Exception:
                    return 0
            if requiredKey == "hgt":
                try:
                    hgt = int(passport["hgt"][:-2])
                    print(hgt)
                    hgtunit = passport["hgt"][-2:]
                    # print("height = ", hgt, passport["hgt"], hgtunit)
                    if hgtunit == "cm":
                        if hgt < 150 or hgt > 193:
                            return 0
                    elif hgtunit == "in":
                        if hgt < 59 or hgt > 76:
                            return 0
                    else:
                        return 0
                except Exception:
                    return 0
            if requiredKey == "hcl":
                if passport["hcl"][0] != "#":
                    return 0
                if len(passport["hcl"]) != 7:
                    return 0
                for c in passport["hcl"][1:]:
                    if c not in acceptedNumChars:
                        return 0
            if requiredKey == "ecl":
                if passport["ecl"] not in acceptedEyeColors:
                    return 0
            if requiredKey == "pid":
                if len(passport["pid"]) != 9:
                    return 0
                for c in passport["pid"]:
                    if c not in acceptedNums:
                        return 0
        else:
            return 0
    print("accepted ", passport)
    return 1


for line in arr:
    if line == "":
        validPassports += validatePassport(passport)
        passport = {}
    else:
        fields = line.split(" ")
        for field in fields:
            k, v = field.split(":")
            passport[k] = v

validPassports += validatePassport(passport)
print(validPassports)
