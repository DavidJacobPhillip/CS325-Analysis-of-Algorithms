# ITERATION ALGORITHM

# importing file with test values
test_file = open('./test_data/num_array_10000.txt', "r")            # opens up the test-array file
values_array = test_file.read().splitlines()                        # places the test array values into an array
test_file.close()                                                           
values = values_array[0].split(' ')                                 # splits the values based on the space delimeter into the "values" array
values = [int(str) for str in values]                               # typecasting the string values into an integer

# iteration algorithm
def iteration(array):                                         
  length = len(array)
  max = -999999999

  for left in range(length):                                        # finding left endpoints      
    sum = 0
    
    for right in range(left, length):                               # finding right endpoints
      sum = sum + array[right]
      
      if sum > max:
        max = sum
  return max                                                        # returns the max value

# printing results
print("running iteration")
print(iteration(values))