#!/usr/bin/env python3
from operator import itemgetter

from Collatz import cycle_length

preload_size = 750
max_depth = 20
cache = {1:1,2:2}

# record frequencies of the first 'depth' numbers in each
# of the first 1M sequences
freqs = {}
for n in range (1, 1000000):
  depth = 0
  while n != 1 and depth < max_depth:
    if depth != 0:
      if n in freqs:
        freqs[n] += 1
      else:
        freqs[n] = 1
    if n % 2 == 0:
      n = n // 2
    else:
      n = n + (n >> 1) + 1
    depth += 1

# sort them
sf = sorted(freqs.items(), key=itemgetter(1), reverse=True)

# cache the first 'preload_size' most common numbers
print ('by frequency in the first ' + str(max_depth) + ' iterations:')
print ('cache = {1:1,2:2,' + str(sf[0][0]) + ':' + str(cycle_length(sf[0][0])), end='')
for i in range(1, preload_size - 2):
  print (',' + str(sf[i][0]) + ':' + str(cycle_length(sf[i][0])), end='')
print ('}')



# # cache the first 'preload_size' numbers in counting order
# cache = {}

# print ('by counting order, the first ' + str(preload_size) + ' cycle lengths:')
# print ('cache = {1:1', end='')
# for n in range(2, preload_size):
#   print (',' + str(n) + ':' + str(cycle_length(n)), end='')
# print ('}')

