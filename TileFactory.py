#!/usr/bin/env python3
from array import array
from Collatz import collatz_eval

tiles = 10000
upper_bound = 1000000

tile_size = upper_bound // tiles
# tile_no = 0
lengths = []
for i in range (1, upper_bound, tile_size) :
  j = i + tile_size - 1
  if j == upper_bound :
    j -= 1
  max_len = collatz_eval(i, j)
  lengths.append(max_len)
  # print (str(tile_no), str(i), str(j), str(max_len))
  # tile_no += 1

print ('tiles = array(\'i\',[' + str(lengths[0]), end='')
for l in range(1, len(lengths)) :
  print (',' + str(lengths[l]), end='')
print ('])')
# index into array with [n // (upper_bound // tiles)]