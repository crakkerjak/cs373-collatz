#!/usr/bin/env python3
from array import array
from Collatz import collatz_eval

TILES = 10000
UPPER_BOUND = 1000000

tile_size = UPPER_BOUND // TILES
lengths = []
for i in range (1, UPPER_BOUND, tile_size) :
  j = i + tile_size - 1
  if j == UPPER_BOUND :
    j -= 1
  max_len = collatz_eval(i, j)
  lengths.append(max_len)

print ('TILES = array(\'i\',[' + str(lengths[0]), end='')
for l in range(1, len(lengths)) :
  print (',' + str(lengths[l]), end='')
print ('])')
# index into array with [n // (UPPER_BOUND // TILES)]