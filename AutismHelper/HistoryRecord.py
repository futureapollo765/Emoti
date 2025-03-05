def RecordInfo():

    # 面部识别结果
    with open('/Library/WebServer/Documents/AutismHelper/faceAnalysis.txt', 'r') as f:
        faceAnalysisContent = f.read()

    # 语音识别结果
    with open('/Library/WebServer/Documents/AutismHelper/recogResult.txt', 'r') as f:
        textRecogResultContent = f.read()

    # 回答
    with open('/Library/WebServer/Documents/AutismHelper/textResponse.txt', 'r') as f:
        response = f.read()
    
    #整合
    with open('/Library/WebServer/Documents/AutismHelper/history.txt', 'a', encoding='utf-8') as f:
        f.write('Known Information')
        f.write('  1. Facial Recognition Result')
        f.write(faceAnalysisContent)
        f.write('  2. Speech to Text Result')
        f.write(textRecogResultContent)
        f.write('  3. Generated Response')
        f.write(response)