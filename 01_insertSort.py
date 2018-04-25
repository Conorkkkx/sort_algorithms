#_*_ coding:utf-8 _*_
#插入排序
#input_List = 尚未插入排序列表
#done_List = 完成插入排序列表

import random

def insertSort(input_List):

    for i in range(len(input_List)-1):
        x = input_List[i+1]
        j = i+1

        while j>0 and input_List[j-1] > x :
            input_List[j] = input_List[j-1]
            j -= 1
        input_List[j] = x
        print(input_List)

    return input_List


    for i in range (len(input_List)-1):
        x = input_List[i]
if __name__ == '__main__':
    n = 8
    input_List = []
    for i in range(n):
        input_List.append(random.randint(1,999))
    print('\n生成随机列表:',input_List,'\n')
    done_List = insertSort(input_List)
    print('\n插入排序后:',done_List,"\n")
