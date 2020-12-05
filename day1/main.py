entries = []

with open('input.txt', 'r') as f: # Creates the entries list
    for line in f:
        line = line.strip()
        entries.append(line)

wanted_number = 2020

# 1
for i in entries:
    for j in entries:
        if int(i) + int(j) == wanted_number:
            print(int(i) * int(j))

# 2
for i in entries:
    for j in entries:
        for h in entries: 
            if int(i) + int(j) + int(h) == wanted_number:
                print(int(i) * int(j) * int(h))
