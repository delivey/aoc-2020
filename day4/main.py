import string

f = open("input.txt", "r").read()

passports = f.split("\n\n")

valids = 0

# 1

for i in passports:

    i = i.replace("\n", " ")
    pairs = i.split(" ")

    needed_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    keys = []

    for pair in pairs:
        key = pair.split(":")[0]
        keys.append(key)

    invalid = False

    for needed_key in needed_keys:
        if needed_key not in keys:
            invalid = True

    if not invalid:
        valids += 1
        
print(valids)


new_valids = 0
# 2

for i in passports:

    i = i.replace("\n", " ")
    pairs = i.split(" ")

    needed_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    items = []
    keys = []

    for pair in pairs:
        key = pair.split(":")[0]
        value = pair.split(":")[1]
        keys.append(key)
        items.append((key, value))

    invalid = False

    for needed_key in needed_keys: # Checks if the required keys are there
        if needed_key not in keys:
            invalid = True

    # Parameters for checking if a passport is valid
    valids = {
        "byr": {"len": 4, "min": 1920, "max": 2002},
        "iyr": {"len": 4, "min": 2010, "max": 2020},
        "eyr": {"len": 4, "min": 2020, "max": 2030},
        "hgt": {"start_type": "int"},
        "hcl": {"len": 7, "start": "#", "end_type": "chars"},
        "ecl": {"possible": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]},
        "pid": {"len": 9, "start": "0"},
        "cid": {}
    }

    for tup in items:
        key = tup[0]
        value = tup[1]

        valid_data = valids[key]

        try:
            length = valid_data["len"]
            if len(value) != length:
                invalid = True
        except KeyError:
            length = False

        try:
            minn = valid_data["min"]
            if int(value) < minn:
                invalid = True
        except KeyError:
            minn = False

        try:
            maxn = valid_data["max"]
            if int(value) > maxn:
                invalid = True
        except KeyError:
            maxn = False

        try: # For hgt (height)
            start_type = valid_data["start_type"]
            clean_string = (value.replace("cm", "").replace("in", ""))
            if clean_string.isnumeric():
                if "cm" in value:
                    if int(clean_string) > 150 and int(clean_string) < 193:
                        pass
                    else:
                        invalid = True
                if "in" in value:
                    if int(clean_string) > 59 and int(clean_string) < 76:
                        pass
                    else:
                        invalid = True
                else:
                    invalid = True
            

        except KeyError:
            start_type = False

        try:
            start = valid_data["start"]
            if not value.startswith(start):
                invalid = True
        except KeyError:
            start = False

        try:
            end_type = valid_data["end_type"] # chars
            last_6 = value[-6:]

            for i in last_6:
                if i not in list(range(0, 10)) or i not in list(string.ascii_lowercase):
                    invalid = True
        except KeyError:
            end_type = False

        try:
            possible = valid_data["possible"]
            if value not in possible:
                invalid = True
        except KeyError:
            possible = False

        if not invalid:
            new_valids += 1


print(new_valids)
        

