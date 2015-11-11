from gaze_task import Task
import tkinter as tk
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n_iters', default=100)
    parser.add_argument('--height', default=500)
    parser.add_argument('--width', default=500)
    args = parser.parse_args()

    print(args)
    root = tk.Tk()
    task = Task(root, ['red.png', 'blue.jpg'],
                'n_iters'=args.n_iters,
                'height'=args.height,
                'width'=args.width)
    task.start()
    root.mainloop()

if __name__ == '__main__':
    main()
