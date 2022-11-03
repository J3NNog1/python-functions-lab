#part 1

sum_to(6)  # returns 21
sum_to(10) # returns 55

def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum

#part 2

largest([1, 2, 3, 4, 0])  # returns 4
largest([10, 4, 2, 231, 91, 54])  # returns 231

def largest(nums):
  largest = 0
  for num in nums:
    if num > largest:
      largest = num
  return largest
  
# Sort the list approach
def largest(nums):
  nums.sort()
  return nums[-1]