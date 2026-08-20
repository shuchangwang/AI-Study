from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# 初始化模型
llm = ChatOpenAI(
    model="qwen3.7-max",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    temperature=0.7
)

# Zero-shot
# 定义提示词模板
prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了{gender}，你帮我取一个名字，简单回答不要多余废话"
)

# # 调用.format方法注入信息即可
# prompt_text = prompt_template.format(lastname="张", gender="女儿")
# res = llm.invoke(input=prompt_text)
# print(res.content)


# 生成链
chain = prompt_template | llm
# 基于链，调用模型获取结果
res = chain.invoke(input={"lastname": "王", "gender": "女儿"})
print(res.content)
