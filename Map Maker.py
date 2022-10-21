# Title: Map Maker
# Date started: July 8th, 2022
# Description:
# Creates a map of a given 2D terrain using a robot and distance sensors.
# First I will write the code so that it maps out a known virtual terrain. Then I will
# adapt the code so that it can map out an unknown real terrain with a real robot
# with real sensors.
# =============================================================================


import numpy as np


# =============================================================================


class Robot:
    def __init__(self, terrain, radars = [], location = (0,0), angle = 0, increment = 1, angle_increment = 10):
        self.terrain = terrain # map of the terrain we want to map out (yes, I know that seems useless, but we will adjust later)
        self.radars = radars # array of radar objects
        self.location = np.array(location) # location on a 2D cartesian plane
        self.angle = angle # in degrees, the direction in which the front of the robot is facing
        self.increment = increment # cm, the increment of distance the robot travels by
        self.angle_increment = angle_increment # degrees, the increment of angle the robot rotates by
        
    # === Movement methods ===
    def forwards(self):
        """
        This method is called when the up arrow key is pressed. It moves the robot
        forward by a distance of <self.increment> in the direction given by 
        <self.angle> from the initial location given by <self.location>.

        Returns
        -------
        None.

        """
        # !!!== Need to figure out how to account for walls and invalid moves ===!!!
        vertical_component = np.sin(self.increment)
        horizontal_component = np.cos(self.increment)
        
        self.location += horizontal_component, vertical_component
        return
    
    def backwards(self):
        """
        This method is called when the down arrow key is pressed. It moves the robot
        backwards by a distance of <self.increment> in the direction given by 
        <self.angle> from the initial location given by <self.location>.

        Returns
        -------
        None.

        """
        # !!!== Need to figure out how to account for walls and invalid moves ===!!!
        vertical_component = np.sin(self.increment)
        horizontal_component = np.cos(self.increment)
        
        self.location -= horizontal_component, vertical_component
        
        return
    
    def left(self):
        """
        This method is called when the left arrow key is pressed. It rotates the
        robot by <angle_increment> counterclockwise/to the left from the initial
        angle given by <self.angle>

        Returns
        -------
        None.

        """
        self.angle += self.angle_increment
        return
    
    def right(self):
        """
        This method is called when the right arrow key is pressed. It rotates the
        robot by <angle_increment> clockwise/to the right from the initial
        angle given by <self.angle>

        Returns
        -------
        None.

        """
        self.angle -= self.angle_increment
        return
    
    # === Detection methods ===
    def detect(self, terrain):
        for radar in self.radars:
            radar.detect(terrain, self.location, self.angle)
        
        # update created map here
        
        return
 
    
# =============================================================================

       
class Radar:
    def __init__(self, ray_length = 0, ray_direction = None):
        self.ray_length = ray_length
        self.ray_direction = ray_direction
        
    def detect(self, terrain, location, angle):
        # to be implemented
        return
    
    
# =============================================================================    
    
    
class CreatedMap:
    def __init__(self):
        self.map = None # will become an array of values... probably
        self.drawing = None # will hold an image of the map drawn up