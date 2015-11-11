import tkinter as tk
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
       weidgh : int
                width of canvas in number of pixels
    '''
    def __init__(self, root, images,
                 width=500, height=500, n_iters=500, delta_t=100):
        self.root = root
        self.images = [ImageTk.PhotoImage(Image.open(images[0])),
                       ImageTk.PhotoImage(Image.open(images[1]))]
        self.delta_t = delta_t
        self.n_iters = n_iters

        self.n_images = len(self.images)
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.img = self.canvas.create_image(0, 0, anchor=tk.NW,
                                            image=self.images[0])
        self.iter_ = 0

    def flash(self):
        '''Flashes between the images in images list every delta_t milliseconds.
        '''
        self.is_focused = True # fake_eye_tracker(self.iter_)

        if self.iter_ < self.n_iters:
            if self.is_focused:
                self.iter_ += 1
                # Get next image to display
                new_image = self.images[self.iter_ % self.n_images]
                self.last_image = new_image

                # Switch to next image after delta_t milliseconds
                self.canvas.itemconfig(self.img, image=new_image)
                self.canvas.after(self.delta_t, self.flash)
            else:
                self.canvas.itemconfig(self.img, image=self.last_image)
                self.canvas.after(self.delta_t, self.flash)

        else:
            sys.exit()

    def start(self):
        self.flash()


def fake_eye_tracker(iter_):
    if iter_ % 5 == 0 and iter_ > 0:
        return False
    else:
        return True
