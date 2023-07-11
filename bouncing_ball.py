"""
File: bouncing_ball.py
Name: 溫孟哲
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
rounds = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    """ball.filled = True
    window.add(ball, START_X, START_Y)
    onmouseclicked(bounce)


def bounce(bounce_ball):
    global rounds
    x = START_X
    y = START_Y
    n = 0
    vy = 0
    if rounds < 3:
        while x < 800:
            while y < 500:
                pause(DELAY)
                n += 1
                window.clear()
                window.add(ball, x, y)
                pause(DELAY)
                x += VX
                vy = GRAVITY * n
                y += vy
            while vy > 0:
                pause(DELAY)
                n -= 1.1
                window.clear()
                window.add(ball, x, y)
                pause(DELAY)
                x += VX
                vy = REDUCE * (GRAVITY * n)
                y -= vy
        window.add(ball, START_X, START_Y)
        rounds += 1"""
    ball.filled = True
    window.add(ball, START_X, START_Y)
    onmouseclicked(bounce)
    while rounds > 3:
        break


def bounce():
    global rounds
    x = START_X
    y = START_Y
    n = 0
    vy = 0
    while x < 800:
        while y < 500:
            pause(DELAY)
            n += 1
            window.clear()
            window.add(ball, x, y)
            pause(DELAY)
            x += VX
            vy = GRAVITY * n
            y += vy
        while vy > 0:
            pause(DELAY)
            n -= 1.1
            window.clear()
            window.add(ball, x, y)
            pause(DELAY)
            x += VX
            vy = REDUCE * (GRAVITY * n)
            y -= vy
    window.add(ball, START_X, START_Y)
    rounds += 1

if __name__ == "__main__":
    main()
