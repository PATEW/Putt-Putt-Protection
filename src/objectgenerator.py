# objectgenerator.py
import random
from sand import Sand
from tree import Tree
from water import Water

class objectgenerator:
    def __init__(self):
        # Initialize empty lists to hold objects
        self.sands = []
        self.trees = []
        self.waters = []
        self.generate_objects()

    def generate_objects(self):
        # Randomly decide how many of each object to create
        sand_count = random.randint(1, 2)
        tree_count = random.randint(1, 6)
        water_count = random.randint(1, 2)

        # Create the specified number of each object
        self.sands = [Sand() for _ in range(sand_count)]
        self.trees = [Tree() for _ in range(tree_count)]
        self.waters = [Water() for _ in range(water_count)]

    def reset_objects(self):
        # Call reset or place methods on all objects
        for sand in self.sands:
            sand.place_sand()
        for tree in self.trees:
            tree.place_tree()
        for water in self.waters:
            water.place_water()

    def get_objects(self):
        # Return all objects in a dictionary
        return {'sands': self.sands, 'trees': self.trees, 'waters': self.waters}
