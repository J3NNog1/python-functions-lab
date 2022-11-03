#part 1

sum_to(6)  # returns 21
sum_to(10) # returns 55

def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum