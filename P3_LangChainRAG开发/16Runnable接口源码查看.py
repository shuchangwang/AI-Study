from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

prompt_template = PromptTemplate.from_template("你是一个AI助手")
llm = ChatOpenAI(
    model_name="qwen3.8-max",
    base_url="https://llm-lh6s7em3q8okhlai.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
    temperature=0
)

chain = prompt_template | llm
print(type(chain))  # <class 'langchain_core.runnables.base.RunnableSequence'>
chain2 = prompt_template | llm | prompt_template | llm
print(type(chain2))  # <class 'langchain_core.runnables.base.RunnableSequence'>
