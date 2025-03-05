import zhtts # type: ignore
import soundfile # type: ignore
import sounddevice as sd # type: ignore
import playsound as ps # type: ignore

def TextToSpeech():
    with open('/Library/WebServer/Documents/AutismHelper/textResponse.txt') as f:
        text = f.read()
    tts = zhtts.TTS() # use fastspeech2 by default
    tts.text2wav(text, "/Library/WebServer/Documents/AutismHelper/response.wav")   #保存到本地 也可保存成mp3格式
    tts.frontend(text)
    tts.synthesis(text)
    ps.playsound('/Library/WebServer/Documents/AutismHelper/response.wav') # 播放保存的wav文件