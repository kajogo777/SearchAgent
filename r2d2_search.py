from generic_search_problem import *

class StateR2D2():
    def __init__(self, position, rock_positions):
        #Defining dynamic state parameters
        self.position = position # (x,y)
        self.rock_positions = rock_positions # [(x,y,on_point)]

class HelpR2D2(SearchProblem):
    # Defining search problem
    def __init__(self, m, n, position, rocks, pressure_points, unmovables, portal):
        # Defining static state parameters
        StateR2D2.m = m
        StateR2D2.n = n
        StateR2D2.pressure_points = pressure_points # [(x,y)]
        StateR2D2.unmovables = unmovables # [(x,y)]
        StateR2D2.portal = portal # (x,y)

        # Problem Operators
        self.actions = {"north": 1, "south": 1, "east": 1, "west": 1}

        # Creating list of rocks not yet placed on the pads
        mapped = map(lambda x: (x[0],x[1],False), rocks)

        # Defining the initial state
        self.initial_state = StateR2D2(position, list(mapped))
        self.path_cost = 0
        self.memoization = []

# goal test function
    def goal_test(self, state):
        test = True
        for rock in state.rock_positions:
            test = test and rock[2]
        test = test and (state.position == StateR2D2.portal)
        return test

# helper methods
    def get_rock_index(self, position, state):
        index = -1
        for i in range(len(state.rock_positions)):
            if state.rock_positions[i][0] == position[0] and state.rock_positions[i][1] == position[1]:
                index = i
        return index # returns -1 if not found else index of current rock in the list

    def is_obstacle(self, position):
        # Check if out of bounds
        if position[0] >= StateR2D2.m or position[0] < 0 or position[1] >= StateR2D2.n or position[1] < 0:
            return True
        # Check if it's a movable object
        if position in StateR2D2.unmovables:
            return True
        # Empty Cell
        return False

    def is_pressure_pad(self, position):
        return position in StateR2D2.pressure_points

# state space transition/expanding function
    def state_space(self, node):
        if node.depth == 0:
            self.memoization = []
        else:
            for state in self.memoization:
                if node.state.position == state.position and node.state.rock_positions == state.rock_positions:
                    return []
        self.memoization.append(node.state)

        children = [] # list of expanded nodes
        directions = [(0,1,"north"), (0,-1,"south"), (1,0,"east"), (-1,0,"west")] # possible movements
        for direction in directions:
            # Next position in a specific direction
            next_position = (node.state.position[0] + direction[0], node.state.position[1] + direction[1])

            # Current state of rocks
            rocks = [i for i in node.state.rock_positions]

            # Check if next position is a rock
            rock_index = self.get_rock_index(next_position, node.state)
            if rock_index > -1: # a rock exists
                new_rock_position = (next_position[0] + direction[0], next_position[1] + direction[1])

                # if exists an obstacle or a rock behind the rock -> don't move
                if self.is_obstacle(new_rock_position) or self.get_rock_index(new_rock_position, node.state) > -1:
                    continue
                # else move rock
                else:
                    # Change rock position + set true if on pressure pad
                    rocks[rock_index] = (next_position[0] + direction[0], next_position[1] + direction[1], self.is_pressure_pad(new_rock_position))
            # else if it's an obstacle -> don't move
            elif self.is_obstacle(next_position):
                continue

            # if rock was movable or empty cell
            # create new state with the new positions of R2-D2 and the rocks
            new_state = StateR2D2(next_position, rocks)

            # create a new node in the specified direction with a new depth while keeping track of path cost and list so far
            new_node = Node(new_state, node, direction[2], node.depth + 1, node.path_cost + self.actions[direction[2]], node.path_list + [node])

            # Optimization : Not repeating states
            # if new_node in node.path_list:
            #     continue

            # add the new node to the expanded list
            children.append(new_node)
        # Return the list of expanded nodes
        return children

# heuristic functions
# helper functions
def get_d(point1, point2):
    dx = point1[0] - point2[0]
    dy = point1[1] - point2[1]
    return abs(dx) + abs(dy)

def get_min_index(point1, arr):
    index = -1
    min_path = StateR2D2.m + StateR2D2.n
    for i in range(len(arr)):
        if(not arr[i][2]):
            d = get_d(point1, arr[i])
            if d < min_path:
                min_path = d
                index = i
    return (index, min_path)

# heuristic 1 : min path
def first_heuristic(state):
    rocks_ignored = []
    rocks = []

    # ignore rocks on pressure pads
    for rock in state.rock_positions:
        if rock[2]:
            rocks_ignored.append((rock[0], rock[1]))
        else:
            rocks.append((rock[0], rock[1], False))

    # if no rocks remained return distance to portal
    if len(rocks) == 0:
        return get_d(state.position, StateR2D2.portal)

    pads = []
    # ignore all activated pressure pads
    for pad in StateR2D2.pressure_points:
        if not pad in rocks_ignored:
            pads.append((pad[0], pad[1], False))

    # remaining objects we need to pass by
    remaining = len(pads) + len(rocks)
    # whether we are looking for closest rock or pad
    look_for_rock = True
    # keeps track of cost so far
    cost = 0
    # start from R2D2 current position
    curr_node = state.position

    while remaining > 0:
        if look_for_rock:
            # find closest rock's index and distance away
            index, min_path = get_min_index(curr_node, rocks)
            # mark rock as visited
            rocks[index] = (rocks[index][0], rocks[index][1], True)
            # next iteration measure distance from this rock
            curr_node = rocks[index]
            # add distance to cost
            cost = cost + min_path
        else:
            # find closest pad's index and distance away
            index, min_path = get_min_index(curr_node, pads)
            # mark pad as visited/ctivated
            pads[index] = (pads[index][0], pads[index][1], True)
            # next iteration measure distance from this pad
            curr_node = pads[index]
            # add distance to cost
            cost = cost + min_path
        # decrement number of remaining objects
        remaining = remaining - 1
        # if we were looking for a rock then look for a pad next and vice versa
        look_for_rock = not look_for_rock

    # when done with planning routes, add the distance to the portal from the last object visited
    cost = cost + get_d(curr_node, StateR2D2.portal)
    return cost

#Heuristic 2
def second_heuristic(state):
    # Generate a list of unactivated pads
    pressure_pads = list(map(lambda pad : (pad[0], pad[1], False), state.pressure_points))

    #looping on the rocks
    sum_distances = 0
    for rock in state.rock_positions:
        index, path = get_min_index(rock, pressure_pads)
        pressure_pads[index] = (pressure_pads[index][0], pressure_pads[index][1], True)
        sum_distances += path

    cost = sum_distances
    return cost

# A star search with 1st heuristic
def a_star_h1(queue, node_list):
    return general_a_star(queue, node_list, first_heuristic)

# A star search with 2nd heuristic
def a_star_h2(queue, node_list):
    return general_a_star(queue, node_list, second_heuristic)

# Greedy search with 1st heuristic
def greedy_h1(queue, node_list):
    return general_greedy(queue, node_list, first_heuristic)

# Greedy search with 2nd heuristic
def greedy_h2(queue, node_list):
    return general_greedy(queue, node_list, second_heuristic)
