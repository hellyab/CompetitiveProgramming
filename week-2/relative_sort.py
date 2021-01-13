def relativeSortArray(arr1, arr2):
        occurenceDict = {}
        maxNumber = 0
        print(type(occurenceDict))
        for i in range(len(arr1)):
            if (arr1[i]) in occurenceDict:
                occurenceDict[(arr1[i])] += 1
            else:
                occurenceDict[(arr1[i])] = 1
            
        print(occurenceDict)
relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6])