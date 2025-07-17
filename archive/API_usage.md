## 调用LLM API的两种方式

### 一、HTTP 直接请求
```python
# an example
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

data = {
    'model': 'gpt-3.5-turbo',
    'messages': [
        {'role': 'user', 'content': prompt}
    ]
    # Here could also be temperature...etc
}

response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data, timeout=10)
```
1. Content types include:
    * `text/` - 文本数据（如 text/html, text/plain）  
    * `image/` - 图片数据（如 image/png, image/jpeg）  
    * `video/` - 视频数据（如 video/mp4）  
    * `application/` - 应用程序数据（如 application/json, application/pdf）  

    JSON属于结构化的应用程序数据，所以用 application/json。上面的代码属于python dictionary，但是可以轻松转变为json格式。

2. Chat Completions API 模拟对话，`messages` 是一个消息数组，每个消息有 `role` 和 `content`。

    `role` 可以是：  
    * `user`：用户输入的请求或问题。  
    * `assistant`：模型的回复。  
    * `system`：系统指令，用于设置模型的行为（如“以简洁的方式回答”）。


### 二、使用SDK库

SDK，software development kit，一个打包集成好的工具库。  

```python
#OpenAI documentation, retrieved from June 28, 2025. 

from openai import OpenAI

client = OpenAI() #this will load your key directly. BUT u need to set your key as an environment variable. It does not read from the .env document.

response = client.responses.create(
  model="gpt-4.1",
  input="Tell me a three sentence bedtime story about a unicorn."
)

print(response)
```
```python
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
gen_api_key = os.getenv("DEEPSEEK_API_KEY")

client2 = OpenAI(
    api_key = gen_api_key,
    base_url = "https://api.deepseek.com"    #这里要写根URL
)

def generate_response(system_prompt, user_message):
    response = client2.chat.completions.create(
        model="deepseek-chat",
        temperature=0,
        messages=[
            {"role": "system", "content": system_prompt},    
            {"role": "user", "content": user_message}
        ]
    )
    return response

system_prompt = "你是一个攻击性很强、说话很损的助理。和你对话的是你的领导。"
user_prompt = "我今天想开摆行不行"

ai_response = generate_response(system_prompt, user_prompt)

print (ai_response.choices[0].message.content) # What returns is an object, not a dictionary.
```


An easier but less editable way.


## Completions 补全
* 对话补全（Chat completions）：就是我们一般使用的对话+回答的形式。
* FIM补全（Fill-in-the-Middle completions）：在中间补全。比如代码。

## 检查返回状态
1. **response.raise_for_status()**  
    response.status_code正常为200，反应http协议（网络/服务器）层面的问题。
2. **data['cod']==200**  
    在json文件里返回，反应API业务逻辑层面的问题。
