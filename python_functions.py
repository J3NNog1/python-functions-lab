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

#part 3

occurrences('fleep floop', 'e')   # returns 2
occurrences('fleep floop', 'p')   # returns 2
occurrences('fleep floop', 'ee')  # returns 1
occurrences('fleep floop', 'fe')  # returns 0

def occurances(string, substr):
  # remove each occuance of substr
  stripped_string = string.replace(substr, '')
  # compute based on length of the strings
  return (len(string) - len(stripped_string)) // len(substr)
	
# Python actually has a method to solve this too!
def occurances(string, substr):
  return string.count(substr)


#part 4

product(-1, 4) # returns -4
product(2, 5, 5) # returns 50
product(4, 0.5, 5) # returns 10.0

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product``