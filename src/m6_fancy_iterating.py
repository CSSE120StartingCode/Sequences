"""
This module practices ITERATING (i.e. looping) through a SEQUENCE
in ways OTHER than just going thru the sequence from BEGINNING to END.

It also shows how to SELECT items in a sequence, e.g.:
  -- the items that are strings
  -- the items that are even integers (e.g. 2, 4, 6, ...)
  -- the items in the second half of the sequence

Note that:
  -- SELECTING items that ARE even integers
is different from:
  -- LOOKING only at items AT even-numbered indices.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    # -------------------------------------------------------------------------
    # TODO: 2.  EXAMINE the  4  sequences immediately below
    #   this comment, and READ the instructions that follows them.
    #  ___
    #  When you have examined the 4 sequences below and understand how
    #  the testing will work for this module, asking questions as needed,
    #  THEN:
    #     change the above _TODO_ to DONE.
    # -------------------------------------------------------------------------
    sequence1 = [55, "hello", 33, rg.Point(90, 25)]  # List
    sequence2 = [90, "dog", 87, "cat", "bone", 33, 100]  # List
    sequence3 = "Yo! Whazup?"  # String
    sequence4 = ("This", "is a", "tuple", 55)  # Tuple

    # -------------------------------------------------------------------------
    # STUDENTS: Do the work in this module as follows.
    #   Otherwise, you will be overwhelmed by the output.
    #
    #   For each function that you implement (TODOs 3 - 9):
    #     1. Locate the statements just below this comment
    #          that call TEST functions.
    #     2. UN-comment only one test at a time.
    #     3. Implement that function per its _TODO_.
    #     4. When satisfied with your work, move onto the next test,
    #        RE-commenting out the previous test if you wish.
    # -------------------------------------------------------------------------

    run_test_print_all_items_forwards(sequence1, sequence2, sequence3,
                                      sequence4)
    # run_test_print_all_items_backwards(sequence1, sequence2, sequence3,
    #                                    sequence4)
    # run_test_print_items_at_odd_indices(sequence1, sequence2, sequence3,
    #                                     sequence4)
    # run_test_print_items_in_second_half(sequence1, sequence2, sequence3,
    #                                     sequence4)
    # run_test_print_items_that_are_bigger_than_5()  # Uses different sequences
    # run_test_print_items_that_are_strings(sequence1, sequence2, sequence3,
    #                                       sequence4)
    # run_test_print_items_that_are_odd_integers(sequence1, sequence2,
    #                                            sequence3, sequence4)


def run_test_print_all_items_forwards(sequence1, sequence2, sequence3,
                                      sequence4):
    """ Tests the   print_all_items_forwards   function. """
    print()
    print("***********************************************************")
    print("Testing the   print_all_items_forwards   function.")
    print("Iterate through an ENTIRE sequence, forwards:")
    print("***********************************************************")

    print("Expected:")
    print("55\nhello\n33\nPoint(90.0, 25.0)\n")
    print("Actual:  ")
    print_all_items_forwards(sequence1)

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("90\ndog\n87\ncat\nbone\n33\n100\n")
    print("Actual:  ")
    print_all_items_forwards(sequence2)

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("Y\no\n!\n \nW\nh\na\nz\nu\np\n?\n")
    print("Actual:  ")
    print_all_items_forwards(sequence3)

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("This\nis a\ntuple\n55\n")
    print("Actual:  ")
    print_all_items_forwards(sequence4)


def run_test_print_all_items_backwards(sequence1, sequence2, sequence3,
                                       sequence4):
    """ Tests the   print_all_items_backwards   function. """
    print()
    print("***********************************************************")
    print("Testing the   print_all_items_backwards   function.")
    print("Iterate through an ENTIRE sequence, backwards:")
    print("***********************************************************")

    print("Expected:")
    print("Point(90.0, 25.0)\n33\nhello\n55\n")
    print("Actual:  ")
    print_all_items_backwards(sequence1)

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("100\n33\nbone\ncat\n87\ndog\n90\n")
    print("Actual:  ")
    print_all_items_backwards(sequence2)

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("?\np\nu\nz\na\nh\nW\n \n!\no\nY\n")
    print("Actual:  ")
    print_all_items_backwards(sequence3)

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("55\ntuple\nis a\nThis\n")
    print("Actual:  ")
    print_all_items_backwards(sequence4)


def run_test_print_items_at_odd_indices(sequence1, sequence2, sequence3,
                                        sequence4):
    print()
    print("***********************************************************")
    print("Testing the   print_items_at_odd_indices   function.")
    print("Iterate through PART of a sequence, namely,")
    print("the items at odd-numbered indices:")
    print("***********************************************************")

    print("Expected:")
    print("hello is at index 1")
    print("Point(90.0, 25.0) is at index 3\n")
    print("Actual:  ")
    print_items_at_odd_indices(sequence1)

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("dog is at index 1")
    print("cat is at index 3")
    print("33 is at index 5\n")
    print("Actual:  ")
    print_items_at_odd_indices(sequence2)

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("o is at index 1")
    print("  is at index 3")
    print("h is at index 5")
    print("z is at index 7")
    print("p is at index 9\n")
    print("Actual:  ")
    print_items_at_odd_indices(sequence3)

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("is a is at index 1")
    print("55 is at index 3\n")
    print("Actual:  ")
    print_items_at_odd_indices(sequence4)


def run_test_print_items_in_second_half(sequence1, sequence2, sequence3,
                                        sequence4):
    print()
    print("***********************************************************")
    print("Testing the   print_items_in_second_half   function.")
    print("Iterate through PART of a sequence, namely,")
    print("the items in the second half of the sequence:")
    print("***********************************************************")

    print("Expected:")
    print("33\nPoint(90.0, 25.0)\n")
    print("Actual:  ")
    print_items_in_second_half(sequence1)

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("cat\nbone\n33\n100\n")
    print("Actual:  ")
    print_items_in_second_half(sequence2)

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("h\na\nz\nu\np\n?\n")
    print("Actual:  ")
    print_items_in_second_half(sequence3)

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("tuple\n55\n")
    print("Actual:  ")
    print_items_in_second_half(sequence4)


def run_test_print_items_that_are_bigger_than_5():
    # Note:  The tests of this function use sequences that are DIFFERENT
    #        than the tests of the other functions.
    print()
    print("***********************************************************")
    print("Testing the  print_items_that_are_bigger_than_5  function.")
    print("Iterate through a sequence, selecting items, namely,")
    print("the items that are bigger than 5:")
    print("Note that the test sequences for this are NOT the same as")
    print("the test sequences for the other exercises herein.")
    print("***********************************************************")

    print("Expected:")
    print("45 is at index 0")
    print("6 is at index 3")
    print("100 is at index 6")
    print("100 is at index 7\n")
    print("Actual:  ")
    print_items_that_are_bigger_than_5([45, 3, -50, 6, 5, 3, 100, 100])

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("7 is at index 0")
    print("30 is at index 1")
    print("6 is at index 2\n")
    print("Actual:  ")
    print_items_that_are_bigger_than_5([7, 30, 6])

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("")
    print("Actual:  ")
    print_items_that_are_bigger_than_5([5, 5, 5])


def run_test_print_items_that_are_strings(sequence1, sequence2, sequence3,
                                          sequence4):
    print()
    print("***********************************************************")
    print("Testing the   print_items_that_are_strings   function.")
    print("Iterate through a sequence, selecting items, namely,")
    print("the items that are strings:")
    print("***********************************************************")

    print("Expected:")
    print("hello is at index 1\n")
    print("Actual:  ")
    print_items_that_are_strings(sequence1)

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("dog is at index 1")
    print("cat is at index 3")
    print("bone is at index 4\n")
    print("Actual:  ")
    print_items_that_are_strings(sequence2)

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("Y is at index 0")
    print("o is at index 1")
    print("! is at index 2")
    print("  is at index 3")
    print("W is at index 4")
    print("h is at index 5")
    print("a is at index 6")
    print("z is at index 7")
    print("u is at index 8")
    print("p is at index 9")
    print("? is at index 10\n")
    print("Actual:  ")
    print_items_that_are_strings(sequence3)

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("This is at index 0")
    print("is a is at index 1")
    print("tuple is at index 2\n")
    print("Actual:  ")
    print_items_that_are_strings(sequence4)


def run_test_print_items_that_are_odd_integers(sequence1, sequence2, sequence3,
                                               sequence4):
    print()
    print("***********************************************************")
    print("Testing the   print_items_that_are_odd_integers   function.")
    print("Iterate through a sequence, selecting items, namely,")
    print("the items that are odd integers:")
    print("Note that there is 1 extra test sequence for this problem.")
    print("***********************************************************")

    print("Expected:")
    print("55 is at index 0")
    print("33 is at index 2\n")
    print("Actual:  ")
    print_items_that_are_odd_integers(sequence1)

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("87 is at index 2")
    print("33 is at index 5\n")
    print("Actual:  ")
    print_items_that_are_odd_integers(sequence2)

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("")
    print("Actual:  ")
    print_items_that_are_odd_integers(sequence3)

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("55 is at index 3\n")
    print("Actual:  ")
    print_items_that_are_odd_integers(sequence4)

    print()
    print("-------------------------------------------------------")
    print("Expected:")
    print("87 is at index 2")
    print("95 is at index 3")
    print("5 is at index 6")
    print("77 is at index 7\n")
    print("Actual:  ")
    print_items_that_are_odd_integers([90, "dog", 87, 95, 8, 10, 5, 77])


###############################################################################
# Iterating through the ENTIRE sequence, FORWARDs.
###############################################################################
def print_all_items_forwards(sequence):
    """
    Prints the items in the given sequence in the order that
    they appear, that is, forwards.  Prints them one item per line.

    For example, if the sequence is [55, "hello", 33, rg.Point(90, 25)],
    then this function prints:
       55
       hello
       33
       Point at (90, 25)
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


###############################################################################
# Iterating through the ENTIRE sequence, BACKWARDs.
###############################################################################
def print_all_items_backwards(sequence):
    """
    Prints the items in the given sequence in the REVERSE of the order
    in which they appear, that is, prints them in backwards order.
    Prints them one item per line.

    For example, if the sequence is [55, "hello", 33, rg.Point(90, 25)],
    then this function prints:
       Point at (90,25)
       33
       hello
       55
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


###############################################################################
# Iterating through PART of a sequence:
#   -- in this sample problem, every other item in the sequence.
###############################################################################
def print_items_at_odd_indices(sequence):
    """
    Prints the items at the odd-numbered indices in the given sequence,
    along with their positions (indices) in the sequence.
    with " is at index " in between (see example).

    For example, if the sequence is [90, "dog", 87, 95, 92, 33, 100],
    then this function prints:
      dog is at index 1
      95 is at index 3
      33 is at index 5
    """
    # -------------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


###############################################################################
# Iterating through PART of a sequence:
#   -- in this sample problem, the second half.
###############################################################################
def print_items_in_second_half(sequence):
    """
    Prints the items in the second half of the given sequence.
    For odd-length sequences, includes the middle item in the sequence.

    For example, if the sequence is [90, "dog", 87, 95, 92, 33, 100],
    then this function prints:
      95
      92
      33
      100
    """
    # -------------------------------------------------------------------------
    # TODO: 6. Implement and test this function.
    #          Tests have been written for you (above).
    #  ___
    #  IMPORTANT: Don't get hung up on dealing with the middle item
    #    being included or not.  Just try to solve the problem and adjust
    #    if needed.  No conditional is needed under most implementations.
    #  ___
    #  IMPORTANT: RANGE expressions need INTEGERS.
    #    Use   //   for integer division.
    # -------------------------------------------------------------------------


###############################################################################
# Iterating through a sequence, selecting items:
#   -- in this sample problem, the items that are bigger than 5.
###############################################################################
def print_items_that_are_bigger_than_5(sequence):
    """
    Prints the items in the given sequence that are bigger than 5,
    along with their positions (indices) in the sequence,
    with " is at index " in between (see example).

    For example, if the sequence is [45, 3, -50, 6, 5, 3, 100, 100],
    then this function prints:
      45 is at index 0
      6 is at index 3
      100 is at index 6
      100 is at index 7

    Precondition: All the items in the sequence are integers.
    """
    # -------------------------------------------------------------------------
    # TODO: 7. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


###############################################################################
# Iterating through a sequence, selecting items:
#   -- in this sample problem, the items that are strings.
###############################################################################
def print_items_that_are_strings(sequence):
    """
    Prints the items in the given sequence that are strings,
    along with their positions (indices) in the sequence,
    with " is at index " in between (see example).

    For example, if the sequence is [90, "dog", 87, "cat", "bone", 33, 100],
    then this function prints:
      dog is at index 1
      cat is at index 3
      bone is at index 4
    """
    # -------------------------------------------------------------------------
    # TODO: 8. Implement and test this function.
    #  ___
    #  IMPORTANT:
    #    -- A string is, by definition, an object whose type is   str.
    #    -- The   type   function gives the type of an object.
    #         For example,   type("hello")   returns   str.  So:
    #             if type("hello") is str:
    #                 ...
    #         would be how you would test whether "hello" is a string.
    #  ___
    #        Note that   str   has NO quotes surrounding it.
    # -------------------------------------------------------------------------


###############################################################################
# Iterating through a sequence, selecting items:
#   -- in this sample problem, the items that are odd integers.
###############################################################################
def print_items_that_are_odd_integers(sequence):
    """
    Prints the items in the given sequence that are odd integers,
    along with their positions in the sequence,
    with " is at index " in between (see example).

    For example, if the sequence is
         [90, "dog", 87, "cat", "bone", 33, 100],
    then this function prints:
      87 is at index 2
      33 is at index 5
    """
    # -------------------------------------------------------------------------
    # TODO: 9. Implement and test this function.
    #  ___
    #  IMPORTANT:  The  type  function returns  int  if its argument
    #    is an integer.  Note that   int   has NO quotes surrounding it.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
