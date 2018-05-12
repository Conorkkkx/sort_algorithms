#_*_ coding:utf-8 _*_
#xx排序
#input_List = 尚未xx排序列表
#done_List = 完成xx排序列表

import random

def ssSort(input_List):
        
if __name__ == '__main__':
    n = random.randint(1,8)
    input_List = []
    for i in range(n):
        input_List.append(random.randint(1,999))
    print('\n生成%d位随机列表:'%n,input_List,'\n')
    done_List = selectSort(input_List)
    print('\nss排序后:',done_List,"\n")
