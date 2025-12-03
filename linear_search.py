def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1

my_list = [22,6,4,3,8]
search_target = 3
result_index = linear_search(my_list, search_target)

if result_index!= 1:
    print(f"The index value of {search_target} is {result_index}")
else: 
    print(f"The target {search_target} is not found in the list")


  