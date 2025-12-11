

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

my_list = [60,30,1,2,22,12,11,90]

bubble_sort(my_list)
print("Sorted array is: ", my_list)