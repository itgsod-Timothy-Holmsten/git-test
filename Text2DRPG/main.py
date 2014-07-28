from player import Player
from map import Map
import signal
from contextlib import contextmanager
import os
import time
import console

ply = Player()

ply.inv = ply.inventory

ply.set_pos([2,2])

map = Map(10000,10000)
map.add_movable_object_to_map(ply)

ply.set_map(map)

def getchar():
   #Returns a single character from standard input
   import tty, termios, sys
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch

map.load_map_from_file("map.txt")

class TimeoutException(Exception): pass

@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException, "Timed out!"
    signal.signal(signal.SIGALRM, signal_handler)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)

## Game loop
while True:
    fps = time.time()

    con_width, con_height = console.getTerminalSize()

    os.system('cls' if os.name == 'nt' else 'clear')
    map.draw_map_follow(ply, int(con_width/4), int((con_width/4) /2))
    print(ply.show_health())
    print "FPS:", 1/(time.time() - fps)
    ch = None
    try:
        with time_limit(0.1):
            ch = getchar()
            ply.walk(ch)
    except:
        pass

    if ch == "x":
        exit()
    if ch == "y":
        pass

