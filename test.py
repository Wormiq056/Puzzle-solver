from Puzzle import Puzzle
import time
import tracemalloc

EMPTY_TILE = 'm'
HEURISTIC_1 = 1
HEURISTIC_2 = 2


def test1_1():
    start_board = [[EMPTY_TILE, 1, 2], [3, 4, 5]]
    end_board = [[4, EMPTY_TILE, 5], [3, 1, 2]]
    print("***Starting test1_1****\n")
    print("Testing heuristic calculation 1")
    print("Testing for starting board: {} , end board: {}\n".format(start_board, end_board))
    print("SOLUTION:")
    t = time.time()
    tracemalloc.start()
    puzzle = Puzzle(start_board, end_board, HEURISTIC_1)
    memory = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()
    elapsed_time = time.time() - t
    print("\nTEST RESULTS:")
    print("Time it took to find a solution: {} seconds".format(elapsed_time))
    print("Number of processed nodes: {}".format(len(puzzle.hashmaps.processed_nodes)))
    print("Peak memory usage {} KB\n\n ".format(memory / 1024))


def test1_2():
    start_board = [[EMPTY_TILE, 1, 2], [3, 4, 5]]
    end_board = [[4, EMPTY_TILE, 5], [3, 1, 2]]
    print("***Starting test1_2****\n")
    print("Testing heuristic calculation 2")
    print("Testing for starting board: {} , end board: {}\n".format(start_board, end_board))
    print("SOLUTION:")
    t = time.time()
    tracemalloc.start()
    puzzle = Puzzle(start_board, end_board, HEURISTIC_2)
    memory = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()
    elapsed_time = time.time() - t
    print("\nTEST RESULTS:")
    print("Time it took to find a solution: {} seconds".format(elapsed_time))
    print("Number of processed nodes: {}".format(len(puzzle.hashmaps.processed_nodes)))
    print("Peak memory usage {} KB\n\n".format(memory / 1024))


def test2_1():
    start_board = [[EMPTY_TILE, 1, 2, 3], [4, 5, 6, 7]]
    end_board = [[2, 7, 6, 5], [1, 3, EMPTY_TILE, 4]]
    print("***Starting test2_1****\n")
    print("Testing heuristic calculation 1")
    print("Testing for starting board: {} , end board: {}\n".format(start_board, end_board))
    print("SOLUTION:")
    t = time.time()
    tracemalloc.start()
    puzzle = Puzzle(start_board, end_board, HEURISTIC_1)
    memory = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()
    elapsed_time = time.time() - t
    print("\nTEST RESULTS:")
    print("Time it took to find a solution: {} seconds".format(elapsed_time))
    print("Number of processed nodes: {}".format(len(puzzle.hashmaps.processed_nodes)))
    print("Peak memory usage {} KB\n\n".format(memory / 1024))


def test2_2():
    start_board = [[EMPTY_TILE, 1, 2, 3], [4, 5, 6, 7]]
    end_board = [[2, 7, 6, 5], [1, 3, EMPTY_TILE, 4]]
    print("***Starting test2_2****\n")
    print("Testing heuristic calculation 2")
    print("Testing for starting board: {} , end board: {}\n".format(start_board, end_board))
    print("SOLUTION:")
    t = time.time()
    tracemalloc.start()
    puzzle = Puzzle(start_board, end_board, HEURISTIC_2)
    memory = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()
    elapsed_time = time.time() - t
    print("\nTEST RESULTS:")
    print("Time it took to find a solution: {} seconds".format(elapsed_time))
    print("Number of processed nodes: {}".format(len(puzzle.hashmaps.processed_nodes)))
    print("Peak memory usage {} KB\n\n".format(memory / 1024))


def test3_1():
    start_board = [[1, 2, 3], [4, 5, 6], [7, 8, EMPTY_TILE]]
    end_board = [[7, 8, 6], [5, 4, 3], [2, EMPTY_TILE, 1]]
    print("***Starting test3_1****\n")
    print("Testing heuristic calculation 1")
    print("Testing for starting board: {} , end board: {}\n".format(start_board, end_board))
    print("SOLUTION:")
    t = time.time()
    tracemalloc.start()
    puzzle = Puzzle(start_board, end_board, HEURISTIC_1)
    memory = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()
    elapsed_time = time.time() - t
    print("\nTEST RESULTS:")
    print("Time it took to find a solution: {} seconds".format(elapsed_time))
    print("Number of processed nodes: {}".format(len(puzzle.hashmaps.processed_nodes)))
    print("Peak memory usage {} KB\n\n".format(memory / 1024))


def test3_2():
    start_board = [[1, 2, 3], [4, 5, 6], [7, 8, EMPTY_TILE]]
    end_board = [[7, 8, 6], [5, 4, 3], [2, EMPTY_TILE, 1]]
    print("***Starting test3_2****\n")
    print("Testing heuristic calculation 2")
    print("Testing for starting board: {} , end board: {}\n".format(start_board, end_board))
    print("SOLUTION:")
    t = time.time()
    tracemalloc.start()
    puzzle = Puzzle(start_board, end_board, HEURISTIC_2)
    memory = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()
    elapsed_time = time.time() - t
    print("\nTEST RESULTS:")
    print("Time it took to find a solution: {} seconds".format(elapsed_time))
    print("Number of processed nodes: {}".format(len(puzzle.hashmaps.processed_nodes)))
    print("Peak memory usage {} KB\n\n".format(memory / 1024))


def test4_1():
    start_board = [[EMPTY_TILE, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
    end_board = [[4, 2, 5, EMPTY_TILE, 7], [9, 3, 8, 1, 6]]
    print("***Starting test4_1****\n")
    print("Testing heuristic calculation 1")
    print("Testing for starting board: {} , end board: {}\n".format(start_board, end_board))
    print("SOLUTION:")
    t = time.time()
    tracemalloc.start()
    puzzle = Puzzle(start_board, end_board, HEURISTIC_1)
    memory = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()
    elapsed_time = time.time() - t
    print("\nTEST RESULTS:")
    print("Time it took to find a solution: {} seconds".format(elapsed_time))
    print("Number of processed nodes: {}".format(len(puzzle.hashmaps.processed_nodes)))
    print("Peak memory usage {} KB\n\n".format(memory / 1024))


def test4_2():
    start_board = [[EMPTY_TILE, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
    end_board = [[4, 2, 5, EMPTY_TILE, 7], [9, 3, 8, 1, 6]]
    print("***Starting test4_2****\n")
    print("Testing heuristic calculation 2")
    print("Testing for starting board: {} , end board: {}\n".format(start_board, end_board))
    print("SOLUTION:")
    t = time.time()
    tracemalloc.start()
    puzzle = Puzzle(start_board, end_board, HEURISTIC_2)
    memory = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()
    elapsed_time = time.time() - t
    print("\nTEST RESULTS:")
    print("Time it took to find a solution: {} seconds".format(elapsed_time))
    print("Number of processed nodes: {}".format(len(puzzle.hashmaps.processed_nodes)))
    print("Peak memory usage {} KB\n\n".format(memory / 1024))


def test5_1():
    start_board = [[EMPTY_TILE, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
    end_board = [[7, 1, 4, 6], [2, 3, EMPTY_TILE, 11], [10, 9, 8, 5]]
    print("***Starting test5_1****\n")
    print("Testing heuristic calculation 1")
    print("Testing for starting board: {} , end board: {}\n".format(start_board, end_board))
    print("SOLUTION:")
    t = time.time()
    tracemalloc.start()
    puzzle = Puzzle(start_board, end_board, HEURISTIC_1)
    memory = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()
    elapsed_time = time.time() - t
    print("\nTEST RESULTS:")
    print("Time it took to find a solution: {} seconds".format(elapsed_time))
    print("Number of processed nodes: {}".format(len(puzzle.hashmaps.processed_nodes)))
    print("Peak memory usage {} KB\n\n".format(memory / 1024))


def test5_2():
    start_board = [[EMPTY_TILE, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
    end_board = [[7, 1, 4, 6], [2, 3, EMPTY_TILE, 11], [10, 9, 8, 5]]
    print("***Starting test5_2****\n")
    print("Testing heuristic calculation 2")
    print("Testing for starting board: {} , end board: {}\n".format(start_board, end_board))
    print("SOLUTION:")
    t = time.time()
    tracemalloc.start()
    puzzle = Puzzle(start_board, end_board, HEURISTIC_2)
    memory = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()
    elapsed_time = time.time() - t
    print("\nTEST RESULTS:")
    print("Time it took to find a solution: {} seconds".format(elapsed_time))
    print("Number of processed nodes: {}".format(len(puzzle.hashmaps.processed_nodes)))
    print("Peak memory usage {} KB\n\n".format(memory / 1024))


def test6_1():
    start_board = [[EMPTY_TILE, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]]
    end_board = [[4, EMPTY_TILE, 9, 11, 10, 8], [3, 5, 2, 1, 6, 7]]
    print("***Starting test6_1****\n")
    print("Testing heuristic calculation 1")
    print("Testing for starting board: {} , end board: {}\n".format(start_board, end_board))
    print("SOLUTION:")
    t = time.time()
    tracemalloc.start()
    puzzle = Puzzle(start_board, end_board, HEURISTIC_1)
    memory = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()
    elapsed_time = time.time() - t
    print("\nTEST RESULTS:")
    print("Time it took to find a solution: {} seconds".format(elapsed_time))
    print("Number of processed nodes: {}".format(len(puzzle.hashmaps.processed_nodes)))
    print("Peak memory usage {} KB\n\n".format(memory / 1024))


def test6_2():
    start_board = [[EMPTY_TILE, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]]
    end_board = [[4, EMPTY_TILE, 9, 11, 10, 8], [3, 5, 2, 1, 6, 7]]
    print("***Starting test6_2****\n")
    print("Testing heuristic calculation 2")
    print("Testing for starting board: {} , end board: {}\n".format(start_board, end_board))
    print("SOLUTION:")
    t = time.time()
    tracemalloc.start()
    puzzle = Puzzle(start_board, end_board, HEURISTIC_2)
    memory = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()
    elapsed_time = time.time() - t
    print("\nTEST RESULTS:")
    print("Time it took to find a solution: {} seconds".format(elapsed_time))
    print("Number of processed nodes: {}".format(len(puzzle.hashmaps.processed_nodes)))
    print("Peak memory usage {} KB\n\n".format(memory / 1024))


def start_testing():
    test1_1()
    test1_2()
    test2_1()
    test2_2()
    #test3_1()
    #test3_2()
    test4_1()
    test4_2()
    test5_1()
    test5_2()
    test6_1()
    test6_2()


if __name__ == '__main__':
    start_testing()
