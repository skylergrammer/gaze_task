import sys
import time


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
    def __init__(self, screen, display,
                 images=None,
                 n_iters=10,
                 delta_t=100,
                 eyetracker=None):

        self.display = display
        self.screen = screen
        self.images = images
        self.delta_t = float(delta_t)
        self.n_iters = n_iters
        self.eyetracker = eyetracker

        if self.eyetracker is not None:
            self.eyetracker.start_recording()
        else:
            pass
            # sys.exit('ERROR: must attach eyetracker object!')

    def _flash(self):

        '''Hidden method that flashes between the images in images list every
           delta_t milliseconds.
        '''
        t0 = time.time() * 10000
        # position = self.eyetracker.sample()
        self.is_focused = True  # check_focus(position)

        while time.time()*10000 - t0 < self.delta_t:
            pass

        if self.is_focused:
            idx = self.iter_ % 2
            self.screen.clear()
            self.screen.draw_image(self.images[idx])
            self.display.fill(self.screen)
            self.display.show()
            self.iter_ += 1

    def start(self):
        '''Calls the hidden _flash() method.
        '''
        self.iter_ = 0
        while self.iter_ < self.n_iters:
            self._flash()

        self.display.close()
        # self.eyetracker.stop_recording()
        #sys.exit()

    def show(self, image):
        self.screen.clear()
        self.screen.draw_image(image)
        self.display.fill(self.screen)
        self.display.show()

    def calibrate(self):
        self.eyetracker.calibrate()
        return self


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
