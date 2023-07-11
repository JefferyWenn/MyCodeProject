"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This file contains the main function main() to make the game animation go smoothly.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 15         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
VX = 3
GRAVITY = 1
DELAY = 10


def main():
    """
    In the following program, players will use the mouse to control the position of the paddle, and
    bounce the falling ball to the upper brick area to destroy all bricks. Except for the border at
    the bottom of the game window, the ball will bounce off any object and border. The player need
    to destroy all the bricks in the window to win and when the ball exceeds the border at the bottom
    of the window three times, Game Over!
    """

    graphics = BreakoutGraphics()

    # Add the animation loop here!
    lives = NUM_LIVES
    while lives > 0:
        pause(FRAME_RATE)
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        graphics.set_ball_velocity()
        graphics.check_collision()
        if graphics.check_hit_bottom() is False:
            lives -= 1
        if graphics.check_win():
            break










if __name__ == '__main__':
    main()
