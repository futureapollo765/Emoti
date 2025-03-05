# FutureApollo Studio Presents
# UTF-8


import urllib.request
import urllib.error
import time
#import keyboard
import cv2
#import numpy as n
import os

# 绝对路径确认
currentDirectory = os.getcwd() # 获取文件路径
relDirectory = 'AutismHelper/UserPics/1face.png' # 图像相对路径
fullDirectory = os.path.join(currentDirectory, relDirectory) # 整合路径
global takeTimer
takeTimer = 0

# 初始化摄像头
def VideoInit():
  print('开始')
  global capture
  #takeTimer = 0
  capture = cv2.VideoCapture(0,) # 电脑自身摄像头
  time.sleep(1)

# 拍摄并保存
def VideoSaver():
  global takeTimer
  takeTimer += 1
  reg, frame = capture.read()
  print(reg)
  frame = cv2.flip(frame, 1) # 图片左右调换
  fileName = '1face.png' # filename为图像名字
  cv2.imwrite(fullDirectory, frame) # 截图 fullDirectory为路径 frame为此时的图像
  takeTimer = 0 # 清零

# 接入f++API并输出结果
def FaceAnalysis():
  http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
  key = "EL2OUXpSEc3LW80thJuQy1IhM9yPSxWo"
  secret = "akE-bjvapFCaElIfZ0b9WSUEhpF6AWes"
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
      f.write('Current user condition(use data after, "gender, age, emotion, ethnicity" to analyze user condition, skip variables without a corresponding data).' + qrcont.decode('utf-8'))
    print(qrcont.decode('utf-8'))
  except urllib.error.HTTPError as e:
    # print(e.read().decode('utf-8'))
    with open('AutismHelper/faceAnalysis.txt', 'w', encoding = 'utf-8') as f:
      f.write('no information collected, use average instead.')
    print('unknown')