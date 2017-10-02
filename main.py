def main():
	#Generate new grid
	grid = GenGrid()

    # Types of search
    types_func = {'BF': breadth_first_search,
                  'DF': depth_first_search,
                  'ID': iterative_deepening_search,
                  'UC': uniform_cost_search,
                  'GR1': greedy_h1,
                  'GR2': greedy_h2,
                  'AS1': a_star_h1,
                  'AS2': a_star_h2}

    # Start Searching
    Search(grid, types_func['BF'], True)

# Run main for testing
main()

def Search(grid , strategy, visualize):
    # Instantiate the search problem
    search_problem = HelpR2D2(grid.m, grid.n, grid.robotPos,
                    grid.rocksPos, grid.pressurePos,
                    grid.unmovables, grid.teleportalPos)

    # Start searching
    node = general_search(search_problem, strategy)

    # Return a list of : path list, path cost, no. of nodes while searching
