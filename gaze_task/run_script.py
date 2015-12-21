#!/usr/bin/env python
from gaze_task.framework import Task, FakeEyeTracker
import argparse
import sys
from PyQt4 import QtGui
from argparseui import ArgparseUi
from pygaze.libscreen import Display
from pygaze.eyetracker import EyeTracker
from PIL import Image
import tkMessageBox
try:
    import Tkinter as tkinter
except:
    import tkinter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('image1', type=str,
                        help='Required: Filename for image 1')
    parser.add_argument('image2', type=str,
                        help='Required: Filename for image 2')
    parser.add_argument('--n_iters', type=int, default=10,
                        help='Number of iterations [default=10]')
    parser.add_argument('--timing', default=1000,
                        help='Duration displayed for each image in millis.')
    parser.add_argument('--displaynumber', default=1, type=int,
                        help='Monitor to show the task.')
    parser.add_argument('--resolution', default='1920 1080', type=str,
                        help='The dimensions of the display in pixels e.g. 1920 1080')
    parser.add_argument('--testing', action='store_true', default=False)
    app = QtGui.QApplication(sys.argv)
    a = ArgparseUi(parser,
                   use_save_load_button=True,
                   window_title='Run Image Flash Task'
                   )
    a.show()
    app.exec_()
    args = a.parse_args()
    resolution = [int(x) for x in args.resolution.split()]
    display = Display(disptype='psychopy',
                      dispsize=resolution,
                      screennr=args.displaynumber)
    screen_params = dict(disptype='psychopy',
                         dispsize=resolution,
                         screennr=args.displaynumber
                         )
    images = []
    images.append(args.image1)
    images.append(args.image2)
    try:
        open_images = [Image.open(x) for x in images]

    except Exception:
        err_msg = "The image(s) %s and %s do not appear to be the correct filename or path" % tuple(images)
        window = tkinter.Tk()
        window.wm_withdraw()
        tkMessageBox.showinfo(title="ERROR: Unable to open images",
                              message=err_msg)
        window.destroy()
        sys.exit()
    if args.testing:
        tobii = FakeEyeTracker()
        print("Using FakeEyeTracker.")
    else:
        tobii = EyeTracker(display, trackertype='tobii')
        print("Using real EyeTracker")

    task = Task(screen_params, display, open_images,
                delta_t=args.timing,
                n_iters=args.n_iters,
                eyetracker=tobii)

    task.start()
    display.close()

if __name__ == '__main__':
    main()
