from random import randint
from shutil import copy

from Collatz import cycle_length, collatz_eval

EID = 'cat3263'
input_file = 'RunCollatz.in'
output_file = 'RunCollatz.out'
target_dir = '../'
max_ranges = [1,10,50,100,500,1000,5000,10000,50000,100000]
tests_per_maxrange = 50
upper_bound = 999999

# ------------
# cycle_length
# ------------

def cycle_length (n, cache) :
  # base case: if cached, return cached value
  # note: pre-load cache with {1:1,2:2}
  if n in cache :
    return cache[n]

  if n % 2 == 0:
    l = 1 + cycle_length (n // 2, cache)
  else:
    l = 2 + cycle_length (n + (n >> 1) + 1, cache)

  # cache and return cycle length
  cache[n] = l
  return l


# ------------
# collatz_eval
# ------------

def collatz_eval (i, j, cache) :
  """
  i the beginning of the range, inclusive
  j the end       of the range, inclusive
  return the max cycle length of the range [i, j]
  """
  # pre-conditions
  assert isinstance (i, int) and isinstance (j, int)
  assert 0 < i and i <= upper_bound
  assert 0 < j and j <= upper_bound
  if i > j:
    i, j = j, i

  max_len = 1
  
  for n in range (i, j + 1) :
    # get cycle length for n 
    l = cycle_length (n, cache)

    # store max_len found so far
    if l > max_len:
      max_len = l
    
  return max_len

# ----------
# make_range
# ----------

def get_range (max_range) :
  i = randint(lower_bound, upper_bound)
  j = 0
  sign = 0
  while sign == 0 :
    sign = randint (-1, 1)
  if sign < 0 :
    j = i - randint (0, min ([i, randint(0, max_range)]))
  else :
    j = i + randint (0, min ([upper_bound-i, randint(0, max_range)]))
  return [i, j]


with open(EID+'-'+input_file, 'w') as i_file, open(EID+'-'+output_file, 'w') as o_file :
  lower_bound = 1
  cache = {1:1,2:2}
  test_no = 1

  for max_range in max_ranges :
    print ('new max_range: ' + str(max_range))
    for n in range(tests_per_maxrange) :
      i, j = get_range(max_range) 
      # print ('range: ' + str(abs(i-j)))

      test_range = str(i) + ' ' + str(j)
      max_len = str(collatz_eval(i, j, cache))
      
      print(test_range, file = i_file)
      print(test_range + ' ' + max_len, file = o_file)
      print('added test ' + str(test_no) + ': ' + test_range + ' ' + max_len)
      test_no += 1

copy (EID+'-'+input_file, target_dir + input_file)
copy (EID+'-'+output_file, target_dir + output_file)
