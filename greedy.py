from pyMaze import maze,agent,COLOR,textLabel

def greedy_search(m, start=None):
    if start is None:
        start = (m.rows, m.cols)
    explored = set()
    frontier = [(start, heuristic(start, m._goal))]  
    greedy_path = {}
    search_path = []

    while frontier:
        curr_cell, _ = frontier.pop(0) 
        search_path.append(curr_cell)
        
        if curr_cell == m._goal:
            break

        for direction in 'ESNW':
            if m.maze_map[curr_cell][direction]:
                if direction == 'E':
                    child = (curr_cell[0], curr_cell[1] + 1)
                elif direction == 'W':
                    child = (curr_cell[0], curr_cell[1] - 1)
                elif direction == 'N':
                    child = (curr_cell[0] - 1, curr_cell[1])
                elif direction == 'S':
                    child = (curr_cell[0] + 1, curr_cell[1])

                if child not in explored:
                    explored.add(child)
                    heuristic_value = heuristic(child, m._goal)
                    frontier.append((child, heuristic_value))
                    greedy_path[child] = curr_cell

        frontier.sort(key=lambda x: x[1])  

    fwd_path = {}
    cell = m._goal
    while cell != start:
        fwd_path[greedy_path[cell]] = cell
        cell = greedy_path[cell]

    return search_path, greedy_path, fwd_path

def heuristic(curr_cell, goal_cell):
    
    return abs(curr_cell[0] - goal_cell[0]) + abs(curr_cell[1] - goal_cell[1])

if __name__ == '__main__':
    m = maze(10, 15)  
    m.CreateMaze(10, 15)  

    search_path, greedy_path, fwd_path = greedy_search(m, (1, 1)) 

    a = agent(m, 1, 1, goal=(10, 15), footprints=True, shape='square', color=COLOR.green)
    b = agent(m, 10, 15, goal=(1, 1), footprints=True, filled=True)
    c = agent(m, 1, 1, footprints=True, color=COLOR.yellow)
    m.tracePath({a: search_path}, showMarked=True)
    m.tracePath({b: greedy_path})
    m.tracePath({c: fwd_path})
    l=textLabel(m,'Greedy Path Length',len(fwd_path)+1)
    l=textLabel(m,'Greedy Search Length',len(search_path))
    m.run()