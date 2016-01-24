#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

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
    
    a = s.split()

    # post-conditions
    assert len(a) == 2
    try: 
        i = int(a[0])
        j = int(a[1])
    except ValueError:
        assert 0    
    assert 0 < i and i < 1000000
    assert 0 < j and j < 1000000
    assert i <= j
    
    return [i, j]

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
    assert i <= j

    max_len = 1
    
    for n in range (i, j + 1):
        # cycle length
        l = 1   

        # Collatz cycle
        while n != 1:
            if n % 2 == 0:
                n = n // 2
                l += 1
            else:
                n = n + (n >> 1) + 1
                l += 2

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
    assert i <= j

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
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
