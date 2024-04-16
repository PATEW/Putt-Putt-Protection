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

        collision_detected = True

        while collision_detected:
            collision_detected = False

            n = len(map)
            for i in range(n):
                for j in range(i+1, n):
                    if check_collision(map[i], map[j]):
                        map[i].set_random_loc()
                        map[j].set_random_loc()
                        collision_detected = True
                        break
                if collision_detected:
                    break

        self.map = map


    def check_collision_in_map(objects: list):
        collision_detected = True

        while collision_detected:
            collision_detected = False

            n = len(objects)
            for i in range(n):
                for j in range(i+1, n):
                    if check_collision(map[i], map[j]):
                        map[i].set_random_loc()
                        map[j].set_random_loc()
                        collision_detected = True
                        break
                if collision_detected:
                    break



    def reset_objects(self):
        # Call reset or place methods on all objects
        for object  in self.map:
            object.set_random_loc()

   # def get_objects(self):
   #     # Return all objects in a dictionary
   #     return {'sands': self.sands, 'trees': self.trees, 'waters': self.waters}

