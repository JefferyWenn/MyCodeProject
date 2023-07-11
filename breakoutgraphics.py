"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This file Define a class called BreakoutGraphics, which handles all background images and components.
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

# Global variables
score = 0


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window_width-paddle_width)/2,
                            y=self.window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball_initial_x = (self.window_width-ball_radius*2)/2
        self.ball_initial_y = (self.window_height-ball_radius*2)/2
        self.ball = GOval(ball_radius*2, ball_radius*2, x=self.ball_initial_x, y=self.ball_initial_y)
        self.ball.filled = True
        self.window.add(self.ball)

        # Create a scoreboard show the total score earned
        self.box = GRect(100, 20)
        self.score_label = GLabel('Score: ' + str(score), x=0, y=20)
        self.score_label.font = '-20'
        self.window.add(self.box, x=0, y=0)
        self.window.add(self.score_label)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Detect whether the ball is moving
        self.detect_ball_move = True

        # Detect whether the ball hit the bottom window
        self.detect_ball_hit_bottom = False

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_move)

        # Draw bricks
        for i in range(BRICK_COLS):
            x = i * (BRICK_WIDTH + BRICK_SPACING)
            for j in range(BRICK_ROWS):
                y = j * (BRICK_HEIGHT + BRICK_SPACING) + BRICK_OFFSET
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT, x=x, y=y)
                self.brick.filled = True
                if j <= 1:
                    self.brick.fill_color = 'red'
                elif j <= 3:
                    self.brick.fill_color = 'orange'
                elif j <= 5:
                    self.brick.fill_color = 'yellow'
                elif j <= 7:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick)

    def paddle_move(self, mouse, width=PADDLE_WIDTH):
        """
        :param mouse: hardware mouse
        :param width: The width of paddle
        Make the paddle move with the mouse.
        """
        self.paddle.x = mouse.x - width / 2
        self.paddle.y = self.window.height - PADDLE_OFFSET
        if self.paddle.x < 0:
            self.paddle.x = 0
        if self.paddle.x > self.window.width - width:
            self.paddle.x = self.window.width - width

    def ball_move(self, mouse):
        """
        :param mouse: hardware mouse
        Control the movement of the ball after the mouse click.
        """
        if self.detect_ball_move:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.detect_ball_move = False

    def get_dx(self):
        """
        :return: The velocity of the ball in x-direction.
        """
        return self.__dx

    def get_dy(self):
        """
        :return: The velocity of the ball in y-direction.
        """
        return self.__dy

    def check_hit_bottom(self):
        """
        Check if the ball hit the bottom of window or not
        :return: bool
        """
        if self.detect_ball_hit_bottom:
            self.detect_ball_hit_bottom = False
            return False
        else:
            self.detect_ball_hit_bottom = False
            return True

    def set_ball_velocity(self):
        """
        Change the ball's velocity while colliding with objects or walls.
        If the ball hits the bottom window, then reset the ball to the initial position.
        """
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window_width:
            self.__dx = - self.__dx
        if self.ball.y <= 0:
            self.__dy = - self.__dy
        if self.ball.y + self.ball.height >= self.window_height:
            self.reset_ball_position()
            self.detect_ball_move = True
            self.detect_ball_hit_bottom = True

    def reset_ball_position(self):
        """
        Reset the ball to the initial position.
        """
        self.window.remove(self.ball)
        self.window.add(self.ball, x=self.ball_initial_x, y=self.ball_initial_y)
        self.__dx = 0
        self.__dy = 0

    def check_collision(self):
        """
        Check if the ball has a collision, if so, what is the colliding object.
        """
        # Create four vertices of the ball
        x1 = self.ball.x
        y1 = self.ball.y
        x2 = self.ball.x+self.ball.width
        y2 = self.ball.y+self.ball.height

        # Detect the objects at each vertices of the ball
        obj1 = self.window.get_object_at(x1, y1)
        obj2 = self.window.get_object_at(x2, y1)
        obj3 = self.window.get_object_at(x1, y2)
        obj4 = self.window.get_object_at(x2, y2)

        # Detect whether the ball has collision
        collision = False

        """
        Detect whether each vertex has a collision. 
        If the ball hit the paddle, then rebound the ball. 
        If it hit the brick, the ball rebounds and demolishes the brick.
        """
        global score
        if obj1 is not None:
            collision = True
            if obj1 != self.box and obj1 != self.score_label:
                if obj1 != self.paddle:
                    self.window.remove(obj1)
                    score += 1
                    self.score_label.text = 'Score: '+str(score)
                self.__dy = -self.__dy
        if collision is False and obj2 is not None:
            collision = True
            if obj2 != self.box and obj2 != self.score_label:
                if obj2 != self.paddle:
                    self.window.remove(obj2)
                    score += 1
                    self.score_label.text = 'Score: '+str(score)
                self.__dy = -self.__dy
        if collision is False and obj3 is not None:
            collision = True
            if obj3 != self.box and obj3 != self.score_label:
                if obj3 != self.paddle:
                    self.window.remove(obj3)
                    score += 1
                    self.score_label.text = 'Score: ' + str(score)
                self.__dy = -self.__dy
        if collision is False and obj4 is not None:
            if obj4 != self.box and obj4 != self.score_label:
                if obj4 != self.paddle:
                    self.window.remove(obj4)
                    score += 1
                    self.score_label.text = 'Score: ' + str(score)
                self.__dy = -self.__dy

    def check_win(self):
        """
        Check if the player have won the game
        :return: bool
        """
        if score == BRICK_COLS * BRICK_ROWS:
            return True
        return False
