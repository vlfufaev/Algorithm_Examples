def bubble_sort(list_):
    for _ in range(len(list_)):
        for j in range(len(list_) - 1):
            if list_[j] > list_[j+1]:
                list_[j], list_[j+1] = list_[j+1], list_[j]
            print(list_)

bubble_sort([2,1,3,5,1])
