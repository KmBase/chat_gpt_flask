import sys
import requests
import flask,json
from gevent import pywsgi

from flask import Flask, request

app = Flask(__name__)
app.secret_key = 'security-guard'

@app.route('/chat',methods=['post'])
def chat():
    data = request.data.decode('utf-8').replace("\'","\"")
    data= json.loads(data)
    print(data)
    question = data['msg']['question']  # 获取表单数据
    proxy_url = data['msg']['proxy_url']
    api_key = data['msg']['api_key']
    print(question)
    # The text prompt you want to generate a response
    # The URL for OpenAI's API
    url = f"{proxy_url}/v1/chat/completions"
    # The headers for the API request
    headers = {"Content-Type": "application/json","Authorization": f"Bearer {api_key}"}
    data = {"model":"gpt-3.5-turbo","messages": [{"role":"user","content":question}],"max_tokens":800,"temperature":0.5,"frequency_penalty":0,"presence_penalty":0}
    # Make the API request
    response = requests.post(url, headers=headers, json=data)
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the generated text from the response
        # generated_text = response.json()['choices'][0]['message']['content']
        # usage = response.json()['usage']
        # print(generated_text)
        # print(usage)
        res = response.json()
        return res
    else:
        # Handle the error
        # generated_text = None
        # usage = None
        print(f"Request failed with status code {response.status_code}")
        return None


# 启动Flask Web服务
if __name__ == '__main__':
    server = pywsgi.WSGIServer((sys.argv[1], sys.argv[2]), app)
    server.serve_forever()