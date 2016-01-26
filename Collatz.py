#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

cache = {1:1,2:2}

# ------------
# collatz_read
# ------------

def collatz_read (s) :
  """
  read two ints
  s a string
  return a list of two ints, representing the beginning and end of a range, [i, j]
  """
  # pre-condition
  assert isinstance(s, str)
  
  s = s.split()

  # post-conditions
  assert len(s) == 2
  try: 
    i, j = ([int(n) for n in s])
  except ValueError:
    assert 0
  assert 0 < i and i < 1000000
  assert 0 < j and j < 1000000
  
  return [i, j]

# ------------
# cycle_length
# ------------

def cycle_length (n) :
  # base case: if cached, return cached value
  # note: pre-load cache with at least {1:1}
  global cache
  if n in cache :
    return cache[n]

  if n % 2 == 0:
    l = 1 + cycle_length (n // 2)
  else:
    l = 2 + cycle_length (n + (n >> 1) + 1)

  # cache and return cycle length
  cache[n] = l
  return l


# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
  """
  i the beginning of the range, inclusive
  j the end       of the range, inclusive
  return the max cycle length of the range [i, j]
  """
  # pre-conditions
  assert isinstance (i, int) and isinstance (j, int)
  assert 0 < i and i < 1000000
  assert 0 < j and j < 1000000
  if i > j:
    i, j = j, i

  max_len = 1
  
  for n in range (i, j + 1) :
    # get cycle length for n 
    l = cycle_length (n)

    # store max_len found so far
    if l > max_len:
      max_len = l
    
  return max_len


# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
  """
  print three ints
  w a writer
  i the beginning of the range, inclusive
  j the end       of the range, inclusive
  v the max cycle length
  """
  
  # pre-conditions
  assert hasattr(w, 'write')
  assert isinstance (i, int) and isinstance (j, int) and isinstance(v, int)
  assert 0 < i and i < 1000000
  assert 0 < j and j < 1000000

  w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
  """
  r a reader
  w a writer
  """
  
  # pre-conditions
  assert hasattr(r, 'read')
  assert hasattr(w, 'write')

  for s in r :
    i, j = collatz_read(s)
    v  = collatz_eval(i, j)
    collatz_print(w, i, j, v)