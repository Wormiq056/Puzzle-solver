import numpy as np
from hashlib import sha256
from operator import attrgetter

OPERATION_DOWN = 'DOWN'
OPERATION_UP = 'UP'
OPERATION_LEFT = 'LEFT'
OPERATION_RIGHT = 'RIGHT'
EMTPY_TILE = 'm'


class Node:
    """
    Body of node which stores necessary information.
    matrix = current state of board
    parent = pointer to its parent node from which matrix was created
    heuristic_value = calculated heuristic from end point of matrix
    """

    def __init__(self, matrix: np.array, parent, last_operator: str, heuristic_value: int) -> None:
        self.matrix = np.array(matrix)
        self.parent = parent
        self.last_operator = last_operator
        self.heuristic_value = heuristic_value


class Hashmaps:
    """
    class that stored processed and still unprocessed_nodes in dictionaries
    key to dictionary is a hash that is uniquely generated from every matrix
    """

    def __init__(self):

        self.processed_nodes = {}
        self.unprocessed_nodes = {}

    def _create_hash_from_matrix(self, matrix: np.array) -> str:
        """
        function that creates unique hash for given matrix with the help of sha256
        this hash is used to store nodes into dictionaries
        """
        hash = (sha256(matrix).hexdigest())
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
        """
        method that find the best next node by sorting unprocessed_nodes by heuristic value
        then return that node with lowest heuristic value to be processed
        :return: Node with lowest heuristic value
        """
        lowest_heuristic_node = min(self.unprocessed_nodes.values(), key=attrgetter('heuristic_value'))
        hash = self._create_hash_from_matrix(lowest_heuristic_node.matrix)
        self.unprocessed_nodes.pop(hash)
        return lowest_heuristic_node


class Helper:
    """
    class that help with heuristic calculations, string manipulations,
    creating children from possible operations on given matrix and creating nodes
    """

    def __init__(self, end_matrix: np.array, hashmaps: Hashmaps, heurisitc_config: int) -> None:
        self.hashmaps = hashmaps
        self.end = end_matrix
        if heurisitc_config == 1:
            self.calc_heuristic = self.heuristic_1
        else:
            self.calc_heuristic = self.heuristic_2

    def heuristic_1(self, current_matrix: np.array) -> int:
        """
        calculation of first type of heuristic (correct position)
        """
        heuristic = 0
        for i in range(len(current_matrix)):
            for j in range(len(current_matrix[i])):
                if current_matrix[i][j] == EMTPY_TILE:
                    continue
                if current_matrix[i][j] != self.end[i][j]:
                    heuristic += 1
        return heuristic

    def heuristic_2(self, current_matrix: np.array) -> int:
        """
        calculation of second type of heuristic (X,Y offset)
        """
        heuristic = 0
        for i in range(len(current_matrix)):
            for j in range(len(current_matrix[i])):
                if current_matrix[i][j] == EMTPY_TILE:
                    continue
                else:
                    index_y, index_x = np.where(self.end == current_matrix[i][j])
                    heuristic = heuristic + abs(index_y[0] - i) + abs(index_x[0] - j)

        return heuristic

    def find_possible_operators(self, matrix: np.array) -> list:
        """
        method that finds next possible operators by checking where empty tile is located on board
        """
        possible_operators = []
        x = len(matrix[0]) - 1
        y = len(matrix) - 1
        index_y, index_x = np.where(matrix == EMTPY_TILE)
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
        node_heuristic = self.calc_heuristic(matrix)  # calcuting heuristic for new node
        new_node = Node(matrix, parent_node, operator_used, node_heuristic)
        return new_node

    def create_node_from_operator(self, parent_node: Node, possible_operator: str) -> Node:
        """
        method that returns children node from parent node by creating new matrix and changing tiles based on operator
        given
        """
        index_y, index_x = np.where(parent_node.matrix == EMTPY_TILE)
        new_matrix = parent_node.matrix.copy()
        if possible_operator == OPERATION_UP:
            a = new_matrix[index_y[0]][index_x[0]]
            new_matrix[index_y[0]][index_x[0]] = new_matrix[index_y[0] + 1][index_x[0]]
            new_matrix[index_y[0] + 1][index_x[0]] = a
            return self.create_node(new_matrix, parent_node, OPERATION_UP)

        if possible_operator == OPERATION_DOWN:
            a = new_matrix[index_y[0]][index_x[0]]
            new_matrix[index_y[0]][index_x[0]] = new_matrix[index_y[0] - 1][index_x[0]]
            new_matrix[index_y[0] - 1][index_x[0]] = a
            return self.create_node(new_matrix, parent_node, OPERATION_DOWN)

        if possible_operator == OPERATION_LEFT:
            a = new_matrix[index_y[0]][index_x[0]]
            new_matrix[index_y[0]][index_x[0]] = new_matrix[index_y[0]][index_x[0] + 1]
            new_matrix[index_y[0]][index_x[0] + 1] = a
            return self.create_node(new_matrix, parent_node, OPERATION_LEFT)

        if possible_operator == OPERATION_RIGHT:
            a = new_matrix[index_y[0]][index_x[0]]
            new_matrix[index_y[0]][index_x[0]] = new_matrix[index_y[0]][index_x[0] - 1]
            new_matrix[index_y[0]][index_x[0] - 1] = a
            return self.create_node(new_matrix, parent_node, OPERATION_RIGHT)

    def process_node(self, current_node: Node) -> None:
        """
        method that processes node by creating it's children and adding current node to processed_nodes dictionary
        and created children nodes to yet unprocessed_nodes dictionary
        """
        possible_operators = self.find_possible_operators(current_node.matrix)
        for i in range(len(possible_operators)):
            children_node = self.create_node_from_operator(current_node, possible_operators[i])
            if self.hashmaps.check_processed(children_node):
                continue
            else:
                self.hashmaps.add_unprocessed(children_node)
        self.hashmaps.add_processed(current_node)


class Puzzle:
    """
    class which takes given matrix and wanted matrix.
    solves given problem whether it is possible or not and gives and output to the console:
    1. if its solvable it prints the correct order of needed operations
    2. if its not solvable it informs that wanted matrix its not possible to achieve
    """

    def __init__(self, start: list, end: list, heuristic_config: int) -> None:
        self.start = np.array(start)
        self.end = np.array(end)
        self.hashmaps = Hashmaps()
        self.helper = Helper(self.end, self.hashmaps, heuristic_config)
        self.solve()

    def solve(self) -> None:
        """
        method that creates first root node that is later passed to _solve method that starts the algorithm
        """
        root_heuristic = self.helper.calc_heuristic(self.start)
        root_node = Node(self.start, None, "", root_heuristic)
        self._solve(root_node)

    def _solve(self, current_node: Node) -> bool:
        """
        main method processes node and find best next node to processes until heuristic_value = 0 or no more unprocessed
        nodes exists meaning possible solution does not exist
        """
        found_solution = True
        while current_node.heuristic_value != 0:
            self.helper.process_node(current_node)
            current_node = self.hashmaps.find_best_next_node()

            if len(self.hashmaps.unprocessed_nodes) == 0:
                found_solution = False
                break
        if found_solution:
            solution = self._create_solution(current_node)
            print("Order of operators to reach wanted board: " + str(solution))
            return True
        else:
            print("Solution for {} array to move into {} array does not exist!".format(self.start, self.end))
            return False

    def _create_solution(self, node: Node) -> list:
        """
        method that creates a solution by going back in the tree until it reaches root node
        """
        solution = []
        while node.last_operator != '':
            solution.insert(0, node.last_operator)
            node = node.parent
        return solution


