import os
import random
import time
import json
import base64
import shutil
 
from paddlespeech.cli.asr.infer import ASRExecutor
from paddlespeech.cli.tts.infer import TTSExecutor
from flask import Flask, request
 
app=Flask(__name__)
asr = ASRExecutor()  # 初始化成全局变量，防止多次初始化导致显存不够 from https://github.com/PaddlePaddle/PaddleSpeech/issues/2881和https://github.com/PaddlePaddle/PaddleSpeech/issues/2908
tts = TTSExecutor()
 
# 公共函数，所有接口都能用
def random_string(length=32): # 生成32位随机字符串，为了生成随机文件名    
    string='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(string) for i in range(length))
 
# 公共函数，所有接口都能用
def base64_to_audio(audio_base64, folder_name=None):  # 服务器上用folder_name参数，用于在audio_file_path中拼接路径，如f'/home/www/card/{folder_name}/'，不同的folder_name对应不同的识别任务(如身份证识别、营业执照识别)，本地测试不用
    audio_base64 = audio_base64.split(',')[-1]
    audio = base64.b64decode(audio_base64)
    audio_file_name = random_string() + '_' + (str(time.time()).split('.')[0])  # 不带扩展名，因为不知道收到的音频文件的原始扩展名，手机录的不一定是什么格式
    audio_file_path = f'/home/python/speech/{folder_name}/' + audio_file_name
    with open(audio_file_path, 'wb') as f:
        f.write(audio)
    return audio_file_path
 
# 将收到的音频文件转为16k 16 bit 1 channel的wav文件，16k表示16000Hz的采样率，16bit不知道是什么
# 若给paddlespeech传的文件不对，会提示The sample rate of the input file is not 16000.The program will resample the wav file to 16000.If the result does not meet your expectations，Please input the 16k 16 bit 1 channel wav file.所以要提前转换。
def resample_rate(audio_path_input):
    audio_path_output = audio_path_input + '_output' + '.wav'  # 传入的audio_path_input不带扩展名，所以后面直接拼接字符串
    command = f'ffmpeg -y -i {audio_path_input}  -ac 1 -ar 16000  -b:a 16k  {audio_path_output}'  # 这个命令输出的wav文件，格式上和PaddleSpeech在README中给的示例zh.wav(https://paddlespeech.bj.bcebos.com/PaddleAudio/zh.wav，内容是'我认为跑步最重要的就是给我带来了身体健康')一样。from https://blog.csdn.net/Ezerbel/article/details/124393431
    command_result = os.system(command)  # from https://blog.csdn.net/liulanba/article/details/115466783
    assert command_result == 0
    if os.path.exists(audio_path_output):
        return audio_path_output
    elif not os.path.exists(audio_path_output):  # ffmpeg输出的文件不存在，可能是ffmpeg命令没执行完，等1秒(因在虚拟机测试转一个8.46M的MP3需0.48秒)，1秒后若还没有输出文件，说明报错了
        time.sleep(1)
        if os.path.exists(audio_path_output):
            return audio_path_output
        else:
            return None
 
# 语音转文字
# 只接受POST方法访问
@app.route("/speechtotext",methods=["POST"])
def speech_to_text():
    audio_file_base64 = request.get_json().get('audio_file_base64')  # 要转为文字的语音文件的base64编码，开头含不含'data:audio/wav;base64,'都行
    audio_file_path = base64_to_audio(audio_file_base64, folder_name='speech_to_text/audio_file')  # 存放收到的原始音频文件
 
    audio_path_output = resample_rate(audio_path_input=audio_file_path)
    if audio_path_output:
        # asr = ASRExecutor()
        result = asr(audio_file=audio_path_output)  # 会在当前代码所在文件夹中产生exp/log文件夹，里面是paddlespeech的日志文件，每一次调用都会生成一个日志文件。记录这点时的版本号是paddlepaddle==2.3.2，paddlespeech==1.2.0。 from https://github.com/PaddlePaddle/PaddleSpeech/issues/1211
        
        os.remove(audio_file_path)  # 识别成功时删除收到的原始音频文件和转换后的音频文件
        os.remove(audio_path_output)
        # try:
        #     shutil.rmtree('')  # 删除文件夹，若文件夹不存在会报错。若需删除日志文件夹，用这个。from https://blog.csdn.net/a1579990149wqh/article/details/124953746
        # except Exception as e:
        #     pass
 
        return json.dumps({'code':200, 'msg':'识别成功', 'data':result}, ensure_ascii=False)
    else:
        return json.dumps({'code':400, 'msg':'识别失败'}, ensure_ascii=False)
 
# 文字转语音
# 只接受POST方法访问
@app.route("/texttospeech",methods=["POST"])
def text_to_speech():
    text_str = request.get_json().get('text')  # 要转为语音的文字
 
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
 
if __name__=='__main__':
    app.run(host='127.0.0.1', port=9723)
