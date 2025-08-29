def bubble_sort(list1):
    list0=list(list1)  
    for i in range(0,len(list0)-1):  
        for j in range(len(list0)-1):  
            if(list0[j]>list0[j+1]):  
                temp = list0[j]  
                list0[j] = list0[j+1]  
                list0[j+1] = temp  
    return list0
tp1=eval(input("Enter a tuple of 10 different numbers : "))
print("Before Sorting : ",tp1)
print("After  Sorting : ",tuple(bubble_sort(tp1)))