def isSorted(lst):
    """Returns True if the list is sorted in ascending order, otherwise False"""
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

if __name__ == "__main__":
    test_lists = [
        [],                      
        [1],                     
        [1, 2, 3, 4, 5],        
        [5, 4, 3, 2, 1],         
        [1, 2, 2, 3, 4],         
        [3, 3, 2],               
        [10, 20, 30, 25, 40],    
        ]


    for lst in test_lists:
        print(f"List: {lst} --> Sorted? {isSorted(lst)}")
