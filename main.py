from grid import *
from generic_search_problem import *
from r2d2_search import *
from visualize import *

def main():
    #Generate new grid
    grid = GenGrid()

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

    # Start Searching
    bfs_test = Search(grid, strategies['GR1'], True)

    print(bfs_test)

def Search(grid , strategy, visualize):
    # Instantiate the search problem
    # search_problem = HelpR2D2(grid.m, grid.n, grid.robotPos,
    #                 grid.rocksPos, grid.pressurePos,
    #                 grid.unmovables, grid.teleportalPos)

    search_problem = HelpR2D2(
                    4,
                    4,
                    (0,0),
                    [(1,2), (2,0)],
                    [(2,2), (3,0)],
                    [],
                    (3,3))

    #Visualize(grid)
    # Start searching
    (goal_node, search_length) = general_search(search_problem, strategy)

    # Visualize if required to: TODO
    #Visualize(grid)

    # Return a list of : (path to goal, total cost to goal, no. of nodes while searching)
    return ((goal_node.path_list + [goal_node]) if goal_node else None, goal_node.path_cost, search_length)

# Run main for testing
main()
