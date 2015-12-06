import sys
from datetime import datetime
from PIL import Image
from pygaze.libscreen import Screen


class Task(object):
    '''Display k image reversals that switch every delta_t milliseconds. Pauses
       image switching if is_looking signal is False.

       Parameters
       ----------
       root : tkinter root object
       canvas : tkinter canvas object
                The canvas that images will be displayed on.
       images : list
                List of image files.  Should be in working directory or full
                paths.
       delta_t : int or float
                 time, in milliseconds, between image switches
       n_iters : int
                 number of image flases to perform before quitting
       height : int
                height of canvas in number of pixels
       width : int
               width of canvas in number of pixels
    '''
    def __init__(self, screen, display, images,
                 n_iters=10,
                 delta_t=100,
                 eyetracker=None):

        self.display = display
        self.images = [Image.open(x) for x in images]
        self.delta_t = float(delta_t)
        self.n_iters = n_iters
        self.eyetracker = eyetracker
        self.screen = screen
        self.screen1 = Screen()
        self.screen2 = Screen()
        self.screen1.draw_image(self.images[0])
        self.screen2.draw_image(self.images[1])
        self.screen.copy(self.screen2)
        self.display.fill(self.screen)
        self.display.show()

        if self.eyetracker is not None:
            self.eyetracker.start_recording()
        else:
            pass
            sys.exit('ERROR: must attach eyetracker object!')

    def _flash(self, t0):

        '''Hidden method that flashes between the images in images list every
           delta_t milliseconds.
        '''
        position = self.eyetracker.sample()
        self.is_focused = check_focus(position)
        while elapsed(t0) < self.delta_t:
            pass

        if self.is_focused:
            idx = self.iter_ % 2
            self.screen.clear()

            if idx == 0:
                self.screen.copy(self.screen1)
            else:
                self.screen.copy(self.screen2)
            self.display.fill(self.screen)
            self.display.show()
            self.iter_ += 1
        print(self.iter_, elapsed(t0))

    def start(self):
        '''Calls the hidden _flash() method.
        '''
        self.iter_ = 0
        while self.iter_ < self.n_iters:
            t0 = datetime.now()
            self._flash(t0)

        self.display.close()
        self.eyetracker.stop_recording()

    def calibrate(self):
        self.eyetracker.calibrate()
        return self

def elapsed(t0):
    return (datetime.now() - t0).total_seconds() * 1000

def fake_eye_tracker(iter_):
    if iter_ % 5 == 0 and iter_ > 0:
        return False
    else:
        return True


def check_focus(position):
    x, y = position
    if x >= 0 and y >= 0:
        return True
    else:
        return False
