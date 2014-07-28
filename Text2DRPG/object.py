class Object(object):
    def __init__(self):
        self.x = 0
        self.y = 0

        self.marker = ""

        self.is_roof = False

        self.empty = False

        self.is_movable = False

    def set_pos(self, vector):
        self.x = vector[0]
        self.y = vector[1]

    def get_pos(self):
        return [self.x, self.y]

    def set_marker(self, marker):
        self.marker = marker

    def get_marker(self):
        return self.marker

    def set_blocking(self, bool):
        if bool == True:
            self.blocking = True
        elif bool == False:
            self.blocking = False

    def get_blocking(self):
        return self.blocking

class Wall(Object):
    def __init__(self):
        super(Wall, self).__init__()
        self.set_marker("#")
        self.set_blocking(True)

class Roof(Object):
    def __init__(self):
        super(Roof, self).__init__()
        self.set_marker("=")
        self.set_blocking(False)
        self.is_roof = True

class Empty(Object):
    def __init__(self):
        super(Empty, self).__init__()
        self.set_marker("")
        self.set_blocking(False)
        self.empty = True

class Floor(Object):
    def __init__(self):
        super(Floor, self).__init__()
        self.set_marker("*")
        self.set_blocking(False)
        self.empty = False