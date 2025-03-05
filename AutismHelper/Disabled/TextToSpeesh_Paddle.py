import os
import random
import time
import json
import base64
import shutil
 
from paddlespeech.cli.asr.infer import ASRExecutor
from paddlespeech.cli.tts.infer import TTSExecutor
from flask import Flask, request
 

# 公共函数，所有接口都能用
def random_string(length=32): # 生成32位随机字符串，为了生成随机文件名    
    string='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(string) for i in range(length))
 
# 文字转语音
# 只接受POST方法访问
@app.route("/texttospeech",methods=["POST"])
def text_to_speech():
    with open('AutismHelper/textResponse.txt') as f:
        text_str = request.get_json().get(f.read())  # 要转为语音的文字
 
    # tts = TTSExecutor()
    audio_file_name = random_string() + '_' + (str(time.time()).split('.')[0]) + '.wav'
    audio_file_path = '/home/python/speech/text_to_speech/audio_file' + audio_file_name
    tts(text=text_str, output=audio_file_path)  # 输出24k采样率wav格式音频。同speech_to_text()中一样，会在当前代码所在文件夹中产生exp/log文件夹，里面是paddlespeech的日志文件，每一次调用都会生成一个日志文件。
    if os.path.exists(audio_file_path):
        with open(audio_file_path, 'rb') as f:
            base64_str = base64.b64encode(f.read()).decode('utf-8')  # 开头不含'data:audio/wav;base64,'
        
        os.remove(audio_file_path)  # 识别成功时删除转换后的音频文件
        # try:
        #     shutil.rmtree('')  # 删除文件夹，若文件夹不存在会报错。若需删除日志文件夹，用这个。from https://blog.csdn.net/a1579990149wqh/article/details/124953746
        # except Exception as e:
        #     pass
 
        return json.dumps({'code':200, 'msg':'识别成功', 'data':base64_str}, ensure_ascii=False)
    elif not os.path.exists(audio_file_path):
        return json.dumps({'code':400, 'msg':'识别失败'}, ensure_ascii=False)
 