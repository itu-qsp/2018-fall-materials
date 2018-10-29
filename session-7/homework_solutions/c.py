def find_element_in_list2(data_list, element):
    for idx, el in enumerate(data_list):
        if el == element:
            first_result_idx = idx
            break
    for idx, el in enumerate(data_list):
        if el == element and idx == first_result_idx:
            return idx, el
            
## Let's say find_element_in_list2 is run with a list of size n.
## The worst-case runtime O(n) is one of the following choices a.-d. But which one?

# If len(data_list) == n and the element searched for is the first element
# then the loops will run twice in total. 
# If the element searched for is the last element (or not there) 
# then the loops will run 2 * n times in total. 

# Even though 2n is the worst-case runtime, it is still linear in big O notation. O(n).

# So the answer is b. linear