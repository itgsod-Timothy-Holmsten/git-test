import object as ob
import console
import sys

def new_line(used_space):
    con_width, con_height = console.getTerminalSize()
    s = str()
    for space in range(0, con_width - used_space):
        s += " "

    return s

class Map(object):
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y

        self.map_objects = {}
        self.map_movable_objects = []

    def draw_map(self, start_x, start_y, end_x, end_y):

        ## Used to draw the map
        self.map = str()

        space = None

        for y in range(start_y, end_y):
            if space != None and y != end_y:
                self.map += "|"
                space += 1
                self.map += new_line(space)
            if y == end_y - 1:
                break
            space = 0
            for x in range(start_x, end_x):
                space += 1
                found = False
                if self.get_map_objects().has_key(str([x, y])):
                    pos = str([x, y])
                    object = self.get_map_objects()[pos]

                    if not object.empty and object.get_marker() != "NO_DRAW":
                        self.map += object.marker
                        continue

                for object_movable in self.map_movable_objects:
                    if object_movable.get_pos() == [x, y]:
                        self.map += object_movable.get_marker()
                        found = True

                if found:
                    continue


                self.map += " "

        ## Draw more outlines of the game screen (bottom)
        for x in range(start_x, end_x):
            self.map += "-"

        ## Print the map (draw)
        sys.stdout.write(self.map)
        print ""


    def draw_map_follow(self, object, distance_x, distance_y):
        ## This function is used to draw the map while following an object (like a camera)

        ## Get the object's position
        object_x, object_y = object.get_pos()

        ## The max and min of where the 'camera' should stop (usually when the map ends)
        x = max(min(object_x, self.size_x - distance_x), distance_x)
        y = max(min(object_y, self.size_y - distance_y), distance_y)

        return self.draw_map(x - distance_x, y - distance_y, x + distance_x + 1, y + distance_y + 1)

    def add_object_to_map(self, object):
        self.map_objects[str(object.get_pos())] = object

    def add_movable_object_to_map(self, object):
        self.map_movable_objects.append(object)

    def load_map_objects(self, objects):
        ## Used if the map should add several objects at the same time

        for object in objects.values():
            self.add_object_to_map(object)

    def get_map_objects(self):
        return self.map_objects

    def load_map_from_file(self, file):
        ## This function is used to add map objects from a text file

        with open(file, "r") as map:
            l = map.readlines()

            print "Loading map..."

            ##########################################
            ## Todo, fix a better method to do this ##
            ##########################################

            for line in range(0, len(l)):
                for char in range(0, len(l[line])):
                    map_objects_from_file = {}
                    map_objects_from_file["1"] = ob.Wall()
                    map_objects_from_file["2"] = ob.Roof()

                    map_objects_from_file["4"] = ob.Floor()

                    _object = l[line][char]

                    if map_objects_from_file.has_key(_object):
                        _obj_ = map_objects_from_file[_object]
                        _obj_.set_pos([char, line])
                        self.add_object_to_map(_obj_)