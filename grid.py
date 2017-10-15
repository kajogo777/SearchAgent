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

	#Base
	m = randint(3,6)
	n = randint(3,6)

	#R2D2
	robotPos = (randint(0, m-1), randint(0, n-1))

	#Teleportal
	teleportalPos = (randint(0, m-1), randint(0, n-1))

	#Unmovable Objects
	unmovableNum = randint(1, max(m,n))
	unmovablesPos = []

	for i in range(0, unmovableNum):
		currUnmovable = (randint(0, m-1), randint(0, n-1))
		#if occupied pick another one
		while ((currUnmovable in unmovablesPos) or (currUnmovable == teleportalPos) or (currUnmovable == robotPos)):
			currUnmovable = (randint(0, m-1), randint(0, n-1))
		unmovablesPos.append(currUnmovable)

	#Rocks & Pressure Pads
	rocksNum = randint(1, max(m,n)) #Same no. of pressure pads
	rocksPos = []
	pressurePos = []

	for j in range(0, rocksNum):
		currRock = (randint(0,m-1), randint(0,n-1))
		currPressure = (randint(0,m-1), randint(0,n-1))

		while ((currPressure in pressurePos) or (currPressure in unmovablesPos) or (currPressure == teleportalPos)):
			currPressure = (randint(0,m-1), randint(0,n-1))

		pressurePos.append(currPressure)

		while ((currRock in rocksPos) or (currRock in unmovablesPos) or (currRock in pressurePos) or (currRock == teleportalPos) or (currRock == robotPos)):
			currRock = (randint(0,m-1), randint(0,n-1))

		rocksPos.append(currRock)

	#Testing
	print("m = ",m)
	print("n = ", n)
	print("The robot is at ", robotPos)
	print("Teleportal is at ", teleportalPos)
	print("There is unmovable objects at ", unmovablesPos)
	print("The rocks' positions are ", rocksPos)
	print("And the pressure pads' positions are ", pressurePos)

	#Generate a grid object
	return Grid(m, n, robotPos, teleportalPos, unmovablesPos, rocksPos, pressurePos);
