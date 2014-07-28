from object import Object
import time
import math

class Inventory(object):
    def __init__(self):
        self.inv = {}

    def add_item(self, object):
        self.inv[len(self.inv)] = object

    def delete_item(self, key):
        self.inv.pop(key)

    def show_inventory(self):
        print(self.inv)

class Player(Object):
    def __init__(self):
        super(Player, self).__init__()
        self.inventory = Inventory()

        self.health = 1
        self.max_health = 10

        self.set_marker("X")
        self.next_walk = 0

        self.level = 10
        self.experience = 0

        self.is_movable = True

    def set_map(self, map):
        self.map = map

    def get_map(self):
        return self.map

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    def get_max_health(self):
        return self.max_health

    def set_max_health(self, health):
        self.max_health = health

    def show_health(self):
        health_string = "Health: |"
        for hp in range(1, self.get_max_health() + 1):
            if hp <= self.get_health():
                health_string += "x|"
            else:
                health_string += " |"


        return health_string

    def should_draw_roof(self, bool):
        map = self.get_map()
        self.draw_roof = bool
        for object in map.get_map_objects().values():
            if object != self:
                if object.is_roof and bool == False:
                    object.set_marker("NO_DRAW")
                elif object.is_roof and bool == True:
                    object.set_marker("=")

    def set_next_walk(self, seconds):
        current_time = time.time()
        self.next_walk = current_time + seconds

    def can_walk(self):
        current_time = time.time()
        if self.next_walk - current_time <= 0 or self.next_walk == 0:
            return True

    def walk(self, direction):

        walk_speed = 1/math.log10(self.level*self.level*4)

        if not self.can_walk():
            return
        else:
            self.set_next_walk(walk_speed)

        ## Set old pos to use for example if an object is blocking
        old_pos = self.get_pos()
        ## Get the map which the player is using
        map = self.get_map()

        ## Draw the roof
        self.should_draw_roof(True)

        ## Walking
        if direction == "w":
            self.y -= 1
        elif direction == "s":
            self.y += 1
        elif direction == "d":
            self.x += 1
        elif direction == "a":
            self.x -= 1

        ## Check all the objects except the player in the map
        for object in map.get_map_objects().values():
            if object != self:
                ## Is the object at the same position as the player
                if object.get_pos() == self.get_pos():
                    ## Is the object blocking
                    if object.get_blocking():
                        self.set_pos(old_pos)
                    ## Is the object a roof
                    if object.is_roof:
                        self.should_draw_roof(False)

