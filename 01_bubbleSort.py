#_*_ coding:utf-8 _*_

#冒泡排序(升序)

#input_List = 尚未冒泡排序列表
#done_List = 完成冒泡排序列表

def bubbleSort(input_List):
    if len(input_List)== 0:
        return []
    else:
        pass

    for i in range(len(input_List)-1):
        print("***第%d次排序***"%(i+1))
        for j in range(len(input_List)-1):
            if input_List[j+1]<input_List[j]:
                input_List[j],input_List[j+1] = input_List[j+1],input_List[j]
            print(input_List)
    return input_List
if __name__ == '__main__':
    input_List = [213,123,45,6,1234,534,324]
    print('输入的列表:',input_List)
    done_List = bubbleSort(input_List)
    print('冒泡算法(升序)排序后:',done_List)
