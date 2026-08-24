from langchain_core.messages import AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

prompte_template = PromptTemplate.from_template("我的邻居姓：{lastname},生了一个：{gender},请起名，仅告知我名字无需其他内容")
str_output_parser = StrOutputParser()
llm = ChatOpenAI(
    model_name="qwen3.8-max",
    base_url="https://llm-lh6s7em3q8okhlai.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)
# chain = prompte_template | llm | str_output_parser | llm
# res: AIMessage = chain.invoke({"lastname": "王", "gender": "儿子"})
# print(res.content) # AIMessage
chain = prompte_template | llm | str_output_parser | llm | str_output_parser
res: str = chain.invoke({"lastname": "王", "gender": "女儿"})
print(res)
print(type(res))# <class 'langchain_core.messages.base.TextAccessor'>
