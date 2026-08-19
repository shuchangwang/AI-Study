from langchain_community.chat_models.tongyi import ChatTongyi

# 得到模型对象, qwen3.7-max就是聊天模型
llm = ChatTongyi(model="qwen3.7-max")

# 准备消息列表
messages = [
    # (角色，内容)  角色：system/human/ai
    ("system", "你是一个边塞诗人。"),
    ("human", "写一首唐诗"),
    ("ai", "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦。"),
    ("human", "按照你上一个回复的格式，再写一首唐诗。")
]

# 调用stream流式执行
response = llm.stream(input=messages)

# for循环迭代打印输出，通过.content来获取到内容
for chunk in response:
    print(chunk.content, flush=True, end="")
    # 大漠风尘暗，孤城落日残，夜半胡笳咽，铁甲透霜寒。
