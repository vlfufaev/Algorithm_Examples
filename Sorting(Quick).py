def partition(array, left, right):
    
    pivot = array[left] # Hyperparameter of QS is first element
    start = left + 1
    end = right

    while True:
       while start <= end and array[end] >= pivot:
            end = end - 1
       while start <= end and array[start] <= pivot:
            start = start + 1
       if start <= end:
            array[start], array[end] = array[end], array[start]
       else:
            break

    array[left], array[end] = array[end], array[left]

    return end

def quick_sort(array, left, right):
    if left >= right:
        return

    p = partition(array, left, right)
    quick_sort(array, left, p-1)
    quick_sort(array, p+1, right)

values = [8, 4, 5, 2, 1, 3]
quick_sort(values, 0, len(values) - 1)
print(values)
