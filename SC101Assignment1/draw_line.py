"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked, onmousemoved
SIZE = 10
color = "#FFC2E2"
window = GWindow()
o1 = GOval(SIZE, SIZE)
last_x = None
last_y = None
last_c = None

def main():
    onmouseclicked(draw)
    onmousemoved(change_position)
    o1.color = color
    window.add(o1)


def change_position(mouse):
    o1.x = mouse.x - SIZE / 2
    o1.y = mouse.y - SIZE / 2

def draw(event):
    global last_x, last_y, last_c
    if last_x is not None and last_y is not None:
        line = GLine(last_x, last_y, event.x, event.y)
        line.line_width = SIZE  #不知道為何沒作用
        line.color = color
        window.remove(last_c)
        window.add(line)

        last_x = None
        last_y = None
    else:
        pen_stroke = GOval(SIZE, SIZE, x=event.x - SIZE / 2, y=event.y - SIZE / 2)
        pen_stroke.color = color
        window.add(pen_stroke)
        last_c = pen_stroke
        last_x = event.x
        last_y = event.y



if __name__ == "__main__":
    main()
