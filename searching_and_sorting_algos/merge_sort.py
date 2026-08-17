def merge_sort(num_list : list[int]) -> list[int]:
    if len(num_list) <=1:
        return num_list

    mid = len(num_list) //2
    
    l_half = num_list[:mid]
    r_half = num_list[mid:]
    l_half = merge_sort(l_half)
    r_half = merge_sort(r_half)
    
    return merge(l_half , r_half)

def merge(left , right) -> list[int]:
    
    new = []
    i , j = 0 , 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j +=1
    
    new.extend(left[i:])
    new.extend(right[j:])
    
    return new
    
num_list = [40 , 30 , 20 , 10]
sorted = merge_sort(num_list)
print(f"Array sorted is {sorted}") 