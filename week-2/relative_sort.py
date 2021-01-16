def relativeSortArray(arr1, arr2):

    #TODO: fix sorting issue with the remaining values
    occurrence_dict = {}
    maxNumber = 0
    print(type(occurrence_dict))
    for i in range(len(arr1)):
        if (arr1[i]) in occurrence_dict:
            occurrence_dict[(arr1[i])] += 1
        else:
            occurrence_dict[(arr1[i])] = 1
    final_array = []
    for number in arr2:
        for i in range(occurrence_dict[number]):
            final_array.append(number)
        occurrence_dict[number] = None

    for occurrence in occurrence_dict:
        if occurrence_dict[occurrence] != None:
            for i in range(occurrence_dict[occurrence]):
                final_array.append(occurrence)
        occurrence_dict[occurrence] = None

    print(final_array)


relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6])
