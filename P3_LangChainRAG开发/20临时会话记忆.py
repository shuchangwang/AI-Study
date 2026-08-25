from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="qwen3.8-max",
    base_url="https://llm-lh6s7em3q8okhlai.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)
# prompt_template = PromptTemplate.from_template(
#     "你需要根据对话历史回应用户问题。对话历史：{chat_history}。用户当前输入：{input}， 请给出回应"
# )
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你需要根据对话历史回应用户问题。对话历史："),
        MessagesPlaceholder("chat_history"),
        ("human", "请给出回应:{input}")
    ]
)


def print_prompt(full_prompt):
    print("=" * 20, full_prompt.to_string(), "=" * 20)
    return full_prompt


base_chain = prompt_template | print_prompt | llm | StrOutputParser()

session_id_datas = {}  # key就是session，value就是InMemoryChatMessageHistory类对象


# 实现通过会话id获取InMemoryChatMessageHistory类对象
def get_history(session_id):
    if session_id not in session_id_datas:
        session_id_datas[session_id] = InMemoryChatMessageHistory()
    return session_id_datas[session_id]


# 创建一个新的链，对原有链增强功能：自动附加历史消息
conversion_chain = RunnableWithMessageHistory(
    base_chain,  # 被增强的原有chain
    get_history,  # 通过会话id获取InMemoryChatMessageHistory类对象
    input_messages_key="input",  # 表示用户输入在模板中的占位符
    history_messages_key="chat_history"  # 表示用户输入在模板中的占位符
)

if __name__ == "__main__":
    # 固定格式，添加LangChain的配置，为当前程序配置所属的session_id
    session_config = {"configurable": {"session_id": "user_001"}}
    print(conversion_chain.invoke({"input": "小明有一只猫"}, session_config))
    print(conversion_chain.invoke({"input": "小刚有两只狗"}, session_config))
    print(conversion_chain.invoke({"input": "共有几只宠物？"}, session_config))
