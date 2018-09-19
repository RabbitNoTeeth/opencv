import cv2

'''
在窗口显示摄像头帧
'''

clicked = False


def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True


camera = cv2.VideoCapture(0)
cv2.namedWindow("my-camera")
cv2.setMouseCallback('my-camera', onMouse)

success, frame = camera.read()
while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('my-camera', frame)
    success, frame = camera.read()

cv2.destroyAllWindows()
camera.release()
