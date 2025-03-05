import speech_recognition as sr # type: ignore
from scipy.io import savemat # type: ignore


recognizer = sr.Recognizer()
user_lang = 'zh_CN'

# 修改vosk输出结果
def EditResult(resu):
    start = resu.index('"', resu.index('"', resu.index('"') + 1) + 1) + 1
    end = resu.index('"', start)
    return resu[start:end]

def MicrophoneInput():

    # 调用麦克风
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        print("Say something")
        audio = recognizer.listen(source)

        try: # 可以选择不同的数据源从而识别不同的语言

            # Google 识别库
            text = recognizer.recognize_google(audio, language = user_lang)
            print("You said : {}".format(text))

            # vosk 离线识别库（问题未解决）
            # text = recognizer.recognize_vosk(audio)
            # EditResult(text)
            # print('you said : {}'.format(text))

        except:
            print("Sorry I can't hear you!")
            text = 'unknown'

    # 保存识别结果
    with open('/Library/WebServer/Documents/AutismHelper/recogResult.txt', 'w', encoding = 'utf-8') as f:
            f.write("User Said: " + str(text))