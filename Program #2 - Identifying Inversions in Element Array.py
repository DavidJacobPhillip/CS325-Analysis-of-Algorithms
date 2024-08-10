array = [1, 0, -1, 0]
inversions = 0
def merge_sort(array):
    if len(array) > 1:
        midpoint = len(array) // 2
        left_array = array[:midpoint]
        right_array = array[midpoint:]

        merge_sort(left_array)
        merge_sort(right_array)
        
        i = 0
        k = 0
        j = 0

        # selecting the greater value to put into the merge between the
        # two array values that are being compared
        while len(left_array) > i and len(right_array) > j:
            global inversions
            if left_array[i] > right_array[j]:
                array[k] = right_array[j]
                j = j + 1
                k = k + 1

                inversions = inversions + len(left_array);   
            else:
                array[k] = left_array[i]
                i = i + 1
                k = k + 1

        # copying remaining elements
        while len(left_array) > i:          
            array[k] = left_array[i]
            i = i + 1
            k = k + 1

        while len(right_array) > j:          
            array[k] = right_array[j]
            j = j + 1
            k = k + 1
            # inversions = inversions + 1  
            
merge_sort(array)

print(array)
print("inversions: ", inversions)