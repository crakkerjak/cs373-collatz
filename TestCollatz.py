#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2015
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    # valid input
    def test_read_1 (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    # end < beginning
    def test_read_2 (self) :
        s    = "10 1\n"
        self.assertRaises(AssertionError, collatz_read, s)

    # end == beginning
    def test_read_3 (self) :
        s    = "10 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, j)
        self.assertEqual(i, 10)

    # input too long
    def test_read_4 (self) :
        s    = "1 10 100\n"
        self.assertRaises(AssertionError, collatz_read, s)

    #input too short
    def test_read_5 (self) :
        s    = "1\n"
        self.assertRaises(AssertionError, collatz_read, s)

    # lower bound too low
    def test_read_6 (self) :
        s    = "0 10\n"
        self.assertRaises(AssertionError, collatz_read, s)

    # upper bound too high 
    def test_read_7 (self) :
        s    = "1 1000000\n"
        self.assertRaises(AssertionError, collatz_read, s)

    # lower bound not a number
    def test_read_8 (self) :
        s    = "a 1\n"
        self.assertRaises(AssertionError, collatz_read, s)
    
    # upper bound not a number
    def test_read_9 (self) :
        s    = "1 a\n"
        self.assertRaises(AssertionError, collatz_read, s)

    # lower bound not an integer
    def test_read_10 (self) :
        s    = "1.5 2\n"
        self.assertRaises(AssertionError, collatz_read, s)

    # upper bound not an integer
    def test_read_11 (self) :
        s    = "1 2.5\n"
        self.assertRaises(AssertionError, collatz_read, s)

    # s not a string
    def test_read_11 (self) :
        s    = [1, 10]
        self.assertRaises(AssertionError, collatz_read, s)


    # ----
    # eval
    # ----

    # valid range tests
    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    # minimum range, low
    def test_eval_5 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    # minimum range, low
    def test_eval_6 (self) :
        v = collatz_eval(1, 2)
        self.assertEqual(v, 2)

    # same result, high
    def test_eval_7 (self) :
        self.assertEqual(collatz_eval(999998, 999998), collatz_eval(999999, 999999))

    # min range correctness, eval(10) < min(eval(9) eval(11))
    def test_eval_8 (self) :
        v = collatz_eval(10, 10)
        self.assertEqual(v, 7)

    # range boundaries inverted
    def test_eval_9 (self) :
        self.assertRaises(AssertionError, collatz_eval, 2, 1)
    
    # lower bound not an int
    def test_eval_10 (self) :
        self.assertRaises(AssertionError, collatz_eval, 1.5, 2)
    
    # upper bound not an int
    def test_eval_11 (self) :
        self.assertRaises(AssertionError, collatz_eval, 1, 3.5)
    
    # lower bound not a number
    def test_eval_12 (self) :
        self.assertRaises(AssertionError, collatz_eval, 'a', 2)
    
    # upper bound not a number
    def test_eval_13 (self) :
        self.assertRaises(AssertionError, collatz_eval, 1, 'a')
    
    # lower bound too low
    def test_eval_14 (self) :
        self.assertRaises(AssertionError, collatz_eval, 0, 1)
    
    # upper bound too high
    def test_eval_15 (self) :
        self.assertRaises(AssertionError, collatz_eval, 1, 1000000)
    
    # "You can assume that no operation overflows a 32-bit integer."

    # -----
    # print
    # -----

    # valid output
    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # last args not numbers (x3)
    def test_print_2 (self) :
        w = StringIO()
        self.assertRaises(AssertionError, collatz_print, w, 'a', 10, 20)

    def test_print_3 (self) :
        w = StringIO()
        self.assertRaises(AssertionError, collatz_print, w, 1, 'a', 20)

    def test_print_4 (self) :
        w = StringIO()
        self.assertRaises(AssertionError, collatz_print, w, 1, 10, 'a')

    # last args not integers (x3)
    def test_print_5 (self) :
        w = StringIO()
        self.assertRaises(AssertionError, collatz_print, w, 1.5, 10, 20)

    def test_print_6 (self) :
        w = StringIO()
        self.assertRaises(AssertionError, collatz_print, w, 1, 10.5, 20)

    def test_print_7 (self) :
        w = StringIO()
        self.assertRaises(AssertionError, collatz_print, w, 1, 10, 20.5)

    # first arg not a writer
    def test_print_8 (self) :
        w = StringIO()
        self.assertRaises(AssertionError, collatz_print, 'a', 1, 10, 20)

    # -----
    # solve
    # -----

    # valid input, multi-line
    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # one valid input, no new-line
    def test_solve_2 (self) :
        r = StringIO("1 10")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # non-numerical input
    def test_solve_3 (self) :
        r = StringIO("1 10\n100 200\n201 21a\n900 1000\n")
        w = StringIO()
        self.assertRaises(AssertionError, collatz_solve, r, w)

    # missing new-line character / input line too long
    def test_solve_4 (self) :
        r = StringIO("1 10\n100 200 201 21a\n900 1000\n")
        w = StringIO()
        self.assertRaises(AssertionError, collatz_solve, r, w)
    
    # range boundaries inverted
    def test_solve_5 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 800\n")
        w = StringIO()
        self.assertRaises(AssertionError, collatz_solve, r, w)

    # r not a reader
    def test_solve_6 (self) :
        r = "1 10\n100 200\n201 210\n900 1000\n"
        w = StringIO()
        self.assertRaises(AssertionError, collatz_solve, r, w)

    # w not a writer
    def test_solve_7 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = ""
        self.assertRaises(AssertionError, collatz_solve, r, w)


# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
