#!/usr/bin/env python3

#--------
# imports
#--------

from random import randint
from shutil import copy

EID = 'cat3263'
INPUT_FILE = 'RunCollatz.in'
OUTPUT_FILE = 'RunCollatz.out'
TEST_FILE = 'TestCollatz.py'
TARGET_DIR = 'collatz-tests'
MAX_RANGES = [1,10,50,100,500,1000,5000,10000,50000,100000]
TESTS_PER_MAXRANGE = 15
UPPER_BOUND = 999999

# ------------
# cycle_length
# ------------

def cycle_length(n, cache) :
  if n in cache :
    return cache[n]

  if n % 2 == 0:
    l = 1 + cycle_length(n // 2, cache)
  else:
    l = 2 + cycle_length(n +(n >> 1) + 1, cache)

  # cache and return cycle length
  cache[n] = l
  return l


# ------------
# collatz_eval
# ------------

def collatz_eval(i, j, cache) :
  """
  i the beginning of the range, inclusive
  j the end       of the range, inclusive
  return the max cycle length of the range [i, j]
  """
  # pre-conditions
  assert isinstance(i, int) and isinstance(j, int)
  assert 0 < i and i <= UPPER_BOUND
  assert 0 < j and j <= UPPER_BOUND
  if i > j:
    i, j = j, i

  max_len = 1
  
  for n in range(i, j + 1) :
    # get cycle length for n 
    l = cycle_length(n, cache)

    # store max_len found so far
    if l > max_len:
      max_len = l
    
  return max_len

def get_range(max_range) :
  i = randint(lower_bound, UPPER_BOUND)
  j = 0
  sign = 0
  while sign == 0 :
    sign = randint(-1, 1)
  if sign < 0 :
    j = i - randint(0, min([i, randint(0, max_range)]))
  else :
    j = i + randint(0, min([UPPER_BOUND-i, randint(0, max_range)]))
  return [i, j]

with open(INPUT_FILE, 'w') as i_file, open(OUTPUT_FILE, 'w') as o_file :
  lower_bound = 1
  cache = {1:1,2:2}
  test_no = 1

  # write specific tests
  # end of range has highest cycle length
  print('1 9', file = i_file)
  print('1 9 ' + str(collatz_eval(1, 9, cache)), file = o_file)    
  # inverted range endpoints
  print('10 1', file = i_file)
  print('10 1 ' + str(collatz_eval(10, 1, cache)), file = o_file)
  # end of valid input range
  print('999998 999999', file = i_file)
  print('999998 999999 ' + str(collatz_eval(999998, 999999, cache)), file = o_file)
  # single int valley range
  print('10 10', file = i_file)
  print('10 10 ' + str(collatz_eval(10, 10, cache)), file = o_file)
  # blank input line, code should skip it and continue (no output)
  print('', file = i_file)
  # input line with only white space, code should skip it and continue
  print('    ', file = i_file)

  # generate and write random tests
  for max_range in MAX_RANGES :
    for n in range(TESTS_PER_MAXRANGE) :
      i, j = get_range(max_range) 
      
      test_range = str(i) + ' ' + str(j)
      max_len = str(collatz_eval(i, j, cache))
      
      print(test_range, file = i_file)
      print(test_range + ' ' + max_len, file = o_file)
      test_no += 1
    
# copy files to public repo directory
if TARGET_DIR != '' :
  for f in [INPUT_FILE, OUTPUT_FILE] :
    copy(f, TARGET_DIR + '/' + EID + '-' + f)
