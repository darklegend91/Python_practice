def bubble(num_list : list[int]) -> None :
    n = len(num_list)
    
    for i in range(n):
        swap = False
        for j in range(0 , n-i-1): # for fisrt it is 4 - 0 -1 that is until 3 so last j is at 2 as it goes to last -1 and then comparision is made
            if num_list[j] > num_list[j+1]:
                num_list[j] , num_list[j+1] = num_list[j+1] , num_list[j]
                swap = True
                
        if not swap:
            break
    
num_list = [40 , 30 , 20 , 10]
bubble(num_list)
print(f"Array sorted is {num_list}")

def bubble_sort(list_num : list[int])-> None:
    n = len(list_num)
    
    for i in range(n):
        swap = False
        for j in range(0 , n-i-1):
            if list_num[j] > list_num[j +1]:
                list_num[j] , list_num[j+1] = list_num[j+1] , list_num[j]
                swap = True
                
        if not swap:
            break