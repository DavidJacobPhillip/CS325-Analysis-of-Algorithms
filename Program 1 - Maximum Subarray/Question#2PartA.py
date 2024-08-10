# ENUMERATION ALGORITHM

# importing file with test values
test_file = open('./test_data/num_array_500.txt', "r")              # opens up the test-array file
values_array = test_file.read().splitlines()                        # places the test array values into an array
test_file.close()                                                           
values = values_array[0].split(' ')                                 # splits the values based on the space delimeter into the "values" array
values = [int(str) for str in values]                               # typecasting the string values into an integer

# enumeration algorithm
def enumeration(array):                                         
  length = len(array)
  maximum = -999999999

  for left in range(length):                                        # finding left endpoints                               
    for right in range(left, length):                               # finding right endpoints
      sum = 0

      for number in range(left, right + 1):                         # sum over elements in subarray between i & j, inclusive
        sum += array[number]

      if sum > maximum:
        maximum = sum
  return maximum                                                    # returns the max value

# printing results
print("running enumeration")
print(enumeration(values))