# python库
import time
import sys

# 来自其他文件的函数
sys.path.append('/Library/WebServer/Documents/AutismHelper') 
from VideoInputAnalysis import VideoInit, VideoSaver, FaceAnalysis
from SpeechRecognition import MicrophoneInput
from InfoCombination import CombiningInput
from InfoCombinationForHistory import HistoryCombination
from GPT import LoadGPTResponse

# 初始化
VideoInit()
time.sleep(0.3)

# GPT功能整合
def GPTFinlFunc():
    VideoSaver()
    FaceAnalysis()
    MicrophoneInput()
    CombiningInput()
    LoadGPTResponse()
    # HistoryCombination() # 简化并记录已知数据