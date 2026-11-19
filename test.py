from openai import OpenAI

client = OpenAI(
    api_key="sk-8840f05194a74aa98390d9c0523bbc38", 
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个资深的电商客服。"},
        {"role": "user", "content": "我买的手机屏幕碎了，能退换吗？"}
    ]
)
print(response.choices[0].message.content)
