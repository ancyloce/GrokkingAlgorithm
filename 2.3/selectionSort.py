def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if(arr[i]) < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
        # TODO: write code...

def selectionSort(arr):
    newArr= []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr
        # TODO: write code...

print(selectionSort([7,1,6,5,9,3,5,2,0]))
