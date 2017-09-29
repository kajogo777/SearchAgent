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
    def __init__(self, state, parent, operator, depth, path_cost):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.path_cost = path_cost

# general search
def general_search(problem, q_function):
    queue = [ Node(problem.initial_state, None, None, 0, 0) ]

    while True:
        if(len(queue) == 0):
            return None

        node = queue[0]
        del queue[0]

        if(problem.goal_test(node.state)):
            return node

        queue = q_function(queue, problem.state_space(node, problem.actions))



# search strategies

# uniform cost search f(n) = g(n)
def uniform_cost_search(queue, node_list):
    new_queue = queue + node_list
    return sorted(new_queue, key=lambda x: x.path_cost)

# general greedy f(n) = h(n)
def general_greedy(queue, node_list, cost_function):
    new_queue = queue + node_list
    return sorted(new_queue, key=lambda x: cost_function(x.state))

# A star f(n) = g(n)+h(n)
def general_a_star(queue, node_list, cost_function):
    new_queue = queue + node_list
    return sorted(new_queue, key=lambda x: x.path_cost + cost_function(x.state))
