import numpy as np
from operator import attrgetter

OPERATION_DOWN = 'DOLE'
OPERATION_UP = 'HORE'
OPERATION_LEFT = 'VLAVO'
OPERATION_RIGHT = 'VPRAVO'


class Node:
    def __init__(self, matrix: np.array, parent, last_operator: str, heuristic_value: int) -> None:
        self.matrix = np.array(matrix)
        self.parent = parent
        self.last_operator = last_operator
        self.heuristic_value = heuristic_value


class Hashmaps:
    processed_nodes = {}
    unprocessed_nodes = {}

    def _create_hash_from_matrix(self, matrix: np.array) -> str:
        hash = ''
        for _ in matrix:
            for element in _:
                hash += element
        return hash

    def add_processed(self, node: Node) -> None:
        hash = self._create_hash_from_matrix(node.matrix)
        self.processed_nodes[hash] = Node

    def check_processed(self, node: Node) -> bool:
        hash = self._create_hash_from_matrix(node.matrix)
        if self.processed_nodes.get(hash) is None:
            return False
        else:
            return True

    def add_unprocessed(self, node: Node) -> None:
        hash = self._create_hash_from_matrix(node.matrix)
        self.unprocessed_nodes[hash] = node

    def get_processed(self, node: Node) -> None:
        hash = self._create_hash_from_matrix(node.matrix)
        return self.processed_nodes.get(hash)

    def find_best_next_node(self) -> Node:
        lowest_heuristic_node = min(self.unprocessed_nodes.values(), key=attrgetter('heuristic_value'))
        hash = self._create_hash_from_matrix(lowest_heuristic_node.matrix)
        self.unprocessed_nodes.pop(hash)
        return lowest_heuristic_node


class Helper:

    def __init__(self, end_matrix: np.array, hashmaps: Hashmaps) -> None:
        self.hashmaps = hashmaps
        self.end = end_matrix

    def calc_heuristic(self, current_matrix: np.array) -> int:
        heuristic = 0
        for i in range(len(current_matrix)):
            for j in range(len(current_matrix)):
                if current_matrix[i][j] != self.end[i][j]:
                    heuristic += 1
        return heuristic

    def find_possible_operators(self, matrix: np.array) -> list:
        possible_operators = []
        x = len(matrix[0]) - 1
        y = len(matrix) - 1
        index_y, index_x = np.where(matrix == 'm')
        if index_x + 1 <= x:
            possible_operators.append(OPERATION_LEFT)
        if index_x - 1 >= 0:
            possible_operators.append(OPERATION_RIGHT)
        if index_y + 1 <= y:
            possible_operators.append(OPERATION_UP)
        if index_y - 1 >= 0:
            possible_operators.append(OPERATION_DOWN)
        return possible_operators

    def create_node(self, matrix: np.array, parent_node: Node, operator_used: str) -> Node:
        node_heuristic = self.calc_heuristic(matrix)
        new_node = Node(matrix, parent_node, operator_used, node_heuristic)
        return new_node

    def create_node_from_operator(self, parent_node: Node, possible_operator: str) -> Node:
        index_y, index_x = np.where(parent_node.matrix == 'm')
        new_matrix = parent_node.matrix.copy()
        if possible_operator == OPERATION_UP:
            new_matrix[index_y[0]][index_x[0]], new_matrix[index_y[0] + 1][index_x[0]] = new_matrix[index_y[0] + 1][
                                                                                             index_x[0]], \
                                                                                         new_matrix[index_y[0]][
                                                                                             index_x[0]]
            return self.create_node(new_matrix, parent_node, OPERATION_UP)
        if possible_operator == OPERATION_DOWN:
            new_matrix[index_y[0]][index_x[0]], new_matrix[index_y[0] - 1][index_x[0]] = new_matrix[index_y[0] - 1][
                                                                                             index_x[0]], \
                                                                                         new_matrix[index_y[0]][
                                                                                             index_x[0]]
            return self.create_node(new_matrix, parent_node, OPERATION_DOWN)

        if possible_operator == OPERATION_LEFT:
            new_matrix[index_y[0]][index_x[0]], new_matrix[index_y[0]][index_x[0] + 1] = new_matrix[index_y[0]][
                                                                                             index_x[0] + 1], \
                                                                                         new_matrix[index_y[0]][
                                                                                             index_x[0]]
            return self.create_node(new_matrix, parent_node, OPERATION_LEFT)
        if possible_operator == OPERATION_RIGHT:
            new_matrix[index_y[0]][index_x[0]], new_matrix[index_y[0]][index_x[0] - 1] = new_matrix[index_y[0]][
                                                                                             index_x[0] - 1], \
                                                                                         new_matrix[index_y[0]][
                                                                                             index_x[0]]
            return self.create_node(new_matrix, parent_node, OPERATION_RIGHT)

    def process_node(self, current_node: Node) -> None:
        possible_operators = self.find_possible_operators(current_node.matrix)
        for i in range(len(possible_operators)):
            children_node = self.create_node_from_operator(current_node, possible_operators[i])
            if self.hashmaps.check_processed(children_node):
                continue
            else:
                self.hashmaps.add_unprocessed(children_node)
        self.hashmaps.add_processed(current_node)


class Puzzle:

    def __init__(self, start: list, end: list) -> None:
        self.start = np.array(start)
        self.end = np.array(end)
        self.hashmaps = Hashmaps()
        self.helper = Helper(self.end, self.hashmaps)
        self.solve()

    def solve(self) -> None:
        root_heuristic = self.helper.calc_heuristic(self.start)

        root_node = Node(self.start, None, "start", root_heuristic)
        self._solve(root_node)

    def _solve(self, current_node: Node) ->None:
        found_solution = True
        while current_node.heuristic_value != 0:
            self.helper.process_node(current_node)
            current_node = self.hashmaps.find_best_next_node()

            if len(self.hashmaps.unprocessed_nodes) == 0:
                found_solution = False
                break
        if found_solution == True:
            solution = self._create_solution(current_node)
        else:
            print("Solution for {} array to move into {} array does not exist!".format(self.start,self.end))

    def _create_solution(self, node : Node) -> list:
        solution = []
        while node.last_operator != 'start':
            solution.insert(0,node.last_operator)
            node = node.parent
        print(solution)


np_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 'm']])
#array2 = np.array([[1, 2, 3], [4, 6, 8], [7, 5, 'm']]) #existuje solution
array2 = np.array([[7,8,6],[5,4,3],[2,'m',1]]) #neexistuje solution
# test_node = Node(np_array, None, 'vlavo', 0)


# helper.create_node_from_operator(test_node, OPERATION_RIGHT, np_array)

# maps = Hashmaps()
# maps._create_hash_from_matrix(np_array)
puzzle = Puzzle(np_array, array2)
