from pyMaze import maze,COLOR,agent
m=maze(10,15)
m.CreateMaze(loopPercent=20)
a=agent(m,filled=True,footprints=False)
m.enableArrowKey(a)
m.run()