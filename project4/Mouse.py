from Turtle import Turtle
from Vector import *
from Color import *

class Mouse(Turtle):
    """docstring for Mouse"""
    def __init__(self, position, heading, fill=green, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.radius = (self.position - self.origin).length()
        self.theta = (self.m / self.radius) * 180 / pi

    def getnextstate(self):
        """Advance around statue."""
        p = (self.position - self.origin).rotate(-self.theta)
        return p + self.origin, self.heading
