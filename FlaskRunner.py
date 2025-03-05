from flask import Flask, render_template, request, redirect, globals
import threading
from jsonSaver import JsonCombined
from AutismHelper.FunctionCombined import GPTFinlFunc
import sys
from AutismHelper.VideoInputAnalysis import VideoInit
import time

# 配置文件
sys.path.append('/Library/WebServer/Documents/AutismHelper')
lock = threading.Lock()
origFilePath = '/Library/WebServer/Documents/AutismHelper/textResponse.txt'
finlFilePath = 'text.json'
response = ""
app = Flask(__name__)


# HTML变量定义输出
@app.route("/Library/WebServer/Documents/AutismHelper/index.html",methods=['GET', 'POST'])
def index():
    return render_template("/Library/WebServer/Documents/AutismHelper/index.html", textResponse = response) 

# 定义并行
t1 = threading.Thread(target=GPTFinlFunc)
# t2 = threading.Thread(target=app.run)

# 执行
try:

    while True:
        GPTFinlFunc()
    # if __name__ == '__main__':
    #     response = JsonCombined(origFilePath, finlFilePath)
    #     t1.start()
    #     time.sleep(1)
    #     # t2.start()
    #     time.sleep(0.1)
    #     t1.join()
    #     # t2.join()
except KeyboardInterrupt:
    print("End")