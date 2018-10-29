## 1. What is the best case for find_element_in_list when the data_list is [0, 1, ..., 9999]?

# The best case is when we are looking for 0. 
# So if we call 
# > find_element_in_list(data_list, 0)
# then it will exit after one repetition of the loop. 

## 2. What is the worst case for find_element_in_list when the data_list is [0, 1, ..., 9999]?

# The worst case is when we are looking for 9999 or something not in the data_list. 
# So if we call 
# > find_element_in_list(data_list, 9999)
# then it will exit after as many repetitions of the loop as there are elements in the list. 

## 3. Let's say find_element_in_list is run with a list of size n. The worst-case runtime 
## O(n) is one of the following choices a-d, write down which one:
#     b. linear
    
# Because the loop repeats as many times as there are elements in the list (in the worst case). 