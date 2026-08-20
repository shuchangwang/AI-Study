from langchain_core.prompts import PromptTemplate

"""
继承关系以及接口实现
PromptTemplate——》StringPromptTemplate——》BasePromptTemplate——》RunnableSerializable——》Runnable
FewShotPromptTemplate——》StringPromptTemplate——》BasePromptTemplate——》RunnableSerializable——》Runnable
ChatPromptTemplate——》BaseChatPromptTemplate——》BasePromptTemplate——》RunnableSerializable——》Runnable
"""

# PromptTemplate
template = PromptTemplate.from_template("我的邻居是：{lastname}，最喜欢：{hobby}")

# PromptTemplate 的format方法
result = template.format(lastname="张三", hobby="钓鱼")
print(type(result), result)
# <class 'str'> 我的邻居是：张三，最喜欢：钓鱼

# PromptTemplate 的invoke方法
result2 = template.invoke({"lastname": "孙燕姿", "hobby": "购物"})
print(type(result2), result2)
# <class 'langchain_core.prompt_values.StringPromptValue'> text='我的邻居是：张三，最喜欢：钓鱼'
