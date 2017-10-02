# search problem ADT
class SearchProblem:
    def __init__(self, operators, initial_state, state_space, goal_test, path_cost):
        self.actions = operators
        self.initial_state = initial_state
        self.state_space = state_space
        self.goal_test = goal_test
        self.path_cost = path_cost

# node ADT
class Node:
    def __init__(self, state, parent, operator, depth, path_cost, path_list):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.path_cost = path_cost
        self.path_list = path_list
