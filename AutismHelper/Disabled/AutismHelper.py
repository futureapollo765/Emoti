# FutureApollo Studio Presents
# UTF-8


import urllib.request
import urllib.error
import time
import keyboard
import cv2
import numpy as n
import os

# 绝对路径确认
currentDirectory = os.getcwd() # 获取文件路径
relDirectory = 'AutismHelper/UserPics/1face.png' # 图像相对路径
fullDirectory = os.path.join(currentDirectory, relDirectory) # 整合路径


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
  cv2.imwrite(fullDirectory, frame) # 截图 fullDirectory为路径 frame为此时的图像
  takeTimer = 0 # 清零

# 接入f++API并输出结果
def FaceAnalysis():
  http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
  key = "2ITvmFxZVeh1xh9q2mjqGrxWlts7G84R"
  secret = "JXOz68WSiL4WRU9ze73-3nff6sIrwu1M"
  boundary = '----------%s' % hex(int(time.time() * 1000))
  data = []
  data.append('--%s' % boundary)
  data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key') # API密钥
  data.append(key)
  data.append('--%s' % boundary)
  data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret') # API密钥
  data.append(secret)
  data.append('--%s' % boundary)
  fr = open(fullDirectory, 'rb')
  data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
  data.append('Content-Type: %s\r\n' % 'application/octet-stream')
  data.append(fr.read())
  fr.close()
  data.append('--%s' % boundary)
  data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_landmark') # 人脸关键点
  data.append('0')
  data.append('--%s' % boundary)
  data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes') # 脸部信息
  data.append("gender,age,emotion,ethnicity") # 可选信息 gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus
  data.append('--%s--\r\n' % boundary)

  for i, d in enumerate(data):
    if isinstance(d, str):
      data[i] = d.encode('utf-8')

  http_body = b'\r\n'.join(data)

  # build http request
  req = urllib.request.Request(url=http_url, data=http_body)

  # header
  req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)

  try:

    # post data to server
    resp = urllib.request.urlopen(req, timeout=5)

    # get response
    qrcont = resp.read()

    # if you want to load as json, you should decode first,
    # for example: json.loads(qrount.decode('utf-8'))
    # print(qrcont.decode('utf-8'))
    with open('AutismHelper/faceAnalysis.txt', 'w', encoding = 'utf-8') as f:
      f.write('目前交流对象的状态信息（使用gender, age, emotion, ethnicity类型后的变量来分析对应信息，注意跳过所有没有数据的变量）。' + qrcont.decode('utf-8'))
    print(qrcont.decode('utf-8'))
  except urllib.error.HTTPError as e:
    # print(e.read().decode('utf-8'))
    with open('AutismHelper/faceAnalysis.txt', 'w', encoding = 'utf-8') as f:
      f.write('非常不幸，我们并没有搜集到目前交流对象的状态信息，请以相对平均的水平来预计当前交流对象的状态。')
    print('unknown')




# 主循环
VideoInit()
time.sleep(0.5) # 等待摄像头启动  
while True:
  VideoSaver()
  time.sleep(0.5) # 保存后等待文件更新
  FaceAnalysis()
  time.sleep(0.5) # 输入结果后等待防止API停止响应