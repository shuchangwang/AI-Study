# 方式一：ChatTongyi
# from langchain_community.chat_models.tongyi import ChatTongyi
#
# # 实例化模型
# model = ChatTongyi(model="qwen3.7-max")
#
# # 模型推理
# res = model.invoke("讲一个笑话吧")
# print(res.content)

# # 方式二:langchain_qwq包
# import os
#
# from langchain_qwq import ChatQwen
#
# api_key = os.getenv("DASHSCOPE_API_KEY")
# llm = ChatQwen(model="qwen3.7-max",
#                enable_thinking=False,
#                base_url="https://llm-lh6s7em3q8okhlai.cn-beijing.maas.aliyuncs.com/compatible-mode/v1")
# response = llm.invoke("讲一个笑话吧")
# print(response.content)

# 方式三：最佳推荐【langchain_openai】
# import os
# api_key = os.getenv("DASHSCOPE_API_KEY")
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model_name="qwen3.8-max",
    base_url="https://llm-lh6s7em3q8okhlai.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
    temperature=0
)
response = llm.invoke(input="用一句话介绍 Langchain")
print(response.content)
# # 流式数据
# for chunk in llm.stream("讲一个笑话"):
#     print(chunk.content, end="", flush=True)
