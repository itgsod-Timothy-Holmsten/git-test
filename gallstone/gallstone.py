class Gallstone(object):

    def __init__(self, rad):
        self.radius = rad

    def __str__(self):
        return "Diameter: %s" %self.diameter

    @property
    def diameter(self):
        return self.radius * 2
