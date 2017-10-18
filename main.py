from grid import *
from generic_search_problem import *
from r2d2_search import *
from visualize import *

def main():
    #Generate new grid
    grid = GenGrid()

    # grid.m = 5
    # grid.n = 5
    # grid.robotPos = (3,1)
    # grid.teleportalPos = (3,2)
    # grid.unmovables = [(2,1)]
    # grid.rocksPos = [(1,3), (1,1), (3,3), (2,3)]
    # grid.pressurePos = [(2,4), (2,2), (3,0), (0,0)]

    # Take user input for either visualizing or not
    visualize = True if input("With Visualization ? Y/N : ") == 'Y' else False

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

    # Testing everything at once
    names = sorted(strategies.items(), key=lambda x: x[0])
    for name, strategy in names:
        print('Running ' + name)
        test = Search(grid, strategy, visualize)
        print("Algorithm: %s,\npath = %s,\ncost = %s,\nExpanded %s nodes\n" % (name, test[0] if len(test[0]) > 0 else 'No Solution', test[1], test[2]))

def Search(grid , strategy, visualize):

    # Create the search problem
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

    else: # If no solution found
        return ([], None, search_length)

# Run main for testing
main()

# Samples
    #Sample grid
    # grid.m = 5
    # grid.n = 4
    # grid.robotPos = (3,1)
    # grid.teleportalPos = (3,1)
    # grid.unmovables = [(1,2), (4,2), (3,3), (3,0), (4,1)]
    # grid.rocksPos = [(0,2)]
    # grid.pressurePos = [(0,3)]

    # Stuck scenario
    # grid.m = 4
    # grid.n = 3
    # grid.robotPos = (2,0)
    # grid.teleportalPos = (0,1)
    # grid.unmovables = [(3,0), (0,0), (2,1)]
    # grid.rocksPos = [(2,2), (1,0), (3,1), (1,1)]
    # grid.pressurePos = [(0,2), (3,2), (1,2), (2,2)]
