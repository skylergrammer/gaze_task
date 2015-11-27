try:
    import tkinter as tk
except:
    import Tkinter as tk
from PIL import ImageTk, Image
import sys


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
    def __init__(self, root, images,
                 width=500, height=500, autosize=False,
                 n_iters=500, delta_t=100, eyetracker=None):

        self.root = root
        images_open = [Image.open(x) for x in images]
        self.images = [ImageTk.PhotoImage(x) for x in images_open]
        self.delta_t = delta_t
        self.n_iters = n_iters

        # If autosize, then get the dimensions from the first image
        if autosize:
            width, height = images_open[0].size

        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.img = self.canvas.create_image(0, 0, anchor=tk.NW,
                                            image=self.images[0])
        self.iter_ = 0
        self.eyetracker = eyetracker

        if self.eyetracker is not None:
            self.eyetracker.start_recording()
        else:
            sys.exit('ERROR: must attach eyetracker object!')

    def _flash(self):

        '''Hidden method that flashes between the images in images list every
           delta_t milliseconds.
        '''
        # TODO used to store the results of the eye tracking poll
        position = self.eyetracker.sample()
        self.is_focused = check_focus(position)

        if self.iter_ < self.n_iters:
            if self.is_focused:
                self.iter_ += 1
                # Get next image to display
                new_image = self.images[self.iter_ % 2]
                self.last_image = new_image
                # Switch to next image after delta_t milliseconds
                self.canvas.itemconfig(self.img, image=new_image)
                self.canvas.after(self.delta_t, self._flash)
            else:
                self.canvas.itemconfig(self.img, image=self.last_image)
                self.canvas.after(self.delta_t, self._flash)
        else:
            self.eyetracker.stop_recording()
            sys.exit()

    def start(self):
        '''Calls the hidden _flash() method.
        '''
        self._flash()


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
