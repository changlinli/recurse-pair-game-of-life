ALIVE = 'O'
DEAD = 'X'

grid = [
    [ALIVE, ALIVE, DEAD, ALIVE],
    [ALIVE, ALIVE, DEAD, ALIVE],
    [ALIVE, DEAD, DEAD, ALIVE],
    [DEAD, DEAD, DEAD, ALIVE],
]

def is_live(cell):
    return cell == ALIVE

def check_two_live_neighbours(x, y):
    all_neighbours = [(neighbour_x, neighbour_y) for neighbour_x, neighbour_y in ...]





# infinite loop
# check cell is alive
# if cell is alive, call check_two_live_neighbours()
# if fewer than two live neighbours, convert to dead cell