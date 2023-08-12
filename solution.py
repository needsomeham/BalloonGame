import GameBoard as gb


def main_kickoff():
    solution_found = False
    # while not solution_found:
    #



if __name__ == '__main__':
    # build a functioning board to test on!
    correct_tiles = [1, 4, 3, 2, 3, 2, 2, 4, 2, 3, 5, 2, 3, 5, 2, 5, 2, 4,
                     1, 5, 5, 3, 3, 4, 2, 5, 3, 1, 1, 3, 2, 5, 3, 4, 1, 3]
    game = gb.GameBoard(correct_tiles)

    # to demonstrate that these tiles are correct, print the board and test if solved
    print('Loaded Board:')
    game.print_board()
    game.check_solution()

    # now we know it works, shuffle the board
    game.shuffle_board()

    # lets look for a solution :)
    game.check_solution(verbose=True)
    print(f'number of matching cards: {game.num_matching()}')