# import os
# api_key = os.getenv("DASHSCOPE_API_KEY")
# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(
#     model_name="qwen3.7-max",
#     base_url="https://llm-lh6s7em3q8okhlai.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
#     temperature=0
# )
# response = llm.stream(input="你是谁呀能做什么？")
# # 流式数据
# for chunk in response:
#     print(chunk.content, end="", flush=True)

from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen3:4b")

res = llm.stream(input="你是谁呀能做什么？")

for chunk in res:
    print(chunk, end="", flush=True)
