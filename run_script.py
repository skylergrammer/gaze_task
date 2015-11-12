#!/usr/bin/env python
from gaze_task import Task
import tkinter as tk
import argparse
import sys
from PyQt4 import QtGui
from argparseui import ArgparseUi

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image1', type=str, required=True,
                        help='Required: Filename for image 1')
    parser.add_argument('--image2', type=str, required=True,
                        help='Required: Filename for image 2')
    parser.add_argument('--n_iters', type=int, default=100,
                        help='Number of iterations [default=100]')
    parser.add_argument('--height', default=500,
                        help='Height in pixels [default=500]')
    parser.add_argument('--width', default=500,
                        help='Width in pixels [default=500]')
    parser.add_argument('--autosize', action='store_true', default=False,
                        help='Will automatically find image size.')
    parser.add_argument('--timing', default=500,
                        help='Duration displayed for each image in millis.')
    app = QtGui.QApplication(sys.argv)
    a = ArgparseUi(parser,
                   use_save_load_button=True,
                   window_title='Run Image Flash Task'
                   )
    a.show()
    app.exec_()
    args = a.parse_args()

    images = [args.image1, args.image2]
    root = tk.Tk()
    task = Task(root, images,
                n_iters=args.n_iters,
                height=args.height,
                width=args.width,
                delta_t=args.timing,
                autosize=args.autosize)
    task.start()
    root.mainloop()

if __name__ == '__main__':
    main()
