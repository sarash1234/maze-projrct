from pyMaze import maze,agent,textLabel,COLOR

def DFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    dSeacrh=[]
    while len(frontier)>0:
        currCell=frontier.pop()
        dSeacrh.append(currCell)
        if currCell==m._goal:
            break
        poss=0
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d =='E':
                    child=(currCell[0],currCell[1]+1)
                if d =='W':
                    child=(currCell[0],currCell[1]-1)
                if d =='N':
                    child=(currCell[0]-1,currCell[1])
                if d =='S':
                    child=(currCell[0]+1,currCell[1])
                if child in explored:
                    continue
                poss+=1
                explored.append(child)
                frontier.append(child)
                dfsPath[child]=currCell
        if poss>1:
            m.markCells.append(currCell)
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return dSeacrh,dfsPath,fwdPath

if __name__=='__main__':
    m=maze(20,20) 
    m.CreateMaze(20,20,loopPercent=40) 
    dSeacrh,dfsPath,fwdPath=DFS(m,(1,1)) 
    a=agent(m,1,1,goal=(20,20),footprints=True,shape='square',color=COLOR.green)
    b=agent(m,20,20,goal=(1,1),footprints=True,filled=True)
    c=agent(m,1,1,footprints=True,color=COLOR.yellow,shape='arrow',filled=True)
    m.tracePath({a:dSeacrh},delay=70,showMarked=True)
    m.tracePath({b:dfsPath},delay=70)
    m.tracePath({c:fwdPath},delay=70)
    l=textLabel(m,'DFS Path Length',len(fwdPath)+1)
    l=textLabel(m,'DFS Search Length',len(dSeacrh))
    m.run()

