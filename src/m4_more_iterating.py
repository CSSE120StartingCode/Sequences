"""
This module lets you practice two forms of the ACCUMULATOR pattern:
  -- SUMMING
  -- COUNTING
where the accumulation is done via ITERATING (i.e., looping)
through a SEQUENCE.

It also demonstrates using an ORACLE and/or PROBABILITY THEORY
in testing and BOUNDARY (EDGE) TESTING.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import random
import builtins  # Never necessary, but here to make a point about SUM
import math
import time

# -----------------------------------------------------------------------------
# TODO: 2. Watch the VIDEO for this module listed in the Follow-Me section
#  of the Preparation for this session.  It explains the various kinds of
#  TESTING that are used in this module.
#    After you have watched that video, mark this _TODO_ as DONE.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# The first of the two statements below makes each run of the program
#   use the same sequence of pseudo-random numbers.
# The second of the two statements below makes each run of the program
#   use a hard-to-predict sequence of pseudo-random numbers (one that depends
#   on the time of day), hence makes the sequence differ from run to run
#   in a way that appears random.
# -----------------------------------------------------------------------------

# random.seed(42)
random.seed((time.time() * 100) % 1000)


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_sequence()
    run_test_count_items_bigger_than()
    run_test_count_positive_sines()
    run_test_sum_first_n()


def run_test_sum_sequence():
    """ Tests the   sum_sequence   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   sum_sequence   function:")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # TODO: 3. READ the COMMENTS and CODE in this function,
    #   asking questions as needed.
    #   ___
    #   When you believe that you understand:
    #     -- What an ORACLE is
    #     -- How one can generate and use RANDOM test cases
    #     -- How one can test using PROBABILITY THEORY
    #   then:
    #      change the above _TODO_ to DONE.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Here (below) are examples of using an ORACLE for testing,
    # that is, using a separate way of gaining the correct tests as if
    # by "magic". The oracle here is the built-in    sum    function.
    # We provided two tests that use that oracle.
    #
    # BTW, google for  "Oracle of Delphi" if you are curious about
    # why we call such tests "oracles".
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Test 1 (using an ORACLE to computer the expected answer):
    # -------------------------------------------------------------------------
    sequence1 = [48, -10, 100, 9939309808, 433443080, -45634930]

    oracle_answer = builtins.sum(sequence1)
    actual_answer = sum_sequence(sequence1)

    print()
    print("Test 1: Using the sequence:")
    print("   ", sequence1)
    print("  Expected (oracle) result: ", oracle_answer)
    print("  Actual result:            ", actual_answer)

    # -------------------------------------------------------------------------
    # Test 2 (using an ORACLE to computer the expected answer):
    # -------------------------------------------------------------------------
    sequence2 = [48, 180, -475, 205, 88]

    oracle_answer = builtins.sum(sequence2)
    actual_answer = sum_sequence(sequence2)

    print()
    print("Test 2: Using the sequence:")
    print("   ", sequence2)
    print("  Expected (oracle) result: ", oracle_answer)
    print("  Actual result:            ", actual_answer)

    # -------------------------------------------------------------------------
    # Test 3 (using an ORACLE to compute the expected answer):
    #
    #   This test uses a RANDOMLY generated sequence,
    #   so every time you run the program it does a DIFFERENT test!
    #   So this code snippet can be used to do MANY tests!
    # -------------------------------------------------------------------------

    # The next few lines make a sequence of 10,000 RANDOM numbers:
    sequence3 = []
    for _ in range(10000):
        sequence3.append(random.randrange(-10, 11))

    oracle_answer = builtins.sum(sequence3)
    actual_answer = sum_sequence(sequence3)

    print()
    print("Test 3: Using the following RANDOMLY generated sequence:")
    print("  Un-comment the relevant line of code if you want")
    print("  to see the actual sequence.")
    # print("   ", sequence3)
    print("  Expected (oracle) result: ", oracle_answer)
    print("  Actual result:            ", actual_answer)

    # -------------------------------------------------------------------------
    # Tests 4 and 5:  using a KNOWN answer
    #   (here, ones easily computed by hand).]
    #
    #   Test 5 is an example of BOUNDARY (aka EDGE) testing, which is:
    #
    #       Where test cases are generated using the EXTREMES of the
    #       input domain, e.g. maximum, minimum, just inside/outside
    #       boundaries, error values. It focuses] on "corner cases".
    #
    #   The above quotation is a slight paraphrase from the Wikipedia
    #   article at https://en.wikipedia.org/wiki/Boundary_testing.
    # -------------------------------------------------------------------------

    # Test 4:
    sequence4 = [48, -10]

    known_answer = 38
    actual_answer = sum_sequence(sequence4)

    print()
    print("Test 4: Using the sequence:")
    print("   ", sequence4)
    print("  Expected (known) result: ", known_answer)
    print("  Actual result:           ", actual_answer)

    # Test 5:
    sequence5 = []

    known_answer = 0
    actual_answer = sum_sequence(sequence5)

    print()
    print("Test 5: Using the sequence:")
    print("   ", sequence5)
    print("  Expected (known) result: ", known_answer)
    print("  Actual result:           ", actual_answer)

    # -------------------------------------------------------------------------
    # Test 6:  (Don't worry if you don't follow this example fully.)
    #
    #   Like Test 3, this test uses a RANDOMLY generated sequence.
    #
    #   But unlike Test 3 (which used an ORACLE),
    #   THIS example uses PROBABILITY THEORY to predict (approximately)
    #   the expected value.
    #
    #   It relies on what is called the
    #      Law of Large Numbers
    #   which, as applied here says:
    #      If you compute the average of a lot of numbers with each
    #      number drawn RANDOMLY from -10 to 10 (inclusive),
    #      the result should be close to the average of the numbers
    #      from -10 to 10 (inclusive) [which is 0].
    #
    #   See https://en.wikipedia.org/wiki/Law_of_large_numbers
    #   for a not-too-clear explanation of the Law of Large Numbers.
    # -------------------------------------------------------------------------

    # Skips this test if  sum_sequence  has not yet been implemented:
    if sum_sequence([1, 2, 3]) == None:
        return

    sequence6 = []  # Next lines make a sequence of 10000 RANDOM numbers
    for _ in range(10000):
        sequence6.append(random.randrange(-10, 11))

    expected_sum_from_probability_theory = 0
    expected_average_from_probability_theory = 0
    actual_sum = sum_sequence(sequence6)
    actual_average = sum_sequence(sequence6) / 10000

    print()
    print("Test 6: Using the following RANDOMLY generated sequence:")
    print("  Un-comment the relevant line of code to see the actual sequence.")
    # print("   ", sequence6)

    print("  Expected results (from PROBABILITY THEORY):")
    print("    Sum:     ", expected_sum_from_probability_theory)
    print("    Average: ", expected_average_from_probability_theory)
    print("  ACTUAL results (should be CLOSE to the above)")
    print("    Sum:     ", actual_sum)
    print("    Average: ", actual_average)
    print("  where 'close' for the sum means absolute value < about 1216")
    print("  most of the time (about 19 times out of 20)")


def sum_sequence(sequence):
    """
    What comes in:  A sequence of integers.
    What goes out: Returns the sum of the numbers in the given sequence.
    Side effects: None.
    Examples:
      sum_sequence([8, 13, 7, -5])  returns  23
      sum_sequence([48, -10])       returns  38
      sum_sequence([])              returns  0
    Type hints:
      :type sequence: list or tuple (of integers)
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #   ___
    #   RESTRICTION:
    #     You may NOT use the built-in  sum   function
    #     in IMPLEMENTING this function.
    #       -- The TESTING code above does use   built_ins.sum
    #          as an ORACLE in TESTING this function, however.
    # -------------------------------------------------------------------------


def run_test_count_items_bigger_than():
    """ Tests the   count_items_bigger_than   function. """
    # -------------------------------------------------------------------------
    # TODO: 5. Implement this TEST function.
    #   It TESTS the  count_items_bigger_than  function defined below.
    #   Include at least ** 2 ** ADDITIONAL tests.
    #
    #   As usual, include both EXPECTED and ACTUAL results in your test
    #   and compute the latter BY HAND (not by running your program).
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   count_items_bigger_than   function:")
    print("--------------------------------------------------")

    # Test 1:
    sequence = [45, 84, 32, 70, -10, 40]
    threshold = 45
    expected = 2
    actual = count_items_bigger_than(sequence, threshold)
    print()
    print("Test 1 expected:", expected)
    print("       actual:  ", actual)

    # Test 2:
    sequence = [45, 84, 32, 70, -10, 40]
    threshold = 0
    expected = 5
    actual = count_items_bigger_than(sequence, threshold)
    print()
    print("Test 2 expected:", expected)
    print("       actual:  ", actual)

    # Test 3:
    sequence = [45, 84, 32, 70, -10, 40]
    threshold = -10
    expected = 5
    actual = count_items_bigger_than(sequence, threshold)
    print()
    print("Test 3 expected:", expected)
    print("       actual:  ", actual)

    # Test 4:
    sequence = [45, 84, 32, 70, -10, 40]
    threshold = -10.000000001
    expected = 6
    actual = count_items_bigger_than(sequence, threshold)
    print()
    print("Test 4 expected:", expected)
    print("       actual:  ", actual)

    # Test 5:
    sequence = []
    threshold = -99999999999999999999999999999
    expected = 0
    actual = count_items_bigger_than(sequence, threshold)
    print()
    print("Test 5 expected:", expected)
    print("       actual:  ", actual)

    # Test 6:  This test uses a RANDOMLY generated sequence
    #          but a KNOWN answer (NONE in the sequence are > threshold)

    # Next lines make a sequence of 100,000 RANDOM numbers,
    # with each chosen from -100 to 99 (inclusive):
    sequence = []
    for _ in range(100000):
        sequence.append(random.randrange(-100, 100))

    threshold = 99.000000001
    expected = 0
    actual = count_items_bigger_than(sequence, threshold)
    print()
    print("Test 6 expected:", expected)
    print("       actual:  ", actual)

    # Test 7:  This test uses a RANDOMLY generated sequence
    #          but a KNOWN answer (ALL in the sequence are > threshold).

    # Next lines make a sequence of 100,000 RANDOM numbers,
    # with each chosen from -100 to 99 (inclusive):
    sequence = []
    for _ in range(100000):
        sequence.append(random.randrange(-100, 100))

    threshold = -100.00000001
    expected = 100000
    actual = count_items_bigger_than(sequence, threshold)
    print()
    print("Test 7 expected:", expected)
    print("       actual:  ", actual)

    # Test 8:  This test uses a RANDOMLY generated sequence
    #          and an APPROXIMATE answer that is PROBABLY about right,
    #          based on PROBABILITY THEORY (the Law of Large Numbers).

    # Next lines make a sequence of 100,000 RANDOM numbers,
    # with each chosen from -100 to 99 (inclusive):
    sequence = []
    n = 100000
    for _ in range(n):
        sequence.append(random.randrange(-100, 100))

    threshold = 98
    expected = n * (1 / 200)
    actual = count_items_bigger_than(sequence, threshold)
    standard_deviation = math.sqrt(n * (1 / 200) * (199 / 200))

    print()
    print("Test 8 uses PROBABILITY THEORY")
    print("  to compute the expected result.")
    print("  See the note that follows to see")
    print("  how to evaluate the results of this test.")
    print("       expected:", expected)
    print("       actual:  ", actual)

    print()
    print("  Note on how to evaluate the results of")
    print("  Test 8 (above): According to Probability Theory,")
    message = "  the above 'actual' should be within {:.0f}"
    print(message.format(2 * standard_deviation))
    print("  of the above 'expected' about 95 percent of the time.")
    print()
    print("  You might try running this program multiple times")
    print("  to see whether or not that seems to be true")
    print("  for your code (and Python's pseudo-random numbers).")

    # TODO: 5 (continued):  Add your 2 ADDITIONAL tests here:


def count_items_bigger_than(numbers, threshold):
    """
    What comes in:
      -- An sequence of numbers.
      -- A number that is a "threshold".
    What goes out:
      Returns the number of items in the given sequence of numbers
      that are strictly bigger than the given "threshold" number.
    Side effects: None.
    Examples:
      If  numbers   is  [45, 84, 32, 70, -10, 40]
      and threshold is 45,
      then this function returns 2 (since 84 and 70 are bigger than 45).

      If  numbers   is  [45, 84, 32, 70, -10, 40]
      and threshold is 0,
      then this function returns 5
      (since all of the 6 numbers except -10 are bigger than 0).

      If  numbers   is  [45, 84, 32, 70, -10, 40]
      and threshold is -10,
      then this function still returns 5
      (since all of the 6 numbers except -10 are bigger than -10;
      note that -10 is NOT bigger than itself).

      If  numbers   is  [45, 84, 32, 70, -10, 40]
      and threshold is -10.00000001,
      then this function returns 6.

    Type hints:
      :type numbers:   list or tuple (of numbers)
      :type threshold: float
    """
    # -------------------------------------------------------------------------
    # TODO: 6. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # -------------------------------------------------------------------------


def run_test_count_positive_sines():
    """ Tests the   count_positive_sines   function. """
    # -------------------------------------------------------------------------
    # TODO: 7. Implement this TEST function.
    #   It TESTS the  count_positive_sines  function defined below.
    #   Include at least ** 1 ** ADDITIONAL test beyond what we supplied.
    #
    #   As usual, include both EXPECTED and ACTUAL results in your test
    #   and compute the latter BY HAND (not by running your program).
    #
    # NOTE: Some numbers that you might expect to be zero,
    #   for example math.sin(math.pi), are in fact slightly positive.
    #   That is because   math.pi   is not exact (nor is math.sin).
    #   Simply stay away from such test cases in this problem.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   count_positive_sines   function:")
    print("--------------------------------------------------")

    # Test 1:
    expected = 4
    actual = count_positive_sines([3, 4, 5, 6, 7, 8, 9])
    print()
    print("Test 1 expected:", expected)
    print("       actual:  ", actual)

    # Test 2:
    expected = 2
    actual = count_positive_sines([3, 6, 8])
    print()
    print("Test 2 expected:", expected)
    print("       actual:  ", actual)

    # Test 3:
    expected = 3
    actual = count_positive_sines([7, 7, 7])
    print()
    print("Test 3 expected:", expected)
    print("       actual:  ", actual)

    # Test 4:
    expected = 0
    actual = count_positive_sines([6, 6, 6, 6, 6, 6, 6, 6, 6])
    print()
    print("Test 4 expected:", expected)
    print("       actual:  ", actual)

    # Test 5:
    expected = 1
    actual = count_positive_sines([3])
    print()
    print("Test 5 expected:", expected)
    print("       actual:  ", actual)

    # Test 6:
    expected = 0
    actual = count_positive_sines([6])
    print()
    print("Test 6 expected:", expected)
    print("       actual:  ", actual)

    # Test 7:
    expected = 0
    actual = count_positive_sines([5, 4, 6])
    print()
    print("Test 7 expected:", expected)
    print("       actual:  ", actual)

    # Test 8 (using the list [0, 1, 2, ... 1063]
    sequence = []
    for k in range(1064):
        sequence.append(k)

    expected = 532  # Trust me!
    actual = count_positive_sines(sequence)
    print()
    print("Test 8 expected:", expected)
    print("       actual:  ", actual)

    # Test 9 (using the list [0, 1, 2, ... 1064]
    sequence.append(1064)

    expected = 533  # Trust me!
    actual = count_positive_sines(sequence)
    print()
    print("Test 9 expected:", expected)
    print("       actual:  ", actual)

    # Test 10 (using the list [0, 1, 2, ... 1065]
    sequence.append(1065)

    expected = 533  # Trust me!
    actual = count_positive_sines(sequence)
    print()
    print("Test 10 expected:", expected)
    print("        actual:  ", actual)

    # TODO: 7 (continued):  Add your 1 ADDITIONAL test here:


def count_positive_sines(numbers):
    """
    What comes in:  An sequence of numbers.
    What goes out: Returns the number of items in the given sequence
      whose sine is positive.
    Side effects: None.

    Examples:  Since:
       sine(3) is about 0.14
       sine(4) is about -0.76
       sine(5) is about -0.96
       sine(6) is about -0.28
       sine(7) is about 0.66
       sine(8) is about 0.99
       sine(9) is about 0.41

      -- count_positive_sines([3, 4, 5, 6, 7, 8, 9])  returns 4
      -- count_positive_sines([3, 6, 8])              returns 2
      -- count_positive_sines([7, 7, 7])              returns 3

    Type hints:
      :type sequence: list or tuple (of numbers)
    """
    # -------------------------------------------------------------------------
    # TODO: 8. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # -------------------------------------------------------------------------


def run_test_sum_first_n():
    """ Tests the   sum_first_n   function. """
    # -------------------------------------------------------------------------
    # TODO: 9. Implement this TEST function.
    #   It TESTS the  sum_first_n  function defined below.
    #   Include at least ** 2 ** ADDITIONAL tests.
    #   ___
    #   As usual, include both EXPECTED and ACTUAL results in your test
    #   and compute the latter BY HAND (not by running your program).
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   sum_first_n   function:")
    print("--------------------------------------------------")

    # Test 1:
    expected = 0
    actual = sum_first_n([48, -10, 50, 5], 0)
    print()
    print("Test 1 expected:", expected)
    print("       actual:  ", actual)

    # Test 2:
    expected = 48
    actual = sum_first_n([48, -10, 50, 5], 1)
    print()
    print("Test 2 expected:", expected)
    print("       actual:  ", actual)

    # Test 3:
    expected = 38
    actual = sum_first_n([48, -10, 50, 5], 2)
    print()
    print("Test 3 expected:", expected)
    print("       actual:  ", actual)

    # Test 4:
    expected = 88
    actual = sum_first_n([48, -10, 50, 5], 3)
    print()
    print("Test 4 expected:", expected)
    print("       actual:  ", actual)

    # Test 5:
    expected = 93
    actual = sum_first_n([48, -10, 50, 5], 4)
    print()
    print("Test 5 expected:", expected)
    print("       actual:  ", actual)

    # Test 6:  This test uses a RANDOMLY generated sequence
    #          and an ORACLE to determine the expected (correct) result.
    sequence = []
    for _ in range(10000):
        sequence.append(random.randrange(-100, 100))
    expected = builtins.sum(sequence[:-1])
    actual = sum_first_n(sequence, 9999)
    print()
    print("Test 6 expected:", expected)
    print("       actual:  ", actual)

    # Test 7:  This test uses a RANDOMLY generated sequence
    #          and an ORACLE to determine the expected (correct) result.
    sequence = []
    for _ in range(10000):
        sequence.append(random.randrange(-100, 100))
    expected = builtins.sum(sequence[:-4000])
    actual = sum_first_n(sequence, 6000)
    print()
    print("Test 7 expected:", expected)
    print("       actual:  ", actual)

    # TODO: 9 (continued):  Add your 2 ADDITIONAL tests here:


def sum_first_n(numbers, n):
    """
    What comes in:
      -- An sequence of numbers.
      -- A nonnegative integer   n   that is less than or equal to
           the length of the given sequence.
    What goes out:
      Returns the sum of the first   n   numbers in the given sequence,
      where   n   is the second argument.
    Side effects: None.
    Examples:
      If numbers is   [48, -10, 50, 5], then:
      - sum_first_n(numbers, 0) returns 0  (the sum of NO numbers is 0)
      - sum_first_n(numbers, 1) returns 48
      - sum_first_n(numbers, 2) returns 38
      - sum_first_n(numbers, 3) returns 88
      - sum_first_n(numbers, 4) returns 93
    Type hints:
      :type numbers:   list of tuple (of numbers)
      :type n: int
    """
    # -------------------------------------------------------------------------
    # TODO: 10. Implement and test this function.
    #           Tests have been written for you (above).
    #  ___
    #  RESTRICTION:
    #    You may NOT use the built-in  sum   function
    #    in IMPLEMENTING this function.
    #      -- The TESTING code above does use   built_ins.sum
    #         as an ORACLE in TESTING this function, however.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
