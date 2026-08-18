import json

# json对象和json数组转为json字符串
json_obj = {
    "name": "张三",
    "age": 18,
    "sex": "男"
}
# result = json.dumps(json_obj) #{"name": "\u5f20\u4e09", "age": 18, "sex": "\u7537"}
# result = json.dumps(json_obj, ensure_ascii=True)  # {"name": "\u5f20\u4e09", "age": 18, "sex": "\u7537"}
result = json.dumps(json_obj, ensure_ascii=False)  # {"name": "张三", "age": 18, "sex": "男"}
print(result)

json_arry = [
    {
        "name": "张三",
        "age": 18,
        "sex": "男"
    }, {
        "name": "李四",
        "age": 12,
        "sex": "女"
    }, {
        "name": "杨幂",
        "age": 16,
        "sex": "女"
    }
]
# [{"name": "张三", "age": 18, "sex": "男"}, {"name": "李四", "age": 12, "sex": "女"}, {"name": "杨幂", "age": 16, "sex": "女"}]
print(json.dumps(json_arry, ensure_ascii=False))

# 字符串转对象和数组
json_obj_str = '{"name": "张三", "age": 18, "sex": "男"}'
json_arry_str = '[{"name": "张三", "age": 18, "sex": "男"}, {"name": "李四", "age": 12, "sex": "女"}, {"name": "杨幂", "age": 16, "sex": "女"}]'
result_json_obj = json.loads(json_obj_str)
result_json_array = json.loads(json_arry_str)
print(result_json_obj)
print(result_json_array)
