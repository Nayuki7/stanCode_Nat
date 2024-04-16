"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
VY = 0
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
moving = False
count = 0

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
ball.filled = True  # 填滿
ball.fill_color = "#FFC2E2"
ball.color = "#FFC2E2"
window.add(ball, x=START_X, y=START_Y)

def main():
    onmouseclicked(start_move)

def start_move(event):
    global moving, count
    if not moving and count < 3:
        moving = True
        move_ball()


def move_ball():
    global VY, moving, count
    while moving:
        ball.move(VX, VY)
        VY += GRAVITY
        if ball.y + SIZE >= window.height:
            VY = -VY*REDUCE
        if ball.x + SIZE > window.width:
            window.add(ball, x=START_X, y=START_Y)  # 重置位置
            VY = 0  # 重置垂直速度
            moving = False
            count += 1
        if count == 3:
            moving = False

        pause(DELAY)


if __name__ == "__main__":
    main()
