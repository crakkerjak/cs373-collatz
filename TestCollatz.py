#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright(C) 2015
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz  import  \
  collatz_read,       \
  cycle_length,       \
  collatz_eval,       \
  collatz_print,      \
  collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):
  # ----
  # read
  # ----

  # valid input
  def test_read_1(self):
    s    = "1 10\n"
    i, j = collatz_read(s)
    self.assertEqual(i,  1)
    self.assertEqual(j, 10)

  # end == beginning
  def test_read_2(self):
    s    = "10 10\n"
    i, j = collatz_read(s)
    self.assertEqual(i, 10)
    self.assertEqual(j, 10)

  # empty input. should skip and keep going.
  def test_read_3(self):
    s    = ""
    self.assertRaises(ValueError, collatz_read, s)
  
  # empty input. should skip and keep going.
  def test_read_4(self):
    s    = "    "
    self.assertRaises(ValueError, collatz_read, s)

  # ------------
  # cycle_length
  # ------------

  def test_cycle_length_1(self):
    v = cycle_length(1)
    self.assertEqual(v, 1)

  def test_cycle_length_2(self):
    v = cycle_length(9)
    self.assertEqual(v, 20)

  def test_cycle_length_3(self):
    v = cycle_length(500)
    self.assertEqual(v, 111)

  def test_cycle_length_4(self):
    v = cycle_length(100000)
    self.assertEqual(v, 129)

  def test_cycle_length_5(self):
    v = cycle_length(500000)
    self.assertEqual(v, 152)

  def test_cycle_length_6(self):
    v = cycle_length(837799)
    self.assertEqual(v, 525)

  def test_cycle_length_7(self):
    v = cycle_length(999999)
    self.assertEqual(v, 259)


  # ----
  # eval
  # ----

  # valid range tests at "tile" boundaries
  def test_eval_1(self):
    v = collatz_eval(1, 10)
    self.assertEqual(v, 20)

  def test_eval_2(self):
    v = collatz_eval(100, 200)
    self.assertEqual(v, 125)

  def test_eval_3(self):
    v = collatz_eval(201, 210)
    self.assertEqual(v, 89)

  def test_eval_4(self):
    v = collatz_eval(900, 1000)
    self.assertEqual(v, 174)

  # minimum range, args equal
  def test_eval_5(self):
    v = collatz_eval(1, 1)
    self.assertEqual(v, 1)

  # full range
  def test_eval_6(self):
    v = collatz_eval(1, 999999)
    self.assertEqual(v, 525)

  # same result, args equal x2
  def test_eval_7(self):
    self.assertEqual(collatz_eval(999998, 999998), collatz_eval(999999, 999999))

  # min range correctness, eval(10) < min(eval(9) eval(11)), args equal
  def test_eval_8(self):
    v = collatz_eval(10, 10)
    self.assertEqual(v, 7)

  # range boundaries inverted
  def test_eval_9(self):
    v = collatz_eval(10, 1)
    self.assertEqual(v, 20)
  
  # "You can assume that no operation overflows a 32-bit integer."

  # -----
  # print
  # -----

  # valid output
  def test_print_1(self):
    w = StringIO()
    collatz_print(w, 1, 10, 20)
    self.assertEqual(w.getvalue(), "1 10 20\n")

  # -----
  # solve
  # -----

  # valid input, multi-line
  def test_solve_1(self):
    r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
    w = StringIO()
    collatz_solve(r, w)
    self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

  # one valid input, no new-line
  def test_solve_2(self):
    r = StringIO("1 10")
    w = StringIO()
    collatz_solve(r, w)
    self.assertEqual(w.getvalue(), "1 10 20\n")
  
  # range boundaries inverted
  def test_solve_3(self):
    r = StringIO("10 1\n200 100\n210 201\n1000 900\n")
    w = StringIO()
    collatz_solve(r, w)
    self.assertEqual(w.getvalue(), "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

  # empty line inserted
  def test_solve_4(self):
    r = StringIO("10 1\n200 100\n\n210 201\n1000 900\n")
    w = StringIO()
    collatz_solve(r, w)
    self.assertEqual(w.getvalue(), "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

  # line with only white space inserted
  def test_solve_5(self):
    r = StringIO("10 1\n200 100\n    \n210 201\n1000 900\n")
    w = StringIO()
    collatz_solve(r, w)
    self.assertEqual(w.getvalue(), "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")


# ----
# main
# ----

if __name__ == "__main__": # pragma: no cover
  main()

""" # pragma: no cover
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m           >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name      Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz      18    0    6    0   100%
TestCollatz    33    1    2    1  94%   79
---------------------------------------------------------
TOTAL      51    1    8    1  97%
"""
