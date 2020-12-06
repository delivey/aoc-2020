f = open("input.txt", "r").read()


pattern_r = 3 # Pattern for going to the right
pattern_d = 1 # Pattern for going down

tree = "#"
trees = 0

split_f = []

for idx, line in enumerate(f.splitlines()):
    split_f.append(line)

current_r = 0
current_d = 0
for idx, line in enumerate(split_f):

    current_r += pattern_r
    current_d += pattern_d

    valid_check = False

    while valid_check == False:
        try:

            if split_f[current_d][current_r] == tree:
                trees += 1
            else:
                pass

            valid_check = True
        except IndexError:
            try:
                split_f[current_d] += split_f[current_d]
            except IndexError:
                break

print(trees)