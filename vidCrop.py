#!/usr/bin/python

import sys
import cv2 as cv
# import gui

if __name__ == '__main__':
    # vidCrop vid.mp4 100 100

    # vidCrop
    # -i for image
    # -v for video (default)

    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))

    if (len(sys.argv) < 2):
        print("TODO Launch GUI")
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
