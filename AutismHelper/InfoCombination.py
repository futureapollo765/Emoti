def CombiningInput():
    
    # GPT前置要求
    with open('/Library/WebServer/Documents/AutismHelper/Prompts.txt', 'r') as f:
        prompts = f.read()

    # 历史记录
    with open('/Library/WebServer/Documents/AutismHelper/History.txt', 'r') as f:
        historyContent = f.read()

    # 面部信息
    with open('/Library/WebServer/Documents/AutismHelper/faceAnalysis.txt', 'r') as f:
        faceAnalysisContent = f.read()

    # 语音识别结果
    with open('/Library/WebServer/Documents/AutismHelper/recogResult.txt', 'r') as f:
        textRecogResultContent = f.read()

    # 信息整合
    with open('/Library/WebServer/Documents/AutismHelper/inputCombined.txt', 'w', encoding='utf-8') as f:
        f.write(prompts)
        f.write(historyContent)
        f.write(faceAnalysisContent)
        f.write(textRecogResultContent)
