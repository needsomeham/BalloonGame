import random


class Tile:
    """
    An individual tile:
     _ _ _ _
    |   1   |
    | 4   2 |
    |   3   |
     _ _ _ _

    Where positions correlate with numbers as follows:
    1: Top
    2: Right
    3: Bottom
    4: Left

    A right (clockwise) rotation yields:
     _ _ _ _
    |   4   |
    | 3   1 |
    |   2   |
     _ _ _ _

     A left (counterclockwise) rotation yields:
     _ _ _ _
    |   2   |
    | 1   3 |
    |   4   |
     _ _ _ _

    """

    def __init__(self, balloons: list):
        self.top = balloons[0]
        self.right = balloons[1]
        self.bottom = balloons[2]
        self.left = balloons[3]

    def rotate_right(self) -> None:
        temp_top = self.top
        self.top = self.left
        self.left = self.bottom
        self.bottom = self.right
        self.right = temp_top

    def rotate_left(self) -> None:
        temp_top = self.top
        self.top = self.right
        self.right = self.bottom
        self.bottom = self.left
        self.left = temp_top

    def print_tile(self) -> None:
        print("  _ _ _ _  ")
        print(f" |   {self.top}   | ")
        print(f" | {self.left}   {self.right} | ")
        print(f" |   {self.bottom}   | ")
        print("  _ _ _ _  ")

    def str_list(self) -> list:
        """
        :return: list of strings from top to bottom of tile
        """
        full = []
        full.append("  _ _ _ _  ")
        full.append(f" |   {self.top}   | ")
        full.append(f" | {self.left}   {self.right} | ")
        full.append(f" |   {self.bottom}   | ")
        full.append("  _ _ _ _  ")
        return full


class GameBoard:
    def __init__(self, balloons: list):
        """
        Game board class to hold 9 tiles and related functionality.
        A solved board consists of 9 tiles where each of their internal edges match with their neighbor:
         _ _ _ _   _ _ _ _   _ _ _ _
        |   1   | |   3   | |   2   |
        | 2   4 | | 4   2 | | 2   3 |
        |   3   | |   2   | |   5   |
         _ _ _ _   _ _ _ _   _ _ _ _
         _ _ _ _   _ _ _ _   _ _ _ _
        |   3   | |   2   | |   5   |
        | 5   5 | | 5   4 | | 4   3 |
        |   2   | |   1   | |   3   |
         _ _ _ _   _ _ _ _   _ _ _ _
         _ _ _ _   _ _ _ _   _ _ _ _
        |   2   | |   1   | |   3   |
        | 1   5 | | 5   3 | | 3   4 |
        |   3   | |   2   | |   1   |
         _ _ _ _   _ _ _ _   _ _ _ _

        Balloons from board above are loaded as follows:
        [1,4,3,2, 3,2,2,4, 2,3,5,2, 3,5,2,5, 2,4,1,5, 5,3,3,4, 2,5,3,1, 1,3,2,5, 3,4,1,3]
        Where the first four ints represent the first tile moving clockwise around the tile.
        Second four ints represent the second tile moving clockwise around that tile.
        So on.

        Positions of tiles are:
         _ _ _ _   _ _ _ _   _ _ _ _
        |       | |       | |       |
        |   0   | |   1   | |   2   |
        |       | |       | |       |
         _ _ _ _   _ _ _ _   _ _ _ _
         _ _ _ _   _ _ _ _   _ _ _ _
        |       | |       | |       |
        |   3   | |   4   | |   5   |
        |       | |       | |       |
         _ _ _ _   _ _ _ _   _ _ _ _
         _ _ _ _   _ _ _ _   _ _ _ _
        |       | |       | |       |
        |   6   | |   7   | |   8   |
        |       | |       | |       |
         _ _ _ _   _ _ _ _   _ _ _ _

        :param balloons: 1d list of balloons by tile, top left to bottom right, of order: top, right, bottom, left
        """

        # generate tiles
        self.tiles = []
        for i in range(9):
            self.tiles.append(Tile(balloons[(i*4):(i*4+4)]))

    def print_board(self) -> None:
        all_str_tiles = [self.tiles[i].str_list() for i in range(9)]
        for outer in range(3):
            for inner in range(5):
                print(all_str_tiles[outer * 3][inner],
                      all_str_tiles[outer * 3 + 1][inner],
                      all_str_tiles[outer * 3 + 2][inner])

    def shuffle_board(self) -> None:
        """
        Randomly makes 50 tile swaps and 100 tile rotations, effectively mixing the board up.
        :return: None
        """

        print('\nShuffling Board')
        tile_locations = [i for i in range(9)]
        for i in range(50):
            tile1 = random.choice(tile_locations)
            tile2 = random.choice(tile_locations)
            self.swap_two_tiles(tile1, tile2)
            direction1 = random.choice([True, False])
            direction2 = random.choice([True, False])
            self.rotate_tile(tile1, direction1)
            self.rotate_tile(tile2, direction2)
        print('Board after shuffling:')
        self.print_board()

    def swap_two_tiles(self, tile1: int, tile2: int) -> None:
        """
        Given two tiles, swap them on the game board.
        :param tile1: int location of tile one
        :param tile2: int location of title two
        :return:
        """
        self.tiles[tile1], self.tiles[tile2] = self.tiles[tile2], self.tiles[tile1]

    def rotate_tile(self, tile: int, right: bool) -> None:
        """
        Rotate a given tile left (counterclockwise) or right (clockwise).

        :param tile: int location of tile
        :param right: True is to rotate right. False if desired to rotate left.
        :return: None
        """
        if right:
            self.tiles[tile].rotate_right()
        else:
            self.tiles[tile].rotate_left()

    def num_matching(self) -> int:
        """
        Calculates the numer of matching tiles on the board.
        A single matching edge is defined as sharing a common number:
         _ _ _ _   _ _ _ _
        |   3   | |   3   |
        | 5   5 | | 5   2 |
        |   2   | |   2   |
         _ _ _ _   _ _ _ _

        :return: number of matching tile edges
        """
        # check edges between 1-2, 1-4, 2-3, 2-5, 3-6, 4-5, 4-7, 5-6, 5-8, 6-9, 7-8, 8-9
        # could be written much more succinctly, but idc rn

        num_correct = 0

        # 1-2
        if self.tiles[0].right == self.tiles[1].left:
            num_correct += 1
        # 1-4
        if self.tiles[0].bottom == self.tiles[3].top:
            num_correct += 1
        # 2-3
        if self.tiles[1].right == self.tiles[2].left:
            num_correct += 1
        # 2-5
        if self.tiles[1].bottom == self.tiles[4].top:
            num_correct += 1
        # 3-6
        if self.tiles[2].bottom == self.tiles[5].top:
            num_correct += 1
        # 4-5
        if self.tiles[3].right == self.tiles[4].left:
            num_correct += 1
        # 4-7
        if self.tiles[3].bottom == self.tiles[6].top:
            num_correct += 1
        # 5-6
        if self.tiles[4].right == self.tiles[5].left:
            num_correct += 1
        # 5-8
        if self.tiles[4].bottom == self.tiles[7].top:
            num_correct += 1
        # 6-9
        if self.tiles[5].bottom == self.tiles[8].top:
            num_correct += 1
        # 7-8
        if self.tiles[6].right == self.tiles[7].left:
            num_correct += 1
        # 8-9
        if self.tiles[7].right == self.tiles[8].left:
            num_correct += 1

        return num_correct

    def check_solution(self, verbose=False) -> bool:
        """
        If all 12 internal edges are matching, the game is solved!
        :param verbose: (optional) if print message "no solution"
        :return: bool - solved or not
        """

        if self.num_matching() == 12:
            print('Solution Found!\n')
            return True
        if verbose:
            print('Not a solution.\n')
        return False


if __name__ == "__main__":
    # internal testing

    print('Testing on bad board:')
    scrambled_tiles = [random.choice([1,2,3,4,5]) for i in range(36)]
    bad_board = GameBoard(scrambled_tiles)
    bad_board.print_board()
    print(f'number of matching tiles: {bad_board.num_matching()}')
    bad_board.check_solution(verbose=True)

    print('Testing on correct board')
    correct_tiles = [1,4,3,2, 3,2,2,4, 2,3,5,2, 3,5,2,5, 2,4,1,5, 5,3,3,4, 2,5,3,1, 1,3,2,5, 3,4,1,3]
    correct_board = GameBoard(correct_tiles)
    correct_board.print_board()
    print(f'number of matching tiles: {correct_board.num_matching()}')
    correct_board.check_solution(verbose=True)

    print('shuffling correct board')
    correct_board.shuffle_board()
    print(f'number of matching tiles: {correct_board.num_matching()}')
    correct_board.check_solution(verbose=True)



