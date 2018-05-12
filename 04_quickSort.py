#_*_ coding:utf-8 _*_
#快速排序
#input_List = 尚未快速排序列表
#done_List = 完成快速排序列表

import random
def quickSort(input_List,L,R):
    i = L
    j = R
    if L >= R:
        return input_List
    base = input_List[L]
    while L < R:
        while L < R and input_List[R]>= base:
            R -= 1
        input_List[L] = input_List[R]
        while L < R and input_List[L]<= base:
            L += 1
        input_List[R] = input_List[L]
    input_List[L] = base
    print(input_List)
    quickSort(input_List,i,L-1)
    quickSort(input_List,L+1,j)
    return input_List

if __name__ == '__main__':
    n = random.randint(1,8)
    input_List = []
    for i in range(n):
        input_List.append(random.randint(1,999))
    print('\n生成%d位随机列表:'%n,input_List,'\n')
    done_List = quickSort(input_List,0,len(input_List)-1)
    print('\n快速排序后:',done_List,"\n")
