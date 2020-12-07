from string import ascii_lowercase

f = open("input.txt", "r").read()

passports = f.split("\n\n")

valids = 0

# 1

for passport in passports:

    passport = passport.replace("\n", " ")
    pairs = passport.split(" ")

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

# 2
new_valids = 0

for passport in passports:

    passport = passport.replace("\n", " ")
    pairs = passport.split(" ")

    needed_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    keys = []
    items = []

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
        "pid": {"pid": True},
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
            pass

        try:
            minn = valid_data["min"]
            if value.isnumeric():
                if int(value) < minn:
                    invalid = True
            else:
                invalid = True
        except KeyError:
            pass

        try:
            maxn = valid_data["max"]
            if value.isnumeric():
                if int(value) > maxn:
                    invalid = True
            else:
                invalid = True
        except KeyError:
            pass

        try: # For hgt (height)
            start_type = valid_data["start_type"]
            unit = value[-2:]
            clean = value[:-2]
            if clean.isnumeric():
                clean = int(clean)
                if unit == "cm":
                    if clean >= 150 and clean <= 193:
                        pass
                    else:
                        invalid = True
                elif unit == "in":
                    if clean >= 59 and clean <= 76:
                        pass
                    else:
                        invalid = True
                else:
                    invalid = True
        except KeyError:
            pass

        try:
            start = valid_data["start"]
            if not value[0] == start:
                invalid = True
        except KeyError:
            pass

        try:
            end_type = valid_data["end_type"] # chars
            last_6 = value[-6:]

            for i in last_6:
                if not i in ascii_lowercase and not i.isnumeric():
                    invalid = True
        except KeyError:
            pass

        try:
            possible = valid_data["possible"]
            if value not in possible:
                invalid = True
        except KeyError:
            pass

        try:
            pid = valid_data["pid"]

            if len(value) != 9:
                invalid = True

            if not value.isnumeric():
                invalid = True
        except KeyError:
            pass

    if not invalid:
        new_valids += 1


print(new_valids)
        

