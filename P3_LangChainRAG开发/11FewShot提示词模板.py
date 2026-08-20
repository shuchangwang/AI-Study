from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_openai import ChatOpenAI

# 示例模板
example_template = PromptTemplate.from_template("单词：{word}，反义词：{antonym}")

# 示例数据，示例的动态数据注入 要求是list内部套字典
example_datas = [
    {"word": "大", "antonym": "小"},
    {"word": "上", "antonym": "下"}
]
few_shot_template = FewShotPromptTemplate(
    example_prompt=example_template,  # 示例数据的模板
    examples=example_datas,  # 示例的数据（用来注入动态数据的），list内套字典
    prefix="告知我单词的反义词，我提供如下的示例：",  # 示例之前的提示词
    suffix="基于前面的示例告知我，{input_word}的反义词是？",  # 示例之后的提示词
    input_variables=['input_word']  # 声明在前缀或后缀中所需要注入的变量名
)
prompt_text = few_shot_template.invoke(input={"input_word": "左"})
print(prompt_text)
print(prompt_text.to_string())
'''
告知我单词的反义词，我提供如下的示例：

单词：大，反义词：小

单词：上，反义词：下

基于前面的示例告知我，左的反义词是？
'''

# 初始化模型
# 得到模型对象
llm = ChatOpenAI(
    model_name="qwen3.8-max",
    base_url="https://llm-lh6s7em3q8okhlai.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
    temperature=0
)
print(llm.invoke(input=prompt_text).content)  # 左的反义词是：右
