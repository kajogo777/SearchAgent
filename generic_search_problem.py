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

# breadth first search
def breadth_first_search(queue, node_list):
    return queue + node_list

# depth first search
def depth_first_search(queue, node_list):
    return node_list + queue

# iterative deepening search
def iterative_deepening_search(queue, node_list):
    if len(queue) == 0: # initialize queue magic value and initial state
        root = node_list[0].parent # get root
        initial_l = 1 # set first iterative depth to 1
        queue.append("$")
        queue.append(root) # add root node to end of queue
        queue.append(initial_l) # add iterative depth to end of queue
    elif queue[0] == "$" and len(node_list) == 0: # if queue has magic value at the beginning and no expanded nodes
        return [] # no states left return empty queue

    depth_limit = queue[-1]
    root = queue[-2]
    for node in node_list:
        if node.depth <= depth_limit:
            queue = [node] + queue

    if queue[0] == "$": # if cannot add nodes anymore and queue has the magic value at the beginning
        queue[-1] = depth_limit+1 # increase depth
        queue = [root] + queue # add root to beginning to trigger DFS again

    return queue

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
