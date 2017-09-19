"""
This module demonstrates INDEXING into a SEQUENCE:
  -- How to index into a sequence, using square brackets []
  -- The 'len' function
  -- What goes wrong if the index is out of range

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         and their colleagues.  September 2015.
"""
# ----------------------------------------------------------------------
# Students: Read and run this program.  There is nothing else
#           for you to do in here.  Just use it as an example.
#           Before you leave this example,
#   *** MAKE SURE YOU UNDERSTAND, FOR EACH OF LISTS, STRINGS and TUPLES:
#   ***  -- THEIR NOTATIONS
#   ***   -- HOW THEY ARE DIFFERENT (other than notation)
#   ***   -- HOW TO REFERENCE THEIR ITEMS (ELEMENTS), with INDEXING
#
#   *** WHEN YOU RUN, you WILL get an ERROR MESSAGE.
#   *** SEE THE CODE BELOW for what to do about that.
# ----------------------------------------------------------------------

import rosegraphics as rg
import time


def main():
    """ Demonstrates indexing. """

    # ------------------------------------------------------------------
    # The following are SEQUENCES:
    #   -- LISTs are in square brackets
    #         and can contain anything
    #   -- STRINGs are in quotes (single or double, your choice)
    #         and must contain only characters
    #   -- TUPLEs are in parentheses
    #         and are otherwise just like lists except that lists
    #         are mutable and tuples are immutable (more on this later)
    # ------------------------------------------------------------------
    my_list = ['dog', 49, 30.5, 50000000, rg.Point(90, 25)]  # List
    my_string = 'Yo! Whazup?'  # String
    my_tuple = ('This', 'is a', 55, 1004, 'tuple')  # Tuple

    # ------------------------------------------------------------------
    # Each of the following three function calls
    # results in a (purposeful) run-time ERROR.  So:
    #   1. Run the program.  See the error that results.
    #   2. Then comment out the function call that ran.
    #   3. Repeat steps 1 and 2 until all three function calls have run.
    # ------------------------------------------------------------------
    examples_of_indexing(my_list)
    examples_of_indexing(my_string)
    examples_of_indexing(my_tuple)


def examples_of_indexing(sequence):
    """ Examples of indexing on the given sequence. """

    # ------------------------------------------------------------------
    # The   len   function returns the length of a sequence.
    # ------------------------------------------------------------------
    length = len(sequence)
    print('\nLength is', length)

    # ------------------------------------------------------------------
    # Refer to specific items in the sequence
    # by using the square bracket notation blah[...],
    # with the INDEX placed inside the square brackets.
    # The numbering for indices starts at ZERO (not at one).
    # ------------------------------------------------------------------
    print('\nAt indices 0, 1 and 4:')
    print(sequence[0])
    print(sequence[1])
    print(sequence[4])

    # ------------------------------------------------------------------
    # Use the square bracket notation in a loop to iterate through
    # the entire sequence.  Note how the index variable  k  is used.
    # ------------------------------------------------------------------
    print('\nList them all:')
    for k in range(len(sequence)):
        print(sequence[k], end=' ')  # end=' ' for SPACE after print
    print()

    # ------------------------------------------------------------------
    # This language allows negative indices.  Most languages do NOT.
    # ------------------------------------------------------------------
    print('\nCool stuff:')
    print(sequence[-1])  # Cool! Look up 'slicing' for even cooler stuff

    # ------------------------------------------------------------------
    # Since indexing starts at ZERO, the index of the last item is the
    # length of the sequence MINUS ONE.  Attempts to index past the end
    # of a sequence results in a run-time error 'index out of range'.
    # ------------------------------------------------------------------
    print('\nLast item, then one past the last item (causes an error):')
    length = len(sequence)
    print(sequence[length - 1])  # Last item in the sequence.

    # The following  sleep  gives enough time for the above  print
    # statements to appear on the console before the error message does.
    time.sleep(1)

    print(sequence[length])  # Oops!  Generates an error.

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
