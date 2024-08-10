# written by Santosh Ramesh
# last modified October 7th, 2021

import sys
import time

# Usage when run from the command line: python max_subarray_algs.py <filename>.
# Example usage:                        python max_subarray_algs.py num_array_500.txt

file_name = sys.argv[1]

f = open(file_name, "r")
A = [int(num) for num in f.readline().strip().split(" ")]
f.close()

# -------------------------------------  
# ENUMERATION ALGORITHM
# -------------------------------------  
def max_subarray_enumeration(A):
  length = len(A)
  maximum = -999999999

  for left in range(length):                                                      
    for right in range(left, length):                    
      sum = 0

      for number in range(left, right + 1):              
        sum += A[number]

      if sum > maximum:
        maximum = sum

  return maximum   

# -------------------------------------  
# ITERATION ALGORITHM
# -------------------------------------  
def max_subarray_iteration(A):
  length = len(A)
  max = -999999999

  for left in range(length):             
    sum = 0
    
    for right in range(left, length):     
      sum = sum + A[right]
      
      if sum > max:
        max = sum
  return max    

# -------------------------------------  
# SIMPLIFICATION & DELEGATION ALGORITHM
# -------------------------------------  
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

def simplification(array, left, right):
  if (left != right):
      mid = (left + right) // 2

      left_sum = simplification(array, left, mid)
      right_sum = simplification(array, mid + 1, right)
      combined_sum = combiner(array, left, mid, right)
      return max(left_sum, right_sum, combined_sum)
  return array[left]

def max_subarray_simplification_delegation(A):
    maximum = simplification(A, 0, len(A) - 1)

    return maximum
    
# -------------------------------------  
# REVERSE INCURSION ALGORITHM
# -------------------------------------  
def max_subarray_recursion_inversion(A):
    current_max = total_max = A[0]                                 

    for i in range(1, len(A) - 1):  
        current_max = current_max + A[i]  
        current_max = max(current_max, A[i])        
        total_max = max(total_max, current_max)    
    return total_max
  
# -------------------------------------  
# TIME ANALYSIS OF ALGORITHMS
# -------------------------------------  
def time_alg(alg, A):
  start_time = time.monotonic_ns() // (10 ** 6)
  max_subarray_val = alg(A)
  end_time   = time.monotonic_ns() // (10 ** 6)
  return max_subarray_val, end_time - start_time

for alg in [max_subarray_enumeration,
  max_subarray_iteration,
  max_subarray_simplification_delegation,
  max_subarray_recursion_inversion]:
  print(file_name, time_alg(alg, A))

print(max_subarray_enumeration(A), max_subarray_iteration(A), max_subarray_simplification_delegation(A), max_subarray_recursion_inversion(A))