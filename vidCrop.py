#!/usr/bin/python

import sys
import cv2 as cv
import tkinter as tk
# import gui

if __name__ == '__main__':
    # vidCrop vid.mp4 100 100

    # vidCrop
    # -i for image
    # -v for video (default)

    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))

    # TODO FINISH GUI https://www.youtube.com/watch?v=D8-snVfekto
    if (len(sys.argv) < 2):
        root = tk.Tk()
        canvas = tk.Canvas(root, height=600, width=800)
        canvas.pack()

        frame = tk.Frame(root, bg="gray")
        frame.place(relx=0.05, rely=0.05, relwidth=0.95, relheight=0.95)

        xButton = tk.Button(frame, text="X Slider and Text Box")
        xButton.pack()
        yButton = tk.Button(frame, text="Y Slider and Text Box")
        yButton.pack()

        upload = tk.Button(root, text="Upload a file")
        upload.pack()

        root.mainloop()
        # GUI Collect Arguments
        # GUI feed arguments too CLI
    else:
        filepath = sys.argv[1]
        x = sys.argv[2]
        y = sys.argv[3]

        try:
            cap = cv.VideoCapture(filepath)
        except IOError as exc:
            raise RuntimeError('Cannot Open ', filepath) from exc

        length = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

        success, img = cap.read()
        while success:
            sucess, img = cap.read()
            img = cv.resize(img, (x, y))
