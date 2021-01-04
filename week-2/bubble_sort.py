def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items)):
            current_index = i
            if items[current_index] < items[j]:
                items[current_index], items[j] = items[j], items[current_index]
                current_index = j
    print(items)    

bubble_sort([5,4,3,2,1])