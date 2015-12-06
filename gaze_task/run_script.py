#!/usr/bin/env python
from gaze_task.framework import Task
import argparse
import sys
from PyQt4 import QtGui
from argparseui import ArgparseUi
from pygaze.libscreen import Display, Screen
from pygaze.eyetracker import EyeTracker


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
    parser.add_argument('--resolution', nargs=2)
    parser.add_argument('--calibrate', default=False, action='store_true',
                        help='Set to perform a calibration first.')
    app = QtGui.QApplication(sys.argv)
    a = ArgparseUi(parser,
                   use_save_load_button=True,
                   window_title='Run Image Flash Task'
                   )
    a.show()
    app.exec_()
    args = a.parse_args()

    display = Display(disptype='psychopy', screennr=1,
                      dispsize=args.resolution)
    screen = Screen(disptype='psychopy')
    images = []
    images.append(args.image1)
    images.append(args.image2)
    tobii = EyeTracker(display, trackertype='tobii')

    task = Task(screen, display, images,
                delta_t=args.timing,
                n_iters=args.n_iters,
                eyetracker=tobii)
    if args.calibrate:
        task.calibrate()

    task.start()
    display.close()

if __name__ == '__main__':
    main()
