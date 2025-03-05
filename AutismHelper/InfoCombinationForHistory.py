from GPTHistorySimplify import LoadGPTHistoryResponse
from HistoryRecord import RecordInfo

def HistoryCombination():

    RecordInfo()
    # GPT前置要求
    with open('/Library/WebServer/Documents/AutismHelper/HistoryPrompts.txt', 'r') as f:
        prompts = f.read()

    # 面部信息
    with open('/Library/WebServer/Documents/AutismHelper/history.txt', 'r') as f:
        history = f.read()

    # 信息整合
    with open('/Library/WebServer/Documents/AutismHelper/historyInfo.txt', 'w', encoding='utf-8') as f:
        f.write(prompts)
        f.write(history)
    LoadGPTHistoryResponse()