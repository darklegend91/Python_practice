def quick_sort(num_list: list[int], low: int, high: int):
    if low < high:
        pivot = partition(num_list, low, high)
        quick_sort(num_list, low, pivot - 1)
        quick_sort(num_list, pivot + 1, high)

def partition(num_list: list[int], low: int, high: int):
    p = num_list[low]     # Pivot is the first element
    i = low + 1
    j = high

    while True:
        # Move i right while values are <= pivot
        while i <= j and num_list[i] <= p:
            i += 1
        
        # Move j left while values are >= pivot
        while i <= j and num_list[j] >= p:
            j -= 1
        
        if i <= j:
            num_list[i], num_list[j] = num_list[j], num_list[i]
        else:
            break

    # Place pivot in its correct position
    num_list[low], num_list[j] = num_list[j], num_list[low]
    return j

num_list = [40, 30, 20, 10]
quick_sort(num_list, 0, len(num_list) - 1)
print(f"Array sorted is {num_list}")