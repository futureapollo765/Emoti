import cv2

takeTimer = 0

# 初始化摄像头
def VideoInit():
  print('开始')
  global capture
  capture = cv2.VideoCapture(0) # 电脑自身摄像头
  global takeTimer
  takeTimer = 0

# 拍摄并保存
def VideoSaver():
  global takeTimer
  takeTimer += 1
  reg, frame = capture.read()
  frame = cv2.flip(frame, 1) # 图片左右调换
  cv2.imshow('window', frame)
  fileName = '1face.png' # filename为图像名字
  cv2.imwrite(fullDirectory, frame) # 截图 前面为路径 frame为此时的图像
  print(fileName + '保存成功') # 打印保存成功
  takeTimer = 0 # 清零
  print(fullDirectory)
 