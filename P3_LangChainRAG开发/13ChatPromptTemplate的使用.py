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
prompt_text = chat_prompt_template.invoke({"history": history_data}).to_string()
"""
System: 你是一个边塞诗人，可以作诗。
Human: 你来写一个唐诗
AI: 床前明月光，疑是地上霜，举头望明月，低头思故乡
Human: 好诗再来一个
AI: 锄禾日当午，汗滴禾下锄，谁知盘中餐，粒粒皆辛苦
Human: 请再来一首唐诗
"""

llm = ChatOpenAI(
    model_name="qwen3.8-max",
    base_url="https://llm-lh6s7em3q8okhlai.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
    temperature=0
)
result = llm.invoke(input=prompt_text)
print(result.content)
