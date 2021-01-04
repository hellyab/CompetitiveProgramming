def selection_sort(items):
    for i in range(len(items)):
        for j in range (len(items)-i):
            smallest_item_index = i
            if items[smallest_item_index]<items[j]:
                smallest_item_index = j
        items[smallest_item_index], items[i] = items[i], items[smallest_item_index]
    print(items)

selection_sort([5,4,3,2,1])