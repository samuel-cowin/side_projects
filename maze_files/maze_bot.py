import maze
import math
import collections

def check_no_collision(xm, ym, xh, yh, maze_data):
    if  ym+1 == yh:
        if (maze_data[math.ceil(yh)][math.floor(xh)]):
            return True
        else:
            return False
    elif xm+1 == xh:
        if (maze_data[math.floor(yh)][math.ceil(xh)]):
            return True
        else:
            return False
    elif xm-1 == xh:
        if (maze_data[math.floor(yh)][math.floor(xh)]):
            return True
        else:
            return False
    elif ym-1 == yh:
        if (maze_data[math.floor(yh)][math.floor(xh)]):
            return True
        else:
            return False
    else:
        return False

def go_down(x, y):
    y = y + 1
    maze.plt.pause(0.5)
    maze.plt.plot(x, y, 'go')
    maze.plot_maze(test_maze)
    return x, y

def go_right(x, y):
    x = x + 1
    maze.plt.pause(0.5)
    maze.plt.plot(x, y, 'go')   
    maze.plot_maze(test_maze)
    return x, y

def go_left(x, y):
    x = x - 1
    maze.plt.pause(0.5)
    maze.plt.plot(x, y, 'go')
    maze.plot_maze(test_maze)
    return x, y

def go_up(x, y):
    y = y - 1
    maze.plt.pause(0.5)
    maze.plt.plot(x, y, 'go')
    maze.plot_maze(test_maze)
    return x, y

def bfs(grid, start, goal):
    width = len(grid[0])
    height = len(grid)
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and check_no_collision(x, y, x2, y2, grid) and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

def execute_path(moves, x1, y1):
    if moves is not None:
        for i in range(len(moves)-1):
            if  moves[i][1]+1 == moves[i+1][1]:
                x1, y1 = go_down(x1, y1)
            elif moves[i][0]+1 == moves[i+1][0]:
                x1, y1 = go_right(x1, y1)
            elif moves[i][0]-1 == moves[i+1][0]:
                x1, y1 = go_left(x1, y1)
            elif moves[i][1]-1 == moves[i+1][1]:
                x1, y1 = go_up(x1, y1)
        
test_maze = []
flag = 1

#size of maze
x = int(input('Provide x complexity (1-50): '))
y = int(input('Provide y complexity (1-50): '))

#Maze generation
test_maze = maze.make_maze(x, y)
        
#add host
x_host = 1.5
y_host = 0.5
maze.plt.plot(x_host, y_host, 'go')
        
#show initial point
maze.plot_maze(test_maze)

#Find optimal path with all information
print(test_maze)    
best_path = bfs(test_maze, (math.floor(x_host), math.floor(y_host)), 2)
print(best_path)

#show path
input('Press enter when ready')
execute_path(best_path, x_host, y_host)