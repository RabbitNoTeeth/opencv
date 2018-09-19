import cv2 as cv

'''
视频文件的读、写
'''

# 加载本地视频文件
videoInput = cv.VideoCapture('my-video.avi')
fps = videoInput.get(cv.CAP_PROP_FPS)
size = (int(videoInput.get(cv.CAP_PROP_FRAME_WIDTH)), int(videoInput.get(cv.CAP_PROP_FRAME_HEIGHT)))
# 创建到本地文件的输出
videoWriter = cv.VideoWriter('my-video-copy.avi', cv.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
# 读取输入文件，如果读取失败， success == False
success, frame = videoInput.read()
while success:
    # 写入帧到输出中
    videoWriter.write(frame)
    success, frame = videoInput.read()
print("done!")

'''
备注：cv.VideoWriter_fourcc('I', '4', '2', '0') 是一个未压缩的YUV颜色编码，是4：2：0色度子采样。这种编码有很好的兼容性，但会产生较大文件，文件扩展名为.avi
    其他常用选项：
        cv.VideoWriter_fourcc('P', 'I', 'M', '1') MPEG-1编码类型，文件扩展名为.avi
        cv.VideoWriter_fourcc('X', 'V', 'I', 'D') MPEG-4编码类型，如果希望得到的视频大小为平均值，推荐使用此选项，文件扩展名为.avi
        cv.VideoWriter_fourcc('T', 'H', 'E', 'O') Ogg Vorbis，文件扩展名为.ogv
        cv.VideoWriter_fourcc('F', 'L', 'V', '1') Flash视频，文件扩展名为.flv
    
'''