import requests
from flask import Flask, request

app = Flask(__name__)
# app.secret_key = 'security-guard'

@app.route('/chat', methods=['POST'])
def chat():
    api_key = request.json['api_key']
    question = request.json['question']  # 获取表单数据
    # Your OpenAI API Key
    api_key = "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"
    # The text prompt you want to generate a response
    # The URL for OpenAI's API
    url = "https://kmbase.eu.org/v1/chat/completions"
    # The headers for the API request
    headers = {"Content-Type": "application/json","Authorization": f"Bearer {api_key}"}
    data = {"model":"gpt-3.5-turbo","messages": [{"role":"user","content":question}],"max_tokens":800,"temperature":0.5,"frequency_penalty":0,"presence_penalty":0}
    # Make the API request
    response = requests.post(url, headers=headers, json=data)
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the generated text from the response
        generated_text = response.json()['choices'][0]['message']['content']
        usage = response.json()['usage']
        print(generated_text)
        print(usage)
    else:
        # Handle the error
        print(f"Request failed with status code {response.status_code}")
    return generated_text

# 启动Flask Web服务
if __name__ == '__main__':
    # app.run(host=sys.argv[1], port=sys.argv[2])
    app.run()
