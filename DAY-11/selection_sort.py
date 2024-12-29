arr = [5,3,2,4,1]

def selectionSort(arr):
    for i in range(len(arr)):
        min_val = i
        for i in range(i+1,len(arr)):
            if arr[j]<arr[min_val]:
                min_val = j
        arr[i] , arr[min_val] = arr [min_val],arr[i]
    print(arr)
selectionSort(arr)