#
# 2do
#
import Point as Point

class Line:
    def __init__(self, start: Point = (0,0), end: Point = (0, 1)):
        self.start = start
        self.end = end

    def location(self):
        return "Start at " + str(self.start) + " and ends at" + str(self.end)