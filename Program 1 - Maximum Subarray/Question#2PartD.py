# REVERSE INCURSION (KADANE) ALGORITHM

# importing file with test values
test_file = open('./test_data/num_array_10000.txt', "r")              # opens up the test-array file
values_array = test_file.read().splitlines()                        # places the test array values into an array
test_file.close()                                                           
values = values_array[0].split(' ')                                 # splits the values based on the space delimeter into the "values" array
values = [int(str) for str in values]                               # typecasting the string values into an integer

def kadane(array):
    current_max = total_max = array[0]                              # initializing both the current global maximum and the subarray maximum to the first array element

    for i in range(1, len(array) - 1):  
        current_max = current_max + array[i]                        # adding the current element being viewed to the current sub-array total
        current_max = max(current_max, array[i])                    # checking whether current element is greater than the sub-array with that element; if so current element replaces sub-array total
        total_max = max(total_max, current_max)                     # max is updated with the current total maximum
    return total_max

# printing results
print("running reverse incursion")
print(kadane(values))
