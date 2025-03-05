import json

origFilePath = '/Library/WebServer/Documents/AutismHelper/textResponse.txt'
finlFilePath = 'text.json'
response = ""

def LoadJsonFile(filePath, targetJson):
    with open(filePath, 'r') as f:
        origText = f.read()
    with open(targetJson, 'w', encoding="utf-8") as f:
        f.write(json.dumps(origText))

def DecodeJsonFile(targetJson):
    with open(targetJson, 'r') as f:
        response = json.load(f)
        print(response)
        return response

def JsonCombined(filePath, targetJson):
    LoadJsonFile(filePath, targetJson)
    response = DecodeJsonFile(targetJson)
    return response