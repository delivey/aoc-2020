passwords = []

with open('input.txt', 'r') as f: # Creates the entries list
    for line in f:
        line = line.strip()
        passwords.append(line)

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