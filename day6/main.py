f = open("input.txt", "r").read()

# 1
groups = f.split("\n\n")

total = 0
for group in groups:
    group = group.replace("\n", "")

    string = "".join(set(group))
    total += len(string)

print(total)