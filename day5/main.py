f = open("input.txt", "r").readlines()

seat_ids = []
for string in f:
    string = string.replace("\n", "")

    row = 0
    column = 0
    r_mn = 0
    r_mx = 127

    c_mn = 0
    c_mx = 7 
    
    for i in string:

        if i == "F":
            r_mx = round(((r_mx + r_mn) / 2) - 0.5)
            row = r_mn
        elif i == "B":
            r_mn = round((r_mx + r_mn) / 2)
            row = r_mx
        
        elif i == "L":
            c_mx = round(((c_mx + c_mn) / 2)  - 0.5)
            column = c_mn
        elif i == "R":
            c_mn = round(((c_mx + c_mn) / 2))
            column = c_mx

    seat_id = row * 8 + column
    print(row, column, seat_id)
    seat_ids.append(seat_id)

print(max(seat_ids))
