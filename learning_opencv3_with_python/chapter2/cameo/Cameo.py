import cv2
from learning_opencv3_with_python.chapter2.cameo.CaptureManager import CaptureManager
from learning_opencv3_with_python.chapter2.cameo.WindowManager import WindowManager
from learning_opencv3_with_python.chapter2.cameo.filters import *


class Cameo(object):

    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeyPress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)
        self._curveFilter = EmbossFilter()

    def run(self):
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame

            # -----
            strokeEdges(frame, frame)
            self._curveFilter.apply(frame, frame)
            # -----

            self._captureManager.exiFrame()
            self._windowManager.processEvents()

    def onKeyPress(self, keycode):
        if keycode == 32:  # space键
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9:  # Tab键
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('screenvideo.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27:  # Esc键
            self._windowManager.destroyWindow()


if __name__ == '__main__':
    Cameo().run()
