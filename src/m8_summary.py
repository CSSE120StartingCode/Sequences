"""
This module lets you practice two forms of the ACCUMULATOR pattern:
  -- SUMMING
  -- COUNTING
where the accumulation is done via ITERATING (i.e., looping)
through a SEQUENCE.

It also demonstrates the distinction between:
  -- an INDEX of the sequence (e.g., -5 is at index 1 in [0, -5, 12, -6]) and
  -- the item AT an index (e.g., the item at index 3 in [0, -5, 12, -6] is -6).

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import testing_helper
import time


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_summary1a()
    run_test_summary1b()
    run_test_summary1c()


###############################################################################
# TODO: 2.  READ the green doc-string for the:
#     - is_prime
#   function defined below.  You do NOT need to understand its
#   implementation, just its specification (per the doc-string).
#   You should  ** CALL **  this function as needed in implementing the
#   other functions.  After you have READ this, change its _TODO_ to DONE.
###############################################################################
def is_prime(n):
    """
    What comes in:  An integer n >= 2.
    What goes out:
      -- Returns True if the given integer is prime,
         else returns False.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
    Note: The algorithm used here is simple and clear but slow.
    """
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  is_prime  function - it has no _TODO_.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------


def run_test_summary1a():
    """ Tests the   summary1a   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   summary1a   function:')
    print('--------------------------------------------------')

    format_string = '    summary1a( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 4
    sequence = (20, 23, 29, 30, 33, 29, 100, 2, 4)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 4
    sequence = (23, 29, 30, 33, 29, 100, 2)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 3
    sequence = (20, 29, 30, 33, 29, 100, 100, 99, 40, 30, 30, 2)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 3
    sequence = (29, 29, 30, 33, 29, 100, 100, 99, 40, 30, 30)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 2
    sequence = (30, 33, 29, 17, 100, 99, 40, 30, 30)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 1
    sequence = (30, 33, 13, 100, 99, 40, 30, 30)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 0
    sequence = (30, 33, 4, 10, 21, 100, 99, 40, 30, 30)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 3
    sequence = (5, 3, 3)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 2
    sequence = (5, 3)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = 1
    sequence = (5,)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = 0
    sequence = ()
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def summary1a(sequence):
    """
    What comes in:  A sequence of integers, all >= 2.
    What goes out:
      -- Returns the number of items in the sequence that are prime.
    Side effects:   None.
    Examples:
      -- If the given sequence is [20, 23, 29, 30, 33, 29, 100, 2, 4],
         then the returned value is 4, since 23, 29, 29, and 2
         are the 4 primes in the sequence.
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    # -------------------------------------------------------------------------


def run_test_summary1b():
    """ Tests the   summary1b   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   summary1b   function:')
    print('--------------------------------------------------')

    format_string = '    summary1b( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 83
    sequence = (20, 23, 29, 30, 33, 29, 100, 2, 4)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 83
    sequence = (23, 29, 30, 33, 29, 100, 2)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 60
    sequence = (20, 29, 30, 33, 29, 100, 100, 99, 40, 30, 30, 2)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 87
    sequence = (29, 29, 30, 33, 29, 100, 100, 99, 40, 30, 30)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 46
    sequence = (30, 33, 29, 17, 100, 99, 40, 30, 30)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 13
    sequence = (30, 33, 13, 100, 99, 40, 30, 30)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 0
    sequence = (30, 33, 4, 10, 21, 100, 99, 40, 30, 30)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 11
    sequence = (5, 3, 3)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 8
    sequence = (5, 3)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = 5
    sequence = (5,)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = 0
    sequence = ()
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def summary1b(seq):
    """
    What comes in:  A sequence of integers, all >= 2.
    What goes out:
      -- Returns the sum of items in the sequence that are prime.
    Side effects:   None.
    Examples:
      -- If the given sequence is [20, 23, 29, 30, 33, 29, 100, 2, 4],
         then the returned value is 83, since the primes in the sequence
         are 23, 29, 29, and 2, and 23 + 29 + 29 + 2 = 83.
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    # -------------------------------------------------------------------------


def run_test_summary1c():
    """ Tests the   summary1c   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   summary1c   function:')
    print('--------------------------------------------------')

    format_string = '    summary1c( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 1 + 2 + 5 + 7  # which is 15
    sequence = (20, 23, 29, 30, 33, 29, 100, 2, 4)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 1 + 4 + 6  # which is 11
    sequence = (23, 29, 30, 33, 29, 100, 2)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 16
    sequence = (20, 29, 30, 33, 29, 100, 100, 99, 40, 30, 30, 2)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 5
    sequence = (29, 29, 30, 33, 29, 100, 100, 99, 40, 30, 30)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 5
    sequence = (30, 33, 29, 17, 100, 99, 40, 30, 30)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 2
    sequence = (30, 33, 13, 100, 99, 40, 30, 30)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 0
    sequence = (30, 33, 4, 10, 21, 100, 99, 40, 30, 30)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 3
    sequence = (5, 3, 3)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 1
    sequence = (5, 3)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = 0
    sequence = (5,)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = 0
    sequence = ()
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = 0
    sequence = (4,)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = summary1c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def summary1c(sequence):
    """
    What comes in:  A sequence of integers, all >= 2.
    What goes out:
      -- Returns the sum of INDICES of the items in the sequence
           that are prime.
    Side effects:   None.
    Examples:
      -- If the given sequence is [20, 23, 29, 30, 33, 29, 100, 2, 4],
         then the returned value is 15, since the primes in the sequence
         are at INDICES 1, 2, 5 and 7, and 1 + 2 + 5 + 7 = 15.
    """
    # -------------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    # -------------------------------------------------------------------------


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string, suffix=''):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string,
                                                 suffix)


def print_actual_result_of_test(expected, actual, test_results,
                                precision=None):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results, precision)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise
