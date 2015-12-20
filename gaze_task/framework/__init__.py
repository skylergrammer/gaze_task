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
    def __init__(self, screen_params, display, images,
                 n_iters=10,
                 delta_t=100,
                 eyetracker=None):

        self.display = display
        self.images = images
        self.delta_t = float(delta_t)
        self.n_iters = n_iters
        self.eyetracker = eyetracker

        # Create screens for both images; doing it now means it is fast
        self.scrn1 = Screen(**screen_params)
        self.scrn1.draw_image(images[0])
        self.scrn2 = Screen(**screen_params)
        self.scrn2.draw_image(images[1])

        if self.eyetracker is not None:
            self.eyetracker.start_recording()
        else:
            sys.exit('ERROR: must attach eyetracker object!')

    def _flash(self, t0):

        '''Hidden method that flashes between the images in images list every
           delta_t milliseconds.
        '''
        position = self.eyetracker.sample()
        self.is_focused = check_focus(position)

        # Pause for specified milliseconds
        while elapsed(t0) < self.delta_t:
            pass

        # If eye tracker detects participant is focused switch images
        if self.is_focused:
            if self.iter_ % 2 == 0:
                self.display.fill(screen=self.scrn1)
            else:
                self.display.fill(screen=self.scrn2)
            self.display.show()
            self.iter_ += 1
        else:
            pass

    def start(self):
        '''Calls the hidden _flash() method.
        '''
        self.iter_ = 0
        while self.iter_ < self.n_iters:
            t0 = datetime.now()
            self._flash(t0)
        self.eyetracker.stop_recording()


def elapsed(t0):
    return (datetime.now() - t0).total_seconds() * 1000


class FakeEyeTracker(object):

    def __init__(self):
        pass

    def stop_recording(self):
        pass

    def start_recording(self):
        pass

    def sample(self):
        return (500, 500)


def check_focus(position):
    x, y = position
    if x >= 0 and y >= 0:
        return True
    else:
        return False
