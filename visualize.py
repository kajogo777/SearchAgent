import pygame
import numpy as np

def Visualize(grid, path_list):

	# Cell coordinates
	cell_size = 100;
	cells_spacing = 1 # 1px spacing bet. cells
	cell_padding = 20 # 20px padding inside cell

	# Init Game
	pygame.init()
	screen_width = grid.m * cell_size;
	screen_height = grid.n * cell_size;
	game = pygame.display.set_mode((screen_width ,screen_height)) #Init window
	pygame.display.set_caption('Search Agent') # Title
	clock = pygame.time.Clock() # Handling FPS
	FPS = 2 # 2 Frames/ Second
	game_ended = False # For exiting game

	# Colors
	WHITE = (253, 253 , 253)
	BLACK = (0, 0 ,0)
	YELLOW = (240,230,140)

	# Load Images
	images_paths = ['rock', 'pad-off', 'pad-on', 'portal', 'r2-d2', 'unmovable']
	images = {} # List of imported images
	for image_name in images_paths:
		img = pygame.image.load('assets/'+ image_name + '.png') # Import image
		img = pygame.transform.smoothscale(img, (cell_size - cell_padding, cell_size - cell_padding))  # Rescale to fit cell
		images[image_name] = img # Add to dictionary

	i = 0
	# Game Loop
	while not game_ended:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # End Game
				game_ended = True
			if event.type == pygame.KEYDOWN: # Keyboard Input
				if event.key == pygame.K_r: # Restart Display if pressed r
					i = 0

		# Get current node
		node = path_list[i]
		if i < (len(path_list) - 1):
			i += 1

		#Change grid
		robotPos = node.state.position
		active_pads = []
		rocks = []
		for rock in node.state.rock_positions:
			if rock[2]: # if rock was on pad
				active_pads.append((rock[0], rock[1]))
			else:
				rocks.append((rock[0], rock[1]))
		# Draw Frame
		game.fill(YELLOW) # Lines color

		# Draw Grid
		for x in np.arange(0, screen_width, cell_size, dtype = int):
			for y in np.arange(0, screen_height, cell_size, dtype = int):
				new_rectangle = pygame.Rect(x + cells_spacing, y + cells_spacing, cell_size - cells_spacing, cell_size - cells_spacing)
				pygame.draw.rect(game, WHITE, new_rectangle) # Draw Cell

		# Generic drawing of game objects
		def PlaceObject(x, y, type):
			game.blit(images[type], (x * cell_size + cell_padding / 2, (grid.n - y - 1) * cell_size + cell_padding / 2))

		# Draw Objects
		game_objects = [(grid.pressurePos,'pad-off'), ([grid.teleportalPos],'portal'), (grid.unmovables,'unmovable'), (rocks,'rock'), ([robotPos],'r2-d2')]
		for idx,obj in enumerate(game_objects):
			for (x, y) in obj[0]:
				#Draw activate pads
				if idx == 0 and (x, y) in active_pads:
					PlaceObject(x, y, 'pad-on')
				else:
					PlaceObject(x, y, obj[1])

		pygame.display.update() # Display frame
		clock.tick(FPS) # for rendering 2 frames/second

	# Close Window
	pygame.quit()
	#quit()
