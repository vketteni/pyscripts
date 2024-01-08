from Xlib import X, display
import time

def move_mouse(dx, dy):
    d = display.Display()
    s = d.screen()
    root = s.root
    current = root.query_pointer()._data
    new_x = current["root_x"] + dx
    new_y = current["root_y"] + dy
    root.warp_pointer(new_x, new_y)
    d.sync()

while True:
    move_mouse(10, 10)
    time.sleep(60)
    move_mouse(-10, -10)
    time.sleep(60)

