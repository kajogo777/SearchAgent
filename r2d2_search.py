import * from general_search_problem

class StateR2D2():
    def __init__(self, position, rock_positions):
        self.position = position # (x,y)
        self.rock_positions = rock_positions # [(x,y,on_point)]

class HelpR2D2(SearchProblem):
    def __init__(self, m, n, position, rocks, pressure_points, unmovables, portal):
        StateR2D2.m = m
        StateR2D2.n = n
        StateR2D2.pressure_points = pressure_points # [(x,y)]
        StateR2D2.unmovables = unmovables # [(x,y)]
        StateR2D2.portal = portal # (x,y)

        self.actions = {"north": 1, "south": 1, "east": 1, "west": 1}
        mapped = map(lambda x: (x[0],x[1],False) ), rocks)
        self.initial_state = StateR2D2(position, list(mapped))
        self.goal_test = goal_test
        self.path_cost = path_cost

# helper methods
    def get_rock(self, position, state):
        index = -1
        for i in range(len(state.rock_positions)):
            if state.rock_positions[i][0] == position[0] and state.rock_positions[i][1] == position[1]:
                index = i
        return index

    def is_obstacle(self, position, state):
        if position[0] >= StateR2D2.m or position[0] < 0 or position[1] >= StateR2D2.n or position[1] < 0:
            return True
        if position in StateR2D2.unmovable:
            return True
        return self.get_rock(position, state) > -1

    def is_pressure_pad(self, position):
        return position in StateR2D2.pressure_points

# state space transition/expanding function
    def state_space(self, node):
        children = []
        directions = [(0,1,"north"), (0,-1,"south"), (1,0,"east"), (-1,0,"west")]
        for action, cost in self.actions.items():
            for direction in directions:
                next_position = (node.state.position[0]+direction[0], node.state.position[1]+direction[1])
                rock = self.get_rock(next_position, node.state)
                if rock > -1: # a rock exists
                    new_rock_position = (next_position[0]+direction[0], next_position[1]+direction[1])
                    if self.is_obstacle(new_rock_position): # if exists obstacle behind rock
                        continue;
                    else:
                        new_rocks = [i for i in self.rock_positions]
                        new_rocks[rock] = (next_position[0] + direction[0], next_position[1] + direction[1], self.is_pressure_pad(new_rock_position))
                        new_state = StateR2D2(next_position, new_rocks)
                        children.append(Node(new_state, node, direction[2], node.depth + 1, node.path_cost + self.actions[direction[2]]))
                elif self.is_obstacle(next_position, node.state): # obstacle, remember rock check redundant
                    continue;


# heuristic functions
    # # minimize rock-pressure pad distance
    # def min_rock_pad(state):
    #     for rock in state.rock_positions:
    #         for

    # # rock first cost function
    # def rock_first(state):
    #     # mode 1 looking for rock + 2*sqrt(m**2 + n**2)
    #     # mode 2 looking for pressure pad + sqrt(m**2 + n**2)
    #     # mode 3 looking for portal + 0
    #     free_rocks = filter(lambda x: not x[2], state.rock_positions)
    #     if free_rocks != []:
    #         best_rock = min(free_rocks, key=lambda rock: math.sqrt((rock[0]-state.position[0])**2+(rock[1]-state.position[1])**2))
    #         d = math.sqrt((best_rock[0]-state.position[0])**2+(best_rock[1]-state.position[1])**2)
    #         if d == 1:
    #         else:
    #             return d
    #     else:
    #         distance_portal = math.sqrt((rock[0]-state.position[0])**2+(rock[1]-state.position[1])**2)
    #
    #     return None
