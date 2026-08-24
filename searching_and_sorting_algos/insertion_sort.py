def insertion(num_list : list[int]) -> None: # Swap bigger to right and small to left and array is sorted from left to right
    n = len(num_list)
    
    for i in range(1 , n):
        key = num_list[i]
        j = i-1
        
        while j >=0 and key < num_list[j]:
            num_list[j+1] = num_list[j]
            j -= 1
           
        num_list[j+1] = key 
    
    print(num_list)
         

num_list = [40 , 30 , 20 , 10]
insertion(num_list)
print(f"Array sorted is {num_list}")