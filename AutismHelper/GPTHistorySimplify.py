import os
import openai


def LoadGPTHistoryResponse():
    # optional; defaults to `os.environ['OPENAI_API_KEY']`
    openai.api_key = "sk-mII7kWmU5LrlG4Da4c512d59F0454b74Ab94702dF887A325"

    # all client options can be configured just like the `OpenAI` instantiation counterpart
    openai.base_url = "https://free.v36.cm/v1/"
    openai.default_headers = {"x-foo": "true"}

    # 上传信息
    with open('/Library/WebServer/Documents/AutismHelper/historyInfo.txt', 'r') as f:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f.read(),
                },
            ],
        )
        textResponse = completion.choices[0].message.content
        with open('/Library/WebServer/Documents/AutismHelper/History.txt', 'w', encoding='utf-8') as f: 
            f.write(textResponse)