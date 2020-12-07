f = open("input.txt", "r").read()

# 1
groups = f.split("\n\n")

total = 0
for group in groups:
    group = group.replace("\n", "")

    string = "".join(set(group))
    total += len(string)

print(total)

# 2

new_total = 0
for group in groups:

    people_in_group = len(group.split("\n"))
    group = group.replace("\n", " ")

    answers = list(group)
    unique_answers = list(set(answers))
    for i in unique_answers:
        people_answered = answers.count(i)
        if people_in_group == people_answered:
            new_total += 1

print(new_total)
    