from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage

llm = ChatTongyi(model="qwen3.7-max")

messages = [
    HumanMessage(content="讲个笑话吧？")
]
response = llm.stream(input=messages)
for chunk in response:
    # print(chunk.content)
    print(chunk.content, end="", flush=True)
