"""
File: draw_line.py
Name:溫孟哲
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow()
SIZE = 10
click = 0
a = None
b = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(mouse):
    global click, a, b

    dot = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
    dot.color = 'blue'
    line = GLine(a, b, mouse.x, mouse.y)
    line.filled = True
    line.fill_color = 'blue'

    if click % 2 == 0:
        window.add(dot)
        click += 1
        a = dot.x
        b = dot.y
    else:
        window.clear()
        window.add(line)
        click -= 1


if __name__ == "__main__":
    main()
