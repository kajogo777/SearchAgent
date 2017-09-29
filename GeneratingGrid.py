from random import *
class Grid:
	def __init__(self, m, n, robotPos, teleportalPos, unmovables, rocksPos, pressurePos):
        self.m = m
        self.n = n
	self.robotPos = robotPos
        self.teleportalPos = teleportalPos
	self.unmovables = unmovables
	self.rocksPos = rocksPos
	self.pressurePos = pressurePos
	
def GenGrid():

	m = randint(1,10)
	n = randint(1,10)
	robotPos = (randint(0, m-1), randint(0, n-1))
	teleportalPos = (randint(0, m-1), randint(0, n-1))
	
	unmovableNum = randint(1,max(m,n))
	unmovablesPos = []

	for i in range(1, unmovableNum):
		currUnmovable = (randint(0,m-1), randint(0,n-1))
		while ((currUnmovable in unmovablesPos) or (currUnmovable == teleportalPos)):
			currUnmovable = (randint(0,m-1), randint(0,n-1))
		unmovablesPos.append(currUnmovable)

	rocksNum = randint(1, max(m,n))
	rocksPos = []
	pressurePos = []

	for j in range(1, rocksNum):
		currRock = (randint(0,m-1), randint(0,n-1))
		currPressure = (randint(0,m-1), randint(0,n-1))

		while ((currPressure in unmovablesPos) or (currPressure == teleportalPos)):
			currPressure = (randint(0,m-1), randint(0,n-1))
		
		pressurePos.append(currPressure) 

		while ((currRock in unmovablesPos) or (currRock in pressurePos) or (currRock == teleportalPos) or (currRock == robotPos)):
			currRock = (randint(0,m-1), randint(0,n-1))
		
		rocksPos.append(currRock) 

	print("m = ",m)
	print("n = ", n)
	print("The robot is at ", robotPos)
	print("Teleportal is at ", teleportalPos)
	print("There is unmovable objects at ", unmovablesPos)
	print("The rocks' positions are ", rocksPos)
	print("And the pressure pads' positions are ", pressurePos)
	return Grid(m, n, robotPos, teleportalPos, unmovablesPos, rocksPos, pressurePos);

GenGrid()