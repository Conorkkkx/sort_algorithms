#_*_ coding:utf-8 _*_

#冒泡排序(升序)
#input_List = 尚未冒泡排序列表
#done_List = 完成冒泡排序列表

import random

def bubbleSort(input_List):
    for i in range(len(input_List)-1):
        changed = False
        print("***开始第%d次排序***"%(i+1))
        for j in range(len(input_List)-1):
            if input_List[j+1]<input_List[j]:
                input_List[j],input_List[j+1] = input_List[j+1],input_List[j]
                changed = True
            print(input_List)
        print("***第%d次排序结束***\n"%(i+1))
        if not changed :
            break
    return input_List

if __name__ == '__main__':
    n = 8
    input_List = []
    for i in range(n):
        input_List.append(random.randint(1,999))
    print('\n生成随机列表:',input_List,'\n')
    done_List = bubbleSort(input_List)
    print('\n冒泡算法(升序)排序后:',done_List,"\n")
