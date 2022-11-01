from enum import Enum
import random
from typing import List

class NodeType(Enum):
    PROGRAM = 0,
    INSTRUCTION = 1,
    CONDITIONAL_STATEMENT = 10,
    CONDITION = 11,
    COMPARISON_OPERATOR = 12, # ==, <, >, <=, >=, !=
    LOGICAL_OPERATOR = 13, # AND, OR
    ARITHMETICAL_EXPR = 20,
    ASSIGNMENT = 21,
    ATOM = 30,
    INT = 31,
    VAR_NAME = 33,
    VAR_NAME_IMMUTABLE = 34,
    TWO_ARG_OPERATOR = 40,
    ADD = 41,
    DIV = 42,
    MUL = 43,
    SUB = 44


class Node:
    max_nr_of_children = 5

    type_to_children = {
        NodeType.PROGRAM: [(-1, [NodeType.INSTRUCTION])],
        NodeType.INSTRUCTION: [(1, [NodeType.CONDITIONAL_STATEMENT]), (1, [NodeType.ASSIGNMENT])],
        NodeType.CONDITIONAL_STATEMENT: [(2, [NodeType.CONDITION, NodeType.INSTRUCTION])],
        NodeType.CONDITION: [(3, [NodeType.ARITHMETICAL_EXPR, NodeType.COMPARISON_OPERATOR, NodeType.ARITHMETICAL_EXPR])],
        NodeType.ARITHMETICAL_EXPR: [(1, [NodeType.ATOM]), 
            (3, [NodeType.ATOM, NodeType.TWO_ARG_OPERATOR, NodeType.ATOM])],
        NodeType.ASSIGNMENT: [(2, [NodeType.VAR_NAME_IMMUTABLE, NodeType.INT])] # add varname=varname
    }

    type_to_point_mutation = {
        NodeType.INT: [NodeType.VAR_NAME],
        NodeType.VAR_NAME: [NodeType.INT],
        NodeType.ADD: [NodeType.DIV, NodeType.SUB, NodeType.MUL],
        NodeType.DIV: [NodeType.ADD, NodeType.SUB, NodeType.MUL],
    }

    def __init__(self, node_type: NodeType, children) -> None:
        self.type = node_type
        self.children = children # List[Node]
        self.parent = None # Node

    @staticmethod
    def is_pseudo_type(type: NodeType) -> bool:
        return type in [NodeType.PROGRAM, NodeType.INSTRUCTION]
    
    @staticmethod
    def generate_random_children_types(parent: NodeType) -> List[NodeType]:
        possible_combinations = len(Node.get_possible_children(parent))
        if possible_combinations == 0:
            return []
        idx = random.randint(0, possible_combinations-1)
        nr_of_children, children_types = Node.get_possible_children(parent)[idx]

        if nr_of_children != -1:
            return children_types
        else:
            nr_of_children = random.randint(1, Node.max_nr_of_children)
            children = []
            for idx in range(nr_of_children):
                idx = random.randint(0, len(children_types)-1)
                children.append(children_types[idx])
            return children
    
    @staticmethod
    def get_possible_children(node_type: NodeType):
        return Node.type_to_children.get(node_type, [])
    
    @staticmethod
    def get_possible_point_mutations(node_type: NodeType):
        return Node.type_to_point_mutation.get(node_type, [])

class GP:
    def __init__(self) -> None:
        self.max_depth = 5
        self.population_size = 5
        self.population = [] # List[Node]
        self.fitness = [] # List[float]
        self.tournament_size = 2
    
    # TODO
    # możliwość testowania programów 
    def compute_fitness(self, individual:Node) -> float:
        return -random.randint(0, 2137)

    def create_random_individual(self) -> Node:
        print("-- NEW INDIVIDUAL --")
        root, level = Node(NodeType.PROGRAM, []), 0
        queue = [(level,root)] # (int, Node)
        while queue:
            level, node = queue.pop(0)
            types = Node.generate_random_children_types(node.type)
            print("level: ", level, " type: ", str(node.type), " children: ", types)
            if level < self.max_depth:
                for idx in range(len(types)):
                    node.children.append(Node(types[idx], []))
                    if not Node.is_pseudo_type(node.children[idx].type):
                        queue.append((level+1, node.children[idx]))
                    else:
                        queue.append((level, node.children[idx]))
        return root
    
    def create_random_population(self):
        for idx in range(self.population_size):
            self.population.append(self.create_random_individual())
            self.fitness.append(self.compute_fitness(self.population[idx]))

    """
        Return idx of the best individual
    """
    def perform_tournament(self) -> int:
        fbest = -1.0e34
        best = random.randint(0, self.population_size-1)
        for idx in range(self.tournament_size):
            competitor = random.randint(0, self.population_size-1)
            if self.fitness[competitor] > fbest:
                fbest = self.fitness[competitor]
                best = competitor
        return best
    
    """
        Return idx of the worst individual
    """
    def perform_negative_tournament(self) -> int:
        fworst = 1.0e34
        worst = random.randint(0, self.population_size-1)
        for idx in range(self.tournament_size):
            competitor = random.randint(0, self.population_size-1)
            if self.fitness[competitor] < fworst:
                fworst = self.fitness[competitor]
                worst = competitor
        return worst

    # TODO
    # operację krzyżowania dwóch drzew/programów
    def perform_crossover(self, parent1: Node, parent2: None) -> Node:
        pass

    """
        Mutates provided node with other randomly chosen.
        Not all nodes have alternatives for mutations and such nodes cannot
        be mutate with point mutation.
    """
    def perform_point_mutation(self, parent: Node) -> Node:
        possibilities = Node.get_possible_point_mutations(parent.type)
        if len(possibilities) == 0:
            return parent
        else:
            idx = random.randint(0, len(possibilities)-1)
            new_node = Node(possibilities[idx], parent.children)
            print("Switch", parent.type, "to", new_node.type)
            return new_node
    
    def mutate(self, root: Node) -> Node:
        queue = [root] 
        while queue:
            node = queue.pop()
            new_node = self.perform_point_mutation(node)
            node.type = new_node.type
            node.children = new_node.children
            for child in node.children:
                queue.append(child)
        return root

    def display_program(self, root: Node):
        print("\n*** PROGRAM ***")
        level = 0
        stack = [(level, root)]
        while stack:
            level, node = stack.pop(-1)
            level_display = "".join(["  " for nr in range(level)]) + "|"
            print(level_display, level, node.type)
            for child in reversed(node.children):
                stack.append((level + 1, child))


print("---RUN---")
gp = GP()
root = gp.create_random_individual()
gp.create_random_population()
gp.display_program(gp.population[0])
gp.population[0] = gp.mutate(gp.population[0])
gp.display_program(gp.population[0])