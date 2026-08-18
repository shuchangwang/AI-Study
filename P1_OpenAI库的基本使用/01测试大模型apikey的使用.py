# 通过当前目录加载.env配置文件方式加载API KEY
# from dotenv import load_dotenv
# 在创建客户端前先加载环境变量
# load_dotenv()

from openai import OpenAI

client = OpenAI(
    # 通过配置高级系统配置，添加环境变量后重启后无需重写api_key相关变量，将自行加载
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    # api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://llm-lh6s7em3q8okhlai.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)

messages = [
    {
        "role": "user",
        "content": "你是谁？你能做什么？"
    }
]
completion = client.chat.completions.create(
    # model="qwen3.7-plus",  # 您可以按需更换为其它深度思考模型
    # model="qwen3.7-max",  # 您可以按需更换为其它深度思考模型
    model="deepseek-v4-flash-0731",  # 您可以按需更换为其它深度思考模型
    messages=messages,
    stream=True
)
for chunk in completion:
    if not chunk.choices:
        continue
    print(chunk.choices[0].delta.content, end="", flush=True)

# is_answering = False  # 是否进入回复阶段
# print("\n" + "=" * 20 + "思考过程" + "=" * 20)
# for chunk in completion:
#     if not chunk.choices:
#         continue
#     delta = chunk.choices[0].delta
#     if hasattr(delta, "reasoning_content") and delta.reasoning_content is not None:
#         if not is_answering:
#             print(delta.reasoning_content, end="", flush=True)
#     if hasattr(delta, "content") and delta.content:
#         if not is_answering:
#             print("\n" + "=" * 20 + "完整回复" + "=" * 20)
#             is_answering = True
#         print(delta.content, end="", flush=True)
