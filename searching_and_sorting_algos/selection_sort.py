def selection(num_list) -> None: 
    
    n = len(num_list)
    
    for i in range(n-1):
        mini = i
        
        for j in range (i+1 , n):
            if num_list[j] < num_list[mini]:
                mini = j
                num_list[i] , num_list[mini] = num_list[mini] , num_list[j]

num_list = [40 , 30 , 20 , 10]
selection(num_list)
print(f"Array sorted is {num_list}")