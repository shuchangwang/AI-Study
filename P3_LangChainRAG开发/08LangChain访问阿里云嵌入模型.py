from langchain_community.embeddings import DashScopeEmbeddings

# 创建模型对象 不传model默认用的是 text-embeddings-v1
llm_embeddings = DashScopeEmbeddings()

# 不用invoke stream
# embed_query：单个转换、embed_documents：批量转换
embedding_str1 = llm_embeddings.embed_query("我喜欢你")
embedding_str2 = llm_embeddings.embed_documents(
    ["曾经有一份真挚的爱情摆在我面前，我没有珍惜，等我失去的时候我才后悔莫及，人世间最痛苦的事莫过于此。",
     "你的剑在我的咽喉上割下去吧！不用再犹豫了！",
     "如果上天能够给我一个再来一次的机会，我会对那个女孩子说三个字：我爱你。",
     "如果非要在这份爱上加上一个期限，我希望是一万年！"])

# 向量维度：1536
print(f"向量维度：{len(embedding_str1)}")
print(f"向量值{embedding_str1}")
print()
print(f"向量值{embedding_str2}")
