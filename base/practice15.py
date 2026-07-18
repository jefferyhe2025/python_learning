import json,requests
"""
将字典处理成json格式
"""
my_dict = {
    'name': '狄仁杰',
    'age': 42,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
print(json.dumps(my_dict))
#将字典处理成json格式并保存在文件中(序列化)
with open('data.json','w') as file: #先创建json文件，再存储内容
    json.dump(my_dict,file)
# #反序列化
with open('data.json','r') as file:
    my_dict = json.load(file)
    print(type(my_dict))
    print(my_dict)
#用conda安装ujson第三方库：conda install ujson

"""
申请网络接口:朋友圈文案
"""
from local_config import API_KEY
# 🚀发送请求
resp1 = requests.get(
    'https://apis.tianapi.com/pyqwenan/index',
    params={'key': API_KEY} #传入API参数信息
)
data = resp1.json() #将请求发来的信息处理成字典格式

if data.get('code') == 200:
    # 打印消息
    result = data['result']
    print(result['content'])
    print(result.get('source', ''))
else:
    # 返回调用失败的信息
    print('调用失败:', data.get('code'), data.get('msg'))

"""
申请网络接口:AI新闻
"""
resp2 = requests.get(
    'https://apis.tianapi.com/ai/index',
    params={'key':API_KEY}
)
data_model = resp2.json()

if data_model.get('code') == 200:
    result = data_model['result']
    # 逐条打印获取到的新闻
    for news in result['newslist']:
        print(news['ctime']) # 打印时间
        print(news['title']) # 打印标题
        print(news['description']) # 打印详情
        print('-' * 60)
else:
    #返回调用失败的信息
    print('调用失败：',data_model.get('code'),data_model.get('msg'))


