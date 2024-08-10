# SIMPLIFICATION & DELEGATION ALGORITHM

# importing file with test values
test_file = open('./test_data/num_array_10000.txt', "r")              # opens up the test-array file
values_array = test_file.read().splitlines()                        # places the test array values into an array
test_file.close()                                                           
values = values_array[0].split(' ')                                 # splits the values based on the space delimeter into the "values" array
values = [int(str) for str in values]                               # typecasting the string values into an integer


def combiner(array, left, mid, right):
    left_max = right_max = -999999999
    current_sum = 0

    
    for i in range(mid, left - 1, -1):
        current_sum = current_sum + array[i]
        left_max = max(current_sum, left_max)
    #print(current_sum)
    
    current_sum = 0
    for i in range(mid + 1, right + 1):
        current_sum = current_sum + array[i]
        right_max = max(current_sum, right_max)

    combined_max = left_max + right_max

    return max(left_max, right_max, combined_max)

# REVERSE INCURSION (KADANE) ALGORITHM
def simp(array, left, right):
    if (left != right):
        mid = (left + right) // 2

        left_sum = simp(array, left, mid)
        right_sum = simp(array, mid + 1, right)
        combined_sum = combiner(array, left, mid, right)
        return max(left_sum, right_sum, combined_sum)
    return array[left]

print("running simplification & delegation")
print(simp(values, 0, len(values) - 1))
