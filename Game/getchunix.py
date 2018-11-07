''' This for unblocking input '''
from __future__ import print_function


class GetchUnix(object):
    ''' This for unblocking input'''
    def __init__(self):
        import tty

    def __call__(self):
        import sys
        import tty
        import termios
        fdx = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fdx)
        try:
            tty.setraw(sys.stdin.fileno())
            che = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fdx, termios.TCSADRAIN, old_settings)
        return che
