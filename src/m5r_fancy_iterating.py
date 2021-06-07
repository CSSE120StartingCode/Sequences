"""
This module shows how to ITERATE (i.e. loop) through a SEQUENCE
in ways OTHER than just going thru the sequence from BEGINNING to END.

It also shows how to SELECT items in a sequence, e.g.:
  -- the items that are strings
  -- the items that are even integers (e.g. 2, 4, 6, ...)

Note that:
  -- SELECTING items that ARE even integers
is different from:
  -- LOOKING only at items AT even-numbered indices.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


###############################################################################
# TODO: 2. READ the program below and RUN it.
#   ___
#   When you have read it, asking questions as needed,
#   and you feel that you understand:
#     -- how to loop through a sequence
#          in ways OTHER than just from BEGINNING to END,
#     -- how to SELECT items in sequence
#     -- the distinction between:
#          -- SELECTING items that ARE even integers and
#          -- LOOKING only at items AT even-numbered indices.
#   then:
#      change the above _TODO_ to DONE.
###############################################################################


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_string_lengths()
    run_test_sum_even_integers()
    run_test_sum_items_at_even_indices()


###############################################################################
# The TEST functions are further down in the file,
# so that you can focus on the following examples.
###############################################################################


def sum_string_lengths(sequence, m, n):
    """
    What comes in:
      -- A sequence of strings
      -- Integers m and n,
           where 0 <= m <= n < length of the sequence
           (which ensures that you can safely use m and n as indices)
    What goes out:
      Returns the sum of the lengths of the strings
      at indices m to n, inclusive, with the restriction
      that the loop must go thru the sequence BACKWARDS.
    Side effects:   None.
    Examples:
      Suppose that  sequence  is:
        ["five", "OK", "songs", "roxanne", "the police", "", "three"]
      Then:
        -- sum_string_lengths(sequence, 1, 3)
             returns the length of "roxanne"
             plus the length of "songs" plus the length of "OK",
             which is 7 + 5 + 2, which is 14.

        -- sum_string_lengths(sequence, 2, 6)
             returns the length of "three"
             plus the length of "" plus the length of "the police"
             plus the length of "roxanne" plus the length of "songs,
             which is 5 + 0 + 10 + 7 + 5, which is 27.
    Type hints:
      :type sequence: list or tuple (of strings)
      :type m: int
      :type n: int
    """
    # -------------------------------------------------------------------------
    # EXAMPLE 1.  Iterates through PART of a sequence, BACKWARDS.
    # -------------------------------------------------------------------------
    total = 0
    for k in range(n, m - 1, -1):
        s = sequence[k]
        total = total + len(s)

    return total

    # Here is an alternative (there are other alternatives as well):
    total = 0
    for k in range(m, n + 1):
        total = total + len(sequence[m + n - k])

    return total


def sum_even_integers(sequence):
    """
    What comes in:
      -- A sequence
    What goes out:
      Returns the sum of the items in the sequence that:
        -- are integers AND
        -- are even.
    Side effects:   None.
    Examples:
      sum_even_integers([3, 10, 6, 5, 5, 10])
        returns 10 + 6 + 10, which is 26

      sum_even_integers([3, 9, 10, 99, 101, 5, 6, 5, 5, 10])
        still returns 10 + 6 + 10, which is 26

      sum_even_integers(["hello", 3, 10, 6, "bye", 5, 7.33, 5, 10])
        still returns 10 + 6 + 10, which is 26

    Type hints:
      :type sequence: list or tuple
    """
    # -------------------------------------------------------------------------
    # EXAMPLE 2.  Iterates through a sequence,
    #   identifying and summing the items that are EVEN INTEGERS.
    #
    #   Note how:
    #     -- The TYPE function returns the TYPE of its argument.
    #     -- An integer X is EVEN if the remainder is 0
    #          when you divide X by 2 and take the remainder.
    # -------------------------------------------------------------------------
    total = 0
    for k in range(len(sequence)):
        item = sequence[k]
        if type(item) is int:
            if item % 2 == 0:
                total = total + item

    return total

    # Here is an alternative (there are other alternatives as well):
    total = 0
    for k in range(len(sequence)):
        if (type(sequence[k]) is int) and (sequence[k] % 2 == 0):
            total = total + sequence[k]

    return total


def sum_items_at_even_indices(sequence):
    """
    What comes in:
      -- A sequence of numbers.
    What goes out:
      Returns the sum of the numbers in the list that:
        -- are at EVEN INDICES.
    Side effects:   None.
    Examples:
      sum_items_at_even_indices([3, 10, 6, 5, 5, 10])
        returns 3 + 6 + 5, which is 14

     sum_items_at_even_indices([5.5, 10, 3, 2, 10, 0, 1])
        returns 5.5 + 3 + 10 + 1, which is 19.5

    Type hints:
      :type sequence: list or tuple (of numbers)
    """
    # -------------------------------------------------------------------------
    # EXAMPLE 3.  Iterates through and sums the items in a list
    #   of numbers that are at even INDICES.
    #
    #   Constrast this example with the previous example.
    # -------------------------------------------------------------------------
    total = 0
    for k in range(0, len(sequence), 2):
        total = total + sequence[k]

    return total

    # Here is a ** BAD alternative ** that computes the right result
    # but takes twice as long to do so as needed.
    total = 0
    for k in range(len(sequence)):  # This is a BAD solution
        if k % 2 == 0:
            total = total + sequence[k]

    return total


###############################################################################
# Just TEST functions below here.
###############################################################################


def run_test_sum_string_lengths():
    """ Tests the   sum_string_lengths   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   sum_string_lengths   function:")
    print("--------------------------------------------------")

    seq = ["five", "OK", "songs", "roxanne", "the police", "", "three"]
    total1 = sum_string_lengths(seq, 1, 3)
    total2 = sum_string_lengths(seq, 2, 6)

    print("Returned, expected:", total1, 14)
    print("Returned, expected:", total2, 27)


def run_test_sum_even_integers():
    """ Tests the   sum_even_integers   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   sum_even_integers   function:")
    print("--------------------------------------------------")

    total1 = sum_even_integers([3, 10, 6, 5, 5, 10])
    total2 = sum_even_integers(["hello", 3, 10, 6, "bye", 5, 7.33, 5, 10])
    total3 = sum_even_integers([3, 9, 10, 99, 101, 5, 6, 5, 5, 10])

    print("Returned, expected:", total1, 26)
    print("Returned, expected:", total2, 26)
    print("Returned, expected:", total3, 26)


def run_test_sum_items_at_even_indices():
    """ Tests the   sum_items_at_even_indices   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   sum_items_at_even_indices   function:")
    print("--------------------------------------------------")

    total1 = sum_items_at_even_indices([3, 10, 6, 5, 5, 10])
    total2 = sum_items_at_even_indices([5.5, 10, 3, 2, 10, 0, 1])

    print("Returned, expected:", total1, 14)
    print("Returned, expected:", total2, 19.5)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
