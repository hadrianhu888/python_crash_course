import random as rm
from random import choice
from random import randint


class RandomWalk:
    """A class that defines a random walk function"""
    num_points = rm.randint(1, 50)

    def __init__(self, num_points=50):
        """Initialize the attributes of the random walk"""
        self.num_points = num_points
        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculates all the points in the walk"""
        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = choice([x_direction * x_distance])

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = choice([y_direction * y_distance])

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0 and x_distance == 0 and y_distance == 0:
                continue

            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values[-1] = x
            self.y_values[-1] = y
