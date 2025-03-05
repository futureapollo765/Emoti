import zhtts
import soundfile
import sounddevice as sd

def TextToSpeech():
    with open('AutismHelper/textResponse.txt') as f:
        text = f.read()
    tts = zhtts.TTS() # use fastspeech2 by default
    tts.text2wav(text, "AutismHelper/demo.wav")   #保存到本地，使用视频播放器打开，也可保存成mp3格式
    tts.frontend(text)
    tts.synthesis(text)
    with open('AutismHelper/demo.wav') as f:
        sd.play(f.read(), samplerate=24000) # samplerate=24000为通过其他包转换为.wav文件，再读取该文件获取的
        sd.wait()