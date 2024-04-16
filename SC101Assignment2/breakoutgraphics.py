"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
PADDLE_COLOR = "#CE4760"
DX = 0
DY = 0


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout',
                 paddle_color=PADDLE_COLOR, max_x_speed=MAX_X_SPEED, intitial_y_speed=INITIAL_Y_SPEED):

        self.game_started = False  # 游戏开始标志
        self.count = 0
        self.game_over_displayed = False

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.paddle_offset = paddle_offset

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = paddle_color
        self.paddle.color = paddle_color

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius)
        self.ball.filled = True
        self.ball.fill_color = "#383B53"
        self.ball.color = "#383B53"
        self.window.add(self.ball, (window_width - ball_radius) / 2, (window_height - ball_radius) / 2)

        self.bricks_left = brick_rows * brick_cols  # 初始化磚塊數量

        #ball move
        self.__dx = random.randint(1, max_x_speed)
        self.__dy = intitial_y_speed
        if random.random() > 0.5:
            self.__dx = -self.__dx

        # mouse
        onmouseclicked(self.op)
        onmousemoved(self.paddle_move)

        # Default initial velocity for the ball
        # Initialize our mouse listeners
        # Draw bricks
        c = ["#465D53", "#4F695D", "#587467", "#608072", "#638475", "#739686", "#7F9F90", "#8BA79A", "#96B0A4", "#A2B9AF"]
        for i in range(brick_rows):
            for j in range(brick_cols):
                temp = GRect(brick_width, brick_height)
                temp.filled = True
                temp.fill_color = c[i]
                temp.color = c[i]
                self.window.add(temp, (brick_width+brick_spacing)*j, brick_offset+(brick_height+brick_spacing)*i)

    def paddle_move(self, event):
        x = event.x - self.paddle.width / 2
        if x < 0:
            x = 0
        if x > self.window.width-self.paddle.width:
            x = self.window.width-self.paddle.width
        self.window.add(self.paddle, x, self.window.height - self.paddle_offset)

    def ball_move(self):
        # 如果游戏结束或胜利信息已经显示，则不再移动球
        if self.game_over_displayed:
            return

        if self.count >= 3:
            if not self.game_over_displayed:
                self.ov()
            return

        if self.check_win_condition() and not self.game_over_displayed:
            self.display_win()
            return

        # 更新球的位置
        if self.game_started and self.count < 3:
            self.ball.move(self.__dx, self.__dy)

            # 檢查球是否碰到窗口邊緣
            if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
                self.__dx = -self.__dx
            if self.ball.y <= 0:
                self.__dy = -self.__dy
            if self.ball.y + self.ball.height >= self.window.height:
                self.ball.x = (self.window.width - self.ball.width) / 2
                self.ball.y = (self.window.height - self.ball.height) / 2
                self.__dx = 0
                self.__dy = 0
                self.count += 1
                self.game_started = False

        collider = self.check_collision()

        if collider is not None:
            # 如果碰到的是板子，则反弹
            if collider == self.paddle:
                self.__dy = -self.__dy
            else:
                # 如果碰到的是砖块，移除砖块并反弹
                self.window.remove(collider)
                self.__dy = -self.__dy

    # game start
    def op(self, event):
        if not self.game_started:
            self.game_started = True
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED
            self.ball_move()

    # game over
    def ov(self):
        if self.game_over_displayed:
            return
        elif not self.game_over_displayed:
            rect = GRect(400, 100)
            rect.filled = True
            rect.fill_color = PADDLE_COLOR
            rect.color = PADDLE_COLOR
            over = GLabel("Game Over")
            over.font = "-65"
            self.window.add(rect, (self.window.width - 400) / 2, (self.window.height - 200) / 2)
            self.window.add(over, (self.window.width - 390) / 2, self.window.height / 2)
            self.game_over_displayed = True

    def check_collision(self):
        # 检查球四个角落是否碰到了物体
        for i in range(0, 2):
            for j in range(0, 2):
                maybe_collided = self.window.get_object_at(self.ball.x + i * 2 * BALL_RADIUS,
                                                           self.ball.y + j * 2 * BALL_RADIUS)
                if maybe_collided is not None:
                    # 如果检测到碰撞的对象是挡板，则直接返回挡板对象
                    if maybe_collided == self.paddle:
                        return maybe_collided
                    # 如果碰到的是其他对象，也返回该对象
                    elif maybe_collided is not self.ball:  # 确保返回的不是球本身
                        self.window.remove(maybe_collided)
                        self.bricks_left -= 1  # 更新剩余砖块数量
                        # 如果是砖块，只需处理一次碰撞，因此返回这个对象
                        return maybe_collided
        return None

    def check_win_condition(self):
        # 检查是否所有砖块都已被移除
        if self.bricks_left == 0:
            return True
        else:
            return False

    def display_win(self):
        # 停止球的移动
        self.__dx = 0
        self.__dy = 0

        # 将球移回初始位置
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2

        # 显示胜利信息
        win_label = GLabel("WIN!")
        win_label.font = "-30-bold"
        win_label.color = "green"
        self.window.add(win_label, x=(self.window.width - win_label.width) / 2,
                        y=(self.window.height - win_label.ascent) / 2)

        # 设置游戏结束标志，防止游戏继续
        self.game_started = False
        self.game_over_displayed = True



