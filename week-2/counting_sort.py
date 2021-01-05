def counting_sort(items):
    max = 0
    for i in range(len(items)):
        if items[i] > max:
            max = items[i]
    count_list = []
    for i in range(max+1):
        count_list.append(0)
    for i in range(len(items)):
        count_list[items[i]]+=1
    final_list = []
    for i in range(len(count_list)):
        for j in range(count_list[i]):
            final_list.append(i)
    print(final_list)

counting_sort([5,4,3,2,1])         
