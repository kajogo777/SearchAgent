from random import *
import pygame
import numpy as np
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
	m = randint(5,10)
	n = randint(5,10)

	#R2D2
	robotPos = (randint(0, m-1), randint(0, n-1))

	#Teleportal
	teleportalPos = (randint(0, m-1), randint(0, n-1))

	#Unmovable Objects
	unmovableNum = randint(1, max(m,n))
	unmovablesPos = []

	for i in range(1, unmovableNum):
		currUnmovable = (randint(0, m-1), randint(0, n-1))
		#if occupied pick another one
		while ((currUnmovable in unmovablesPos) or (currUnmovable == teleportalPos) or (currUnmovable == robotPos)):
			currUnmovable = (randint(0, m-1), randint(0, n-1))
		unmovablesPos.append(currUnmovable)

	#Rocks & Pressure Pads
	rocksNum = randint(1, max(m,n)) #Same no. of pressure pads
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

def VisualizeGrid():

	#Generate new grid
	grid = GenGrid()

	# Init Game
	pygame.init()
	screen_width = 1000;
	screen_height = 1000;
	game = pygame.display.set_mode((screen_width ,screen_height)) #Init window
	pygame.display.set_caption('Search Agent') # Title
	clock = pygame.time.Clock() # Handling FPS
	FPS = 60
	game_ended = False # For exiting game

	# Colors
	WHITE = (255, 255 , 255)
	BLACK = (0, 0 ,0)

	# Cell coordinates
	cell_width = int(screen_width / grid.m)
	cell_height = int(screen_height / grid.n)
	cells_spacing = 1 # 1px spacing bet. cells
	cell_padding = 20 # 20px padding inside cell

	# Load Images
	images_paths = ['rock', 'pad-off', 'pad-on', 'portal', 'r2-d2', 'unmovable']
	images = {} # List of imported images
	for image_name in images_paths:
		img = pygame.image.load('assets/'+ image_name + '.png') # Import image
		img = pygame.transform.scale(img, (cell_width - cell_padding, cell_height - cell_padding))  # Rescale to fit cell
		images[image_name] = img # Add to dictionary

	# Game Loop
	while not game_ended:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # End Game
				game_ended = True
			if event.type == pygame.KEYDOWN: # Keyboard Input
				if event.key == pygame.K_s:
					print('pressed')

		# Draw Frame
		game.fill(BLACK) # Background

		#Draw Grid
		for x in np.arange(0, screen_width, cell_width, dtype = int):
			for y in np.arange(0, screen_height, cell_height, dtype = int):
				new_rectangle = pygame.Rect(x + cells_spacing, y + cells_spacing, cell_width - cells_spacing, cell_height - cells_spacing)
				pygame.draw.rect(game, WHITE, new_rectangle)

		# Generic drawing of game objects
		def PlaceObject(x, y, type):
			game.blit(images[type], (x * cell_width + cell_padding / 2, y * cell_height + cell_padding / 2))

		game_objects = [([grid.robotPos],'r2-d2'), ([grid.teleportalPos],'portal'), (grid.unmovables,'unmovable'), (grid.pressurePos,'pad-off'), (grid.rocksPos,'rock')]
		#Draw Objects
		for obj in game_objects:
			for (x, y) in obj[0]:
				PlaceObject(x, y, obj[1])

		pygame.display.update() # Display frame
		clock.tick(FPS) # Updating by 60 FPS

	# Close Window
	pygame.quit()
	quit()

VisualizeGrid()
