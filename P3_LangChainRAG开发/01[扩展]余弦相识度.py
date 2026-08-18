import numpy as np

"""
计算两个向量的余弦相似度（衡量方向相似性，剔除长度影响）

参数：
    vec_a (np.array): 向量A
    vec_b (np.array): 向量B
返回：
    float: 余弦相似度结果（范围[-1,1]，越接近1方向越一致）
公式：
    cos_sim = (vec_a · vec_b) / (||vec_a|| × ||vec_b||)
    拆解：
    1. 点积：vec_a · vec_b = vec_a[0]×vec_b[0] + vec_a[1]×vec_b[1] + ... + vec_a[n]×vec_b[n]
    2. 模长：||vec_a|| = √(vec_a[0]² + vec_a[1]² + ... + vec_a[n]²)
    3. 模长：||vec_b|| = √(vec_b[0]² + vec_b[1]² + ... + vec_b[n]²)

A: [0.5, 0.5]
B: [0.7, 0.7]
C: [0.7, 0.5]
D: [-0.6, -0.5]
"""


def get_dot(vector_a, vector_b):
    """计算2个向量的点积，2个向量同维度数字乘积之和"""
    if len(vector_a) != len(vector_b):
        raise ValueError("两向量的维度数量必须一致才能获取成绩之和")
    dot_sum = 0
    # zip函数的作用：zip它会将 vector_A 和 vector_B 中对应位置的元素打包成元组。对于你的例子，它内部包含的逻辑数据是 (a[0], b[0]) 和 (a[1], b[1])。
    result = zip(vector_a, vector_b)
    for a, b in result:
        dot_sum += a * b
    return dot_sum


def get_norm(vector):
    """计算单个向量的模长：对向量的每个数字求平方在求和在开根号"""
    sum_square = 0
    for val in vector:
        sum_square += val * val
    return np.sqrt(sum_square)


def cosine_similarity(vector_a, vector_b):
    """余弦相似度：2个向量的点积 除以 2个向量模长的乘积"""
    result = get_dot(vector_a, vector_b) / (get_norm(vector_a) * get_norm(vector_b))
    return result


if __name__ == '__main__':
    vector_A = [0.5, 0.5]
    vector_B = [0.7, 0.7]
    vector_C = [0.7, 0.5]
    vector_D = [-0.6, -0.5]
    AB_similarity = cosine_similarity(vector_A, vector_B)
    AC_similarity = cosine_similarity(vector_A, vector_C)
    AD_similarity = cosine_similarity(vector_A, vector_D)
    print(f"AB:{AB_similarity}")
    print(f"AC:{AC_similarity}")
    print(f"AD:{AD_similarity}")
