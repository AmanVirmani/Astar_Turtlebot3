from math import sqrt
from utils import Node, Environment


class PathPlanning:
    # Initiation method
    def __init__(self, start, goal, clearance, stepSize):
        self.start = start
        self.goal = goal
        self.clearance = clearance
        self.stepSize = stepSize

    # Method to solve a A* object
    def Astar(self):
        search = []
        # Set current node to start and add start node to the node list and node search dictionary
        CurrentNode = Node(self.start, self.start, self.goal, self.stepSize)
        NodeList = [CurrentNode]
        NodeDict = {tuple(CurrentNode.env)}
        search.append(CurrentNode)
        # Check if the current node is the goal node
        while sqrt((CurrentNode.env[0] - self.goal[0]) ** 2 + (CurrentNode.env[1] - self.goal[1]) ** 2) > 1.5:

            # Keep checking if there are nodes in list
            if len(NodeList) > 0:
                # Set current node to the first node in the list and then delete from list
                CurrentNode = NodeList.pop()

                Course = Environment(CurrentNode.env, self.clearance)
<<<<<<< HEAD
                # Check all of the possible nodes
                for node in Course.possibleMoves(self.start, CurrentNode, self.stepSize):

                    # Search dictonary and add node to list and dictionary if it hasn't been explored yet
                    if tuple((int(node.env[0]), int(node.env[1]), node.env[2])) not in NodeDict:
                        NodeList.append(node)
                        search.append(node)
                        NodeDict.add(tuple((int(node.env[0]), int(node.env[1]), node.env[2])))
                # Sort list of nodes based on cost
                NodeList.sort(key=lambda x: x.cost, reverse=True)
=======
                # Check all of the possible actions
                for action in Course.possibleMoves(self.start, CurrentNode, self.stepSize):

                    # Search dictonary and add node to list and dictionary if it hasn't been explored yet
                    if tuple((int(action.env[0]), int(action.env[1]), action.env[2])) not in NodeDict:
                        NodeList.append(action)
                        search.append(action)
                        NodeDict.add(tuple((int(action.env[0]), int(action.env[1]), action.env[2])))
                # Sort list of nodes based on cost
                NodeList.sort(key=lambda x: x.weight, reverse=True)
>>>>>>> d2b054beac22f2227f5e470247076e85b2a770e3

            else:
                return -1, CurrentNode.path(), search
        # solve for path
        x = CurrentNode.path()
        path = []
        for node in x:
            path.append(node)
        return path, search
