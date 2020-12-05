passwords = []

with open('input.txt', 'r') as f: # Creates the entries list
    for line in f:
        line = line.strip()
        passwords.append(line)

# 1
valids = 0

for i in passwords:
    data = i.split(': ')
    requirements = data[0]
    password = data[1]

    req_data = requirements.split(" ")

    limits = req_data[0]
    letter = req_data[1]

    limits_data = limits.split("-")
    minimum = int(limits_data[0])
    maximum = int(limits_data[1])

    letters = password.count(letter)

    if letters >= minimum and letters <= maximum:
        valids += 1

print(valids)

# 2
new_valids = 0
for i in passwords:
    data = i.split(': ')
    requirements = data[0]
    password = data[1]

    req_data = requirements.split(" ")

    limits = req_data[0]
    letter = req_data[1]

    limits_data = limits.split("-")
    position_1 = int(limits_data[0]) - 1
    position_2 = int(limits_data[1]) - 1

    positions = [pos for pos, char in enumerate(password) if char == letter]

    # Shouldn't do this, but it works
    if position_1 in positions and position_2 not in positions or position_2 in positions and position_1 not in positions:
        print(positions, "VALID")
        new_valids += 1

print(new_valids)