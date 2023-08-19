import heapq, random, time
import GameBoard as gb


def find_me_a_solution(game:gb) -> bool:
    """
    Greedy Algo Strategy:
    - Take top board from heap queue.
    - Generate 10 random boards from top board and add children to priority heap following rules:
        - Sawp two tiles that do not have solved edges.
        - Rotate one tile 90 degrees that does not have solved edges.
        - Do not add child to queue if already seen.
    - Repeat
    """

    print("\n\n"
          "--------------------------------------\n"
          "Looking for solution to shuffled board")
    start_time = time.perf_counter()
    counter = 0
    num_solutions_found = 0
    all_edges_tuple = [(0,1), (0,3), (1,2), (1,4), (2,5), (3,4), (3,6), (4,5), (4,7), (5,8), (6,7), (7,8)]
    edges_set = set(sum(all_edges_tuple, ()))
    cache_ids = {}
    # pythons heap queue is dumb and only gives the min, so negate to get max :/
    heap_queue = [(-game.score, game.get_id())]
    heapq.heapify(heap_queue)


    while True:
        # pick top scoring board to work with
        working_score, working_id = heapq.heappop(heap_queue)
        id_list = [int(x) for x in working_id]
        working_game = gb.GameBoard(id_list)

        # find tiles that do not have a matching edge
        board_edges_tuples = [k for k, v in working_game.matching_edges.items() if v is True]
        board_edges_reduced = set(sum(board_edges_tuples, ()))
        not_used = list(edges_set.difference(board_edges_reduced))

        # make 10 random permutations on the board and add their children to the queue
        for i in range(10):
            old_game = gb.GameBoard(id_list)

            # False - rotate, True - swap two tiles
            rand = not not random.getrandbits(1)
            if not rand:
                old_game.rotate_tile(random.choice(not_used), not not random.getrandbits(1))
            else:
                tile1, tile2 = random.sample(not_used, 2)
                old_game.swap_two_tiles(tile1, tile2)

            permuted_id = old_game.get_id()
            # check that we have not seen the board before
            if cache_ids.get(permuted_id) is not None:
                continue
            if old_game.check_solution():
                num_solutions_found += 1
                cache_ids[permuted_id] = True
                print(f"Solution found after {counter} iterations checked.")
                print(f"Total number of solutions found {num_solutions_found}.")
                print(f"Solved board:")
                old_game.print_board()
                if permuted_id != starting_tiles_str:
                    print(f"Solution does not match starting tiles, continuing to search for starting tile array.\n")
                else:
                    print(f"Found tile array matching starting solution!")
                    print(f"Total time algo ran: {time.perf_counter() - start_time}s")
                    return True
            else:
                cache_ids[permuted_id] = True
                permuted_score = old_game.score
                heapq.heappush(heap_queue, (-permuted_score, permuted_id))

            counter += 1


if __name__ == '__main__':
    # build a functioning board to test on!
    starting_tiles = [1, 4, 3, 2, 3, 2, 2, 4, 2, 3, 5, 2, 3, 5, 2, 5, 2, 4,
                     1, 5, 5, 3, 3, 4, 2, 5, 3, 1, 1, 3, 2, 5, 3, 4, 1, 3]

    global starting_tiles_str
    starting_tiles_str = ""
    for num in starting_tiles:
        starting_tiles_str += str(num)

    print(starting_tiles_str)
    game = gb.GameBoard(starting_tiles)


    # to demonstrate that these tiles are correct, print the board and test if solved
    print('Loaded Board:')
    game.print_board()
    game.check_solution()

    # now we know it works, shuffle the board
    game.shuffle_board()

    # check that shuffle is not a solution
    game.check_solution(verbose=True)
    print(f'number of matching cards: {game.score}')

    # find a solution
    find_me_a_solution(game)
