#code to implement quadratic time complexity
def all_pairs(arr):
    # Loop through each element in the list
    for i in range(len(arr)):
        # Loop through the elements that come after index i
        for j in range(i+1,len(arr)):
            # Print the pair of elements
            print(arr[i],arr[j])

all_pairs([1,2,3,4])
