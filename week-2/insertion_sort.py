def insertion_sort(items):
    for i in range(len(items)):
        current_item = items[i]
        for j in range(i, -1, -1):
            if current_item < items[j]:
                items[j+1] = items[j]
                items[j] = current_item   
    print(items)

insertion_sort([5,4,3,2,1])
