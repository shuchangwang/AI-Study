# 0.导入相关库
from openai import OpenAI

# 1，获取client对象
client = OpenAI(
    # api_key="xxxxxxxxxxxxx",
    base_url="https://llm-lh6s7em3q8okhlai.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)

# 2.调用模型
response = client.chat.completions.create(
    model="qwen3.7-max",
    messages=[
        {"role": "system", "content": "你是一个Python编程专家，并且话非常多"},
        {"role": "assistant", "content": "好的，我是编程专家，并且话非常多，你要问什么？"},
        {"role": "user", "content": "输出1-10的数字，使用Python代码"}
    ],
    stream=True  # 是否开启流式输出
)

# 3.处理结果
for chunk in response:
    if not chunk.choices:
        continue
    print(chunk.choices[0].delta.content,
          end=" ",  # 每一段之间用空格分隔
          flush=True  # 立刻刷新缓冲区
          )
