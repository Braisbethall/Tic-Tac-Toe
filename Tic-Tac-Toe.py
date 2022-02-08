grid = [["-" for x in range(3)] for y in range(3)]
grid_elements = list("-" * 9)
digits = list("1234567890")
total_moves = 9


def win_check():
    x_set = ["X" for _ in range(3)]
    o_set = ["0" for _ in range(3)]
    winning_sets = [grid_elements[0:3], grid_elements[3:6], grid_elements[6:], grid_elements[0::3],
                    grid_elements[1::3], grid_elements[2::3], grid_elements[0::4], grid_elements[2:7:2]]
    for set_ in winning_sets:
        if x_set == set_:
            return "X wins"
        elif o_set == set_:
            return "0 wins"


def print_grid():
    print(f"""---------
| {grid[0][0]} {grid[0][1]} {grid[0][2]} |
| {grid[1][0]} {grid[1][1]} {grid[1][2]} |
| {grid[2][0]} {grid[2][1]} {grid[2][2]} |
---------""")


print_grid()
while total_moves > 0:
    coordinates = input("Enter the coordinates through a space: ").split()
    if len(coordinates) != 2 or coordinates[0] not in digits or coordinates[1] not in digits:
        print("You should enter two single digits!")
    elif int(coordinates[0]) < 1 or int(coordinates[0]) > 3 or int(coordinates[1]) < 1 or int(coordinates[1]) > 3:
        print("Coordinates should be from 1 to 3!")
    elif grid[int(coordinates[0])-1][int(coordinates[1])-1] != "-":
        print("This cell is occupied! Choose another one!")
    else:
        grid[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = "0"\
            if grid_elements.count("X") > grid_elements.count("0") else "X"
        grid_elements[(int(coordinates[0]) * 3 - 3) + int(coordinates[1]) - 1] = "0"\
            if grid_elements.count("X") > grid_elements.count("0") else "X"
        total_moves -= 1
        print_grid()
        if win_check():
            print(win_check())
            break
else:
    print("Draw")