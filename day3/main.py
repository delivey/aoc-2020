f = open("input.txt", "r").read()

tree = "#"

split_f = []

for idx, line in enumerate(f.splitlines()):
    split_f.append(line)


def run_slope(pattern_r, pattern_d):

    trees = 0
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

    return trees

# 1
print(run_slope(3, 1))

# 2
slopes = {
    1: {"right": 1, "down": 1},
    2: {"right": 3, "down": 1},
    3: {"right": 5, "down": 1},
    4: {"right": 7, "down": 1},
    5: {"right": 1, "down": 2}
}

results = []
for i in list(range(1, (len(slopes)+1))):
    number = i
    right = slopes[i]["right"]
    down = slopes[i]["down"]

    result = run_slope(right, down)
    results.append(result)

# https://www.geeksforgeeks.org/python-multiply-numbers-list-3-different-ways/
def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x 
    return result 

answer = multiplyList(results)
print(answer)
