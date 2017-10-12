from grid import *
from generic_search_problem import *
from r2d2_search import *
from visualize import *

def main():
    #Generate new grid
    grid = GenGrid()

    #Sample grid
    # grid.m = 5
    # grid.n = 4
    # grid.robotPos = (3,1)
    # grid.teleportalPos = (3,1)
    # grid.unmovables = [(1,2), (4,2), (3,3), (3,0), (4,1)]
    # grid.rocksPos = [(0,2)]
    # grid.pressurePos = [(0,3)]

    # Types of search
    strategies = {
        'BF': breadth_first_search,
        'DF': depth_first_search,
        'ID': iterative_deepening_search,
        'UC': uniform_cost_search,
        'GR1': greedy_h1,
        'GR2': greedy_h2,
        'AS1': a_star_h1,
        'AS2': a_star_h2
    }
    names = sorted(strategies.items(), key=lambda x: x[0])
    for name, strategy in names:
        test = Search(grid, strategy, True)
        print("path = %s %s, cost = %s, %s nodes" % (name, test[0], test[1], test[2]))

def Search(grid , strategy, visualize):

    # Instantiate the search problem
    search_problem = HelpR2D2(grid.m, grid.n, grid.robotPos,
                    grid.rocksPos, grid.pressurePos,
                    grid.unmovables, grid.teleportalPos)

    # Start searching
    (goal_node, search_length) = general_search(search_problem, strategy)

    # Return a list of : (path to goal, total cost to goal, no. of nodes while searching)
    if goal_node:
        path_list = goal_node.path_list + [goal_node]
        # Visualize if required to:
        if visualize:
            Visualize(grid, path_list)
        return (path_list, goal_node.path_cost, search_length)

    else:
        return ([], None, search_length)
# Run main for testing
main()
