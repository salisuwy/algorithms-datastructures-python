def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(f"Bubble Sort: {arr}")


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    print(f"Selection Sort: {arr}")


def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp

    print(f"Insertion Sort: {arr}")


def merge_sort(arr):
    def sort(arr):
        if len(arr) > 1:
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            sort(left)
            sort(right)

            i, j, k = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
    sort(arr)
    print(f"Merge Sort: {arr}")


def quick_sort(arr):
    def sort(arr, start, end):
        if start < end:
            p = partition(arr, start, end)
            sort(arr, start, p-1)
            sort(arr, p+1, end)
    
    def partition(arr, start, end):
        pivot = end
        left = start
        right = end-1
        while left < right:
            while arr[left] < arr[pivot] and left < end:
                left += 1
            while arr[right] > arr[pivot] and right > start:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
        
        arr[left], arr[pivot] = arr[pivot], arr[left]
        return left
  
    sort(arr, 0, len(arr)-1)
    print(f"Quick Sort: {arr}")


if __name__ == "__main__":
    import random

    unsorted = []
    i = 0
    while i < 20:
        num = random.randint(-10, 40)
        if num not in unsorted:
            unsorted.append(num)
            i += 1

    print("Unsorted: ", unsorted)
    bubble_sort(unsorted[:])
    selection_sort(unsorted[:])
    insertion_sort(unsorted[:])
    merge_sort(unsorted[:])
    quick_sort(unsorted[:])