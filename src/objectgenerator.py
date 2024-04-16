# objectgenerator.py
import random
from sand import Sand
from tree import Tree
from water import Water
import random
from util import check_collision

class objectgenerator:
    def __init__(self):
        # Initialize empty lists to hold objects
        self.map = []
        self.generate_objects()

    def generate_objects(self):
        # Randomly decide how many of each object to create
        sand_count = random.randint(1, 2)
        tree_count = random.randint(3, 6)
        water_count = random.randint(1, 2)

        # Create the specified number of each object
        sands = [Sand() for _ in range(sand_count)]
        trees = [Tree() for _ in range(tree_count)]
        waters = [Water() for _ in range(water_count)]

        map = sands + trees + waters

        random.shuffle(map)

        n = len(map)
        obstacles = []
        max_attempts = 10000000
        for curr_obj in map:
            attempts = 0 
            placed = False
            while not placed and attempts < max_attempts:
                curr_obj.set_random_loc()
                attempts += 1
                overlapping = any(check_collision(curr_obj, obj2) for obj2 in obstacles)
                if not overlapping:
                    obstacles.append(curr_obj)
                    placed = True

        self.map = obstacles




    def reset_objects(self):
        # Call reset or place methods on all objects
        for object  in self.map:
            object.set_random_loc()

   # def get_objects(self):
   #     # Return all objects in a dictionary
   #     return {'sands': self.sands, 'trees': self.trees, 'waters': self.waters}

