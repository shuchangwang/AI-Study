from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

# 得到模型对象, qwen3.7-max就是聊天模型
llm = ChatTongyi(model="qwen3.7-max")

# 准备消息列表
messages = [
    SystemMessage(content="你是一个边塞诗人。"),
    HumanMessage(content="写一首唐诗"),
    AIMessage(content="锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦。"),
    HumanMessage(content="按照你上一个回复的格式，再写一首唐诗。")
]

# 调用stream流式执行
response = llm.stream(input=messages)

# for循环迭代打印输出，通过.content来获取到内容
for chunk in response:
    print(chunk.content, flush=True, end="")
    # 月黑雁飞高，单于夜遁逃，欲将轻骑逐，大雪满弓刀。
