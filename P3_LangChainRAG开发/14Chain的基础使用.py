from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个边塞诗人，可以作诗。"),
        MessagesPlaceholder("history"),
        ("human", "请再来一首唐诗")
    ]
)

history_data = [
    ("human", "你来写一个唐诗"),
    ("ai", "床前明月光，疑是地上霜，举头望明月，低头思故乡"),
    ("human", "好诗再来一个"),
    ("ai", "锄禾日当午，汗滴禾下锄，谁知盘中餐，粒粒皆辛苦"),
]

llm = ChatOpenAI(
    model_name="qwen3.8-max",
    base_url="https://llm-lh6s7em3q8okhlai.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
    temperature=0
)

# 组成链，要求每一个组件都是Runnable接口的子类
chain = chat_prompt_template | llm
print(type(chain))  # <class 'langchain_core.runnables.base.RunnableSequence'>
print(chain)

# 通过链去调用invoke或stream
# result = chain.invoke(input={"history": history_data})
# print(type(result))  # <class 'langchain_core.messages.ai.AIMessage'>
# print(result)
# print(result.content)

# # 通过stream流式输出
# for chunk in chain.stream({"history": history_data}):
#     print(chunk.content, end="", flush=True)
