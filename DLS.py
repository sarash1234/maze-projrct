from pyMaze import maze,agent,textLabel,COLOR

def DLS(m, start=None, depth_limit=0):
    if start is None:
        start = (m.rows, m.cols)
    explored = set()  
    frontier = [(start, 0)] 
    dlsPath = {}
    dSearch = []
    while frontier:
        currCell, depth = frontier.pop()
        dSearch.append(currCell)
        if currCell == m._goal:
            break
        if depth >= depth_limit:
            continue  
        poss = 0
        for d in 'ESNW':
            if m.maze_map[currCell][d]:
                if d == 'E':
                    child = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    child = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    child = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    child = (currCell[0] + 1, currCell[1])
                if child in explored:
                    continue
                poss += 1
                explored.add(child)
                frontier.append((child, depth + 1)) 
                dlsPath[child] = currCell
        if poss > 1:
            m.markCells.append(currCell)
    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[dlsPath[cell]] = cell
        cell = dlsPath[cell]
    return dSearch, dlsPath, fwdPath

if __name__ == '__main__':
    m = maze(20, 20)  
    m.CreateMaze(10,10,loopPercent=40)  
    dSearch, dlsPath, fwdPath = DLS(m, (1, 1), depth_limit=30)
    a = agent(m, 1, 1, goal=(10, 10), footprints=True, shape='square', color=COLOR.green)
    b = agent(m, 10, 10, goal=(1, 1), footprints=True, filled=True)
    c = agent(m, 1, 1, footprints=True,shape='arrow', color=COLOR.yellow)
    m.tracePath({a: dSearch}, showMarked=True)
    m.tracePath({b: dlsPath})
    m.tracePath({c: fwdPath})
    l=textLabel(m,'DLS Path Length',len(fwdPath)+1)
    l=textLabel(m,'DLS Search Length',len(dSearch))
    m.run()


