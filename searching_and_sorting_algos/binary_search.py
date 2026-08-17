def binary_search_iterative( num_list :list[int] , target : int) -> int:
    left = 0
    right = len(num_list) -1
    
    while left <=right :
        mid = left + (right - left) // 2
        if num_list[mid] == target:
            return mid
        
        elif num_list[mid] > target :
            # target is small move the window to left
            right = mid  - 1
        
        else:
            # target is bigger move the window to right
            left = mid + 1
    
    return -1

def binary_search_reccursive( num_list :list[int] , target : int , left: int , right :  int) -> int:
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if num_list[mid] == target:
        return mid
            
    elif num_list[mid] > target :
        # target is small move the window to left
        return binary_search_reccursive(num_list , target , left , mid-1)
            
    else:
        # target is bigger move the window to right
        return binary_search_reccursive(num_list , target , mid+1 , right)
    
    return -1
    
    
def main() -> None:
    
    num_list = [10,  20, 35 , 46 , 78, 121]
    target = 46
    target1 = 10
    print(f"The element { target } is found at index (Starting from 0) {binary_search_iterative(num_list , target)}")
    print(f"The element { target } is found at index (Starting from 0) {binary_search_reccursive(num_list , target1 , 0 , len(num_list) -1)}")
    
if __name__ == "__main__" :
    main()