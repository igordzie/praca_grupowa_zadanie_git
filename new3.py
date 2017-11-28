pascals_triangle = []

def blank_list_gen(x):
    while len(pascals_triangle) < x:
        pascals_triangle.append([0])

def pascals_tri_gen(rows):
    blank_list_gen(rows)
    for element in range(rows):
        count = 1
        while count < rows - element:
            pascals_triangle[count + element].append(0)
            count += 1
    for row in pascals_triangle:
        row.insert(0, 1)
        row.append(1)
    pascals_triangle.insert(0, [1, 1])
    pascals_triangle.insert(0, [1])

pascals_tri_gen(6)

for row in pascals_triangle:
    print(row)