# langchain_ollama
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen:4b")
response = llm.invoke(input="你是谁？你能帮我做什么？")
print(response)
