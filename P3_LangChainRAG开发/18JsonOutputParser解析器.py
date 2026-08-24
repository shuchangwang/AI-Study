from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# 创建解析器
str_output_parser = StrOutputParser()
json_output_parser = JsonOutputParser()

# 创建模型
llm = ChatOpenAI(
    model="qwen3.8-max",
    base_url="https://llm-lh6s7em3q8okhlai.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)

# 创建提示词模版
first_prompt_template = PromptTemplate.from_template(
    "我的邻居姓：{lastname},生了一个：{gender},请帮我起名字，并封装为JSON格式返回给我，要求key是name,value是你起的名字，请严格遵守格式要求"
)
second_prompt_template = PromptTemplate.from_template("姓名：{name},帮我解释其含义")

# 构建chain链 AIMessage("{'name': '张悦宁'}")
# chain = first_prompt_template | llm | json_output_parser
# res = chain.invoke({"lastname": "张", "gender": "女儿"})
# print(type(res))  # <class 'dict'>
# print(res)  # {'name': '张悦宁'}

chain = first_prompt_template | llm | json_output_parser | second_prompt_template | llm | str_output_parser
# res = chain.invoke({"lastname": "张", "gender": "女儿"})
# print(type(res))  #<class 'langchain_core.messages.base.TextAccessor'>
# print(res)

# stream流式输出
for chunk in chain.stream({"lastname": "张", "gender": "女儿"}):
    print(chunk, end="", flush=True)
