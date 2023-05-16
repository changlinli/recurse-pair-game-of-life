ALIVE = 'O'
DEAD = 'X'

top_grid = [
    [ALIVE, ALIVE, DEAD, ALIVE],
    [ALIVE, ALIVE, DEAD, ALIVE],
    [ALIVE, DEAD, DEAD, ALIVE],
    [DEAD, DEAD, DEAD, ALIVE],
]

def is_live(cell):
    return cell == ALIVE

def get_neighbour_values(x, y, grid):
    all_neighbour_coordinates = \
        [(neighbour_x, neighbour_y) for neighbour_x in range(x - 1, x + 2) for neighbour_y in range(y - 1, y + 2) if
         neighbour_x >= 0 and neighbour_y >= 0]
    print(all_neighbour_coordinates)
    all_neighbour_values = [ grid[neighbour_x][neighbour_y] for (neighbour_x, neighbour_y) in all_neighbour_coordinates ]
    return all_neighbour_values

def check_cell(x, y, grid):
    all_live_neighbours = [neighbour for neighbour in get_neighbour_values(x, y, grid) if is_live(neighbour)]
    num_of_live_neighbours = len(all_live_neighbours)
    if is_live(grid[x][y]):
        if num_of_live_neighbours < 2:
            return DEAD
        elif num_of_live_neighbours >= 2 and num_of_live_neighbours <= 3:
            return ALIVE
        elif num_of_live_neighbours > 3:
            return DEAD
    else:
        if num_of_live_neighbours == 3:
            return ALIVE
        else:
            return DEAD


def check_two_live_neighbours(x, y, grid):
    all_live_neighbours = [ neighbour for neighbour in get_neighbour_values(x, y, grid) if is_live(neighbour) ]


print(get_neighbour_values(2, 2, top_grid))





# infinite loop
# check cell is alive
# if cell is alive, call check_two_live_neighbours()
# if fewer than two live neighbours, convert to dead cell