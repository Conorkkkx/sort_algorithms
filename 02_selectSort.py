#_*_ coding:utf-8 _*_
#选择排序
#input_List = 尚未选择排序列表
#done_List = 完成选择排序列表

import random

def selectSort(input_List):
    for i in range(len(input_List)-1):
        x = i
        for j in range(i,len(input_List)):
            if input_List[j] < input_List[x]:
                x = j
        if i != x:
            input_List[i],input_List[x] = input_List[x],input_List[i]
        print('第%d次排序'%(i+1))
        print(input_List)
    return input_List
        
if __name__ == '__main__':
    
    n = random.randint(1,8)
    input_List = []

    for i in range(n):
        input_List.append(random.randint(1,999))
    print('\n生成%d位随机列表:'%n,input_List,'\n')
    done_List = selectSort(input_List)
    print('\n插入排序后:',done_List,"\n")
