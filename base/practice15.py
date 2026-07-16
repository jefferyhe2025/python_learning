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
with open('data.json','w') as file:
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

resp = requests.get(
    'https://apis.tianapi.com/pyqwenan/index',
    params={'key': API_KEY}
)
data = resp.json()

if data.get('code') == 200:
    result = data['result']
    print(result['content'])
    print(result.get('source', ''))
else:
    print('调用失败:', data.get('code'), data.get('msg'))

