import cv2 as cv

'''
捕获摄像头的帧并保存到本地视频文件
'''

# 获取摄像头
camera = cv.VideoCapture(0)
# 由于VideoCapture的get()方法不能返回摄像头帧速率的准确值，所以这里自定义一个值
fps = 30
# 获得摄像头帧图像大小
size = (int(camera.get(cv.CAP_PROP_FRAME_WIDTH)), int(camera.get(cv.CAP_PROP_FRAME_HEIGHT)))
# 创建到本地文件的输出
videoWriter = cv.VideoWriter('my-camera.avi', cv.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
# 读取摄像头帧，如果读取失败， success == False
success, frame = camera.read()
# 设置只读取10s的摄像头帧
left = 10 * fps - 1
while success and left > 0:
    # 写入帧到输出中
    videoWriter.write(frame)
    success, frame = camera.read()
    left -= 1
camera.release()
print("done!")

'''
备注：cv.VideoWriter_fourcc('I', '4', '2', '0') 是一个未压缩的YUV颜色编码，是4：2：0色度子采样。这种编码有很好的兼容性，但会产生较大文件，文件扩展名为.avi
    其他常用选项：
        cv.VideoWriter_fourcc('P', 'I', 'M', '1') MPEG-1编码类型，文件扩展名为.avi
        cv.VideoWriter_fourcc('X', 'V', 'I', 'D') MPEG-4编码类型，如果希望得到的视频大小为平均值，推荐使用此选项，文件扩展名为.avi
        cv.VideoWriter_fourcc('T', 'H', 'E', 'O') Ogg Vorbis，文件扩展名为.ogv
        cv.VideoWriter_fourcc('F', 'L', 'V', '1') Flash视频，文件扩展名为.flv
    
'''