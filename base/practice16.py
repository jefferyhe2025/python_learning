import csv
import random
"""
将数据写入 CSV 文件
"""
with open('file/scores.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file,delimiter='|',quoting=csv.QUOTE_ALL) # 改变分隔符、包围方式
    writer.writerow(['姓名', '语文', '数学', '英语'])
    names = ['张三','李四','王五','赵六']
    for name in names:
        scores = [random.randrange(60,100) for _ in range(3)]
        scores.insert(0,name)
        writer.writerow(scores)

"""
读取csv文件的数据
"""
with open('file/scores.csv','r',encoding='utf-8') as file:
    reader = csv.reader(file,delimiter='|')  # 默认去除引号包围方式
    for datalist in reader:
        #打印行数
        print(reader.line_num,end='\t')
        #打印每行的元素
        for elm in datalist:
            print(elm,end='\t')
        print()
