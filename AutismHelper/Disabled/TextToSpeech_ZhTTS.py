import zhtts
import soundfile
import sounddevice as sd
def TextToSpeech():
    tts = zhtts.TTS()  # use fastspeech2 by default
    with open('AutismHelper/textResponse.txt', 'r') as f:
        text1 = f.read()

    # 下面是自带的函数，借助Pycharm查看出来的。audio为numpy数组可直接传入播放器。
    """
    mel = tts.text2mel(text1)
    print(mel.shape, type(mel))
    audio = tts.mel2audio(mel)
    print(audio, type(audio))
    """
    audio = tts.text2wav(text1, 'AutismHelper.textResponse.wav')
    # 下面这里可以先看【6.sounddevice播放音频】
    sd.play(audio, samplerate=24000) # samplerate=24000为通过其他包转换为.wav文件，再读取该文件获取的
    sd.wait()
    path = 'AutismHelper/AudioClip.wav'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(str(audio))

    devs=sd.query_devices()  #返回系统所有的声音设备
    print(devs) # 带><的是默认播放设备
    # 1 代表设备号；麦克风阵列 (Synaptics Audio)代表设备名称；MME (2 in, 0 out)代表驱动为MME和2个输入通道
    """
    0 Microsoft Sound Mapper - Input, MME (2 in, 0 out)
    >  1 麦克风阵列 (Synaptics Audio), MME (2 in, 0 out)
    2 Microsoft Sound Mapper - Output, MME (0 in, 2 out)
    <  3 扬声器 (Synaptics Audio), MME (0 in, 2 out)
    4 主声音捕获驱动程序, Windows DirectSound (2 in, 0 out)
    5 麦克风阵列 (Synaptics Audio), Windows DirectSound (2 in, 0 out)
    6 主声音驱动程序, Windows DirectSound (0 in, 2 out)
    7 扬声器 (Synaptics Audio), Windows DirectSound (0 in, 2 out)
    8 扬声器 (Synaptics Audio), Windows WASAPI (0 in, 2 out)
    9 麦克风阵列 (Synaptics Audio), Windows WASAPI (2 in, 0 out)
    10 麦克风阵列 1 (Synaptics Audio capture), Windows WDM-KS (2 in, 0 out)
    11 麦克风阵列 2 (Synaptics Audio capture), Windows WDM-KS (4 in, 0 out)
    12 麦克风阵列 3 (Synaptics Audio capture), Windows WDM-KS (4 in, 0 out)
    13 Output 1 (Synaptics Audio output), Windows WDM-KS (0 in, 2 out)
    14 Output 2 (Synaptics Audio output), Windows WDM-KS (0 in, 8 out)
    15 Input (Synaptics Audio output), Windows WDM-KS (2 in, 0 out)
    16 耳机 (@System32\drivers\bthhfenum.sys,#2;%1 Hands-Free AG Audio%0
    ;(iGene-U2)), Windows WDM-KS (0 in, 1 out)
    17 耳机 (@System32\drivers\bthhfenum.sys,#2;%1 Hands-Free AG Audio%0
    ;(iGene-U2)), Windows WDM-KS (1 in, 0 out)
    18 耳机 (), Windows WDM-KS (0 in, 2 out)
    """

TextToSpeech()