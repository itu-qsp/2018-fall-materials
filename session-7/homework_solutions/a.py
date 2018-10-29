# In this part of the assignment, you should write a function where_is that finds
# an element in a list. More precisely:

# Input: A list l and an element x to search for.

# Output: An index idx such that l[idx] == x, or None if x is not present in l. If
# x occurs more than once, the first occurrence is reported.

# The following has to work:

# > where_is([1, 3, 5], 3)
# 1
# > where_is([1, 2, 4, 5, 4], 4)
# 2
# > where_is([1, 2, 3], 0)
# None

def where_is(l, x):
    """Finds the first occurence of the element x in the list l.
    l: list 
    x: any type
    Prints the index of x in the list l
    Returns an integer which is the index of x in the list l
    Both prints and returns None if x not found
    """
    for idx in range(len(l)):
        if l[idx] == x:
            print(idx)
            return idx
    print(None)
    return None 
    
where_is([1, 3, 5], 3)
where_is([1, 2, 4, 5, 4], 4)
where_is([1, 2, 3], 0)
print()

# Alternatively we could save all the idx values where l[idx] == x is True

def where_is(l, x):
    found_index = []
    for idx in range(len(l)):
        if l[idx] == x:
            found_index.append(idx)
    if len(found_index) == 0:
        print(None)
        return None
    else:
        print(found_index[0])
        return found_index[0]
    
where_is([1, 3, 5], 3)
where_is([1, 2, 4, 5, 4], 4)
where_is([1, 2, 3], 0)

