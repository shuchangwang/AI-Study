from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

first_prompt_template = PromptTemplate.from_template(
    "我的邻居姓：{lastname},生了一个：{gender},请帮我起名字，仅告知我名字无需其他内容"
)
second_prompt_template = PromptTemplate.from_template("姓名：{name},帮我解释其含义")

str_output_parser = StrOutputParser()
json_output_parser = JsonOutputParser()

llm = ChatOpenAI(
    model="qwen3.8-max",
    base_url="https://llm-lh6s7em3q8okhlai.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)

# chain = first_prompt_template | llm | json_output_parser | second_prompt_template | llm | str_output_parser
# for chunk in chain.stream({"lastname": "张", "gender": "女儿"}):
#     print(chunk, end="", flush=True)


# 函数的入参：AIMessage -> dict  ({"name": "xxx"})
# my_func = RunnableLambda(lambda ai_msg: {"name": ai_msg.content})
# chain = first_prompt_template | llm | my_func | second_prompt_template | llm | str_output_parser
# for chunk in chain.stream({"lastname": "张", "gender": "女儿"}):
#     print(chunk, end="", flush=True)


chain = first_prompt_template | llm | (lambda ai_msg: {"name": ai_msg.content}) | second_prompt_template | llm | str_output_parser
for chunk in chain.stream({"lastname": "张", "gender": "女儿"}):
    print(chunk, end="", flush=True)
