import tkinter as tk
from PIL import ImageTk as itk
import datetime as dt


class task(object):
    '''Display k image reversals that switch every delta_t milliseconds. Pauses
       image switching if is_looking signal is False.
    '''
    def __init__(self, images, n_iterations=500, delta_t=1):
        self.images = images
        self.delta_t = delta_t

    def start(self):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=1024, height=768)

        image1 = tk.PhotoImage(file=self.images[0])
        image2 = tk.PhotoImage(file=self.images[1])

        switch_images(image1, image2, canvas, delta_t=self.delta_t)
        root.mainloop()


def switch_images(image1, image2, canvas, delta_t=100):
    time_start = dt.now().microsecond
    canvas.delete('all')

    calc_delta_time_ms = lambda time1, time2: (time2 - time1) * 1000

    while calc_delta_time_ms(time_start, dt.now.microsecond):
    canvas.create_image(0, 0, image=image1)

    canvas.delete('all')
    canvas.create_image(0, 0, image=image1)
