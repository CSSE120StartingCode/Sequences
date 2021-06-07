"""
This module lets you practice the ITERATE-THROUGH-A-SEQUENCE pattern
in its most classic form:
  -- Iterate all the way through the sequence, from beginning to end.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_count_negatives()
    run_test_count_short_ones()
    run_test_draw_circles()


def run_test_count_negatives():
    """ Tests the   count_negatives   function. """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement this TEST function.
    #   It TESTS the  count_negatives  function defined below.
    #   Include at least ** 2 ** ADDITIONAL tests beyond those we wrote.
    #   ___
    #   Use the same 4-step process as for previous TEST functions:
    #   ___
    #   Step 1: Read the doc-string (below) that provides the
    #     specification of the function you are to test.
    #     Understand what that function SHOULD return.
    #   ___
    #   Step 2:  Pick a test case:  numbers that you could send as
    #     actual arguments to the function.
    #   ___
    #   Step 3: Figure out (by hand, or by trusting a test case that
    #     your instructor provided) the CORRECT (EXPECTED) answer
    #     for your test case.
    #   ___
    #   Step 4: Write code that prints both the EXPECTED answer
    #     and the ACTUAL answer returned when you call the function.
    #     Follow the same form as in the test case we provided below.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   count_negatives   function:")
    print("--------------------------------------------------")

    # Test 1:
    expected = 1
    actual = count_negatives([8, 13, 7, -5])
    print()
    print("Test 1 expected:", expected)
    print("       actual:  ", actual)

    # Test 2:
    expected = 0
    actual = count_negatives([])
    print()
    print("Test 2 expected:", expected)
    print("       actual:  ", actual)

    # Test 3:
    expected = 0
    actual = count_negatives([3, 2.5, 3])
    print()
    print("Test 3 expected:", expected)
    print("       actual:  ", actual)

    # Test 4:
    expected = 4
    actual = count_negatives([-500, -500, -500, -0.0000001])
    print()
    print("Test 4 expected:", expected)
    print("       actual:  ", actual)

    # Test 5:
    expected = 1
    actual = count_negatives((8, 13, 7, -5))
    print()
    print("Test 5 expected:", expected)
    print("       actual:  ", actual)

    # -------------------------------------------------------------------------
    # TODO: 2 (continued):  Add your 2 ADDITIONAL tests here:
    # -------------------------------------------------------------------------


def count_negatives(seq):
    """
    What comes in:  An sequence of numbers.
    What goes out:  Returns the number of items in the given sequence
      that are negative.
    Side effects:   None.
    Examples:
      count_negatives([8, 13, 7, -5])  returns  1
      count_negatives([])  returns  0
      count_negatives([3, 2.5, 3])  returns  0
      count_negatives([-500, -500, -500, -0.0000001])  returns  4
      count_negatives((8, 13, 7, -5))  returns  1
    Type hints:
      :type seq: (list | tuple) of (int | float)
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # -------------------------------------------------------------------------


def run_test_count_short_ones():
    """ Tests the   count_short_ones   function. """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement this TEST function.
    #   It TESTS the  count_short_ones  function defined below.
    #   Include at least ** 2 ** ADDITIONAL tests beyond those we wrote.
    #  ___
    #  Use the same 4-step process as for previous TEST functions.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   count_short_ones   function:")
    print("--------------------------------------------------")

    # Test 1:
    expected = 5
    seq = [[3, 5],
           [3, 9, 0, 4],
           [5],
           [5],
           [],
           [9, 8, 7],
           [5, 6]]
    actual = count_short_ones(seq)
    print()
    print("Test 1 expected:", expected)
    print("       actual:  ", actual)

    # Test 2:
    expected = 3
    seq = ["all", "we", "need", "is", "peace", "", "short", "123"]
    actual = count_short_ones(seq)
    print()
    print("Test 2 expected:", expected)
    print("       actual:  ", actual)

    # Test 3:
    expected = 6
    seq = ["abc", "a", "", "foo", "de", "dd", "x", "foo", "argh", "a"]
    actual = count_short_ones(seq)
    print()
    print("Test 3 expected:", expected)
    print("       actual:  ", actual)

    # Test 4:
    expected = 0
    seq = []
    actual = count_short_ones(seq)
    print()
    print("Test 4 expected:", expected)
    print("       actual:  ", actual)

    # Test 5:
    expected = 1
    seq = [[]]
    actual = count_short_ones(seq)
    print()
    print("Test 5 expected:", expected)
    print("       actual:  ", actual)

    # Test 6:
    expected = 4
    seq = [[], [], [], []]
    actual = count_short_ones(seq)
    print()
    print("Test 6 expected:", expected)
    print("       actual:  ", actual)

    # Test 7:
    expected = 0
    seq = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    actual = count_short_ones(seq)
    print()
    print("Test 7 expected:", expected)
    print("       actual:  ", actual)

    # -------------------------------------------------------------------------
    # TODO: 4 (continued):  Add your 2 ADDITIONAL test(s) here:
    # -------------------------------------------------------------------------


def count_short_ones(seq_of_lists):
    """
    What comes in:  An sequence of sequences.
    What goes out:  Returns the number of sub-sequences in the given
      sequence whose length is less than 3.
    Side effects:   None.
    Examples:
      If the argument is:
         [ [3, 5],  [3, 9, 0, 4],  [5],  [5],  [],  [9, 8, 7],  [5, 6] ]
      then this function returns 5, since 5 of the 7 lists in the
      above sequence have length less than 3.

      If the argument is:
          ["all", "we", "need", "is", "peace", "", "short", "123"],
      then this function returns 3,
      since  "we"  and  "is"  and  ""  all have length less than 3.

    Type hints:
      :type seq_of_lists: (list | tuple) of (list | tuple | str)
    """
    # ------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # ------------------------------------------------------------------


def run_test_draw_circles():
    """ Tests the   draw_circles   function. """
    # -------------------------------------------------------------------------
    # We have supplied two tests for you, on a single window.
    # NO ADDITIONAL TESTS ARE REQUIRED, although you are welcome to
    # supply more tests if you choose.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   draw_circles   function:")
    print("See the window that pops up.")
    print("--------------------------------------------------")

    window = rg.RoseWindow(450, 350, "Points to Circles")

    points1 = [rg.Point(200, 100),
               rg.Point(100, 130),
               rg.Point(150, 200)]

    points2 = [rg.Point(50, 50),
               rg.Point(250, 250)]

    points3 = []
    for k in range(40):
        points3.append(rg.Point((10 * k) + 10, 10))

    draw_circles(window, points1, 15, "red")  # Test 1: 3 red circles
    message = "You should see 3 SMALL RED circles.\n"
    message += "Click to continue"
    window.continue_on_mouse_click(message)

    draw_circles(window, points2, 40, "blue")  # Test 2: 2 blue circles
    message = "Now you should see 3 small red circles\n"
    message += "** AND **  2 BIG BLUE ones.  Click to continue."
    window.continue_on_mouse_click(message)

    draw_circles(window, points3, 4, "purple")  # Test 3: 99 purple dots
    message = "Now you should see 3 small red and 2 big blue\n"
    message += "** AND **  40 TEENY PURPLE circles.  Click to exit."
    window.continue_on_mouse_click(message, close_it=True)

    # Test 4 on another window:
    window = rg.RoseWindow(250, 150, "More Points to Circles")

    points4 = [rg.Point(30, 50),
               rg.Point(80, 75),
               rg.Point(130, 25)]
    draw_circles(window, points4, 25, "yellow")
    window.close_on_mouse_click()


def draw_circles(window, points, radius, color):
    """
    What comes in:
      -- An rg.RoseWindow
      -- A sequence of rg.Point objects
      -- A positive number
      -- A string that can be used as a RoseGraphics color
    What goes out: Nothing (i.e., None).
    Side effects:
      See   draw_circles_picture.pdf   in this project for pictures
      that may help you better understand the following specification:

      For each point in the given sequence of rg.Points,
      constructs and draws an rg.Circle centered at that point,
      with the given radius and fill color, on the given rg.RoseWindow.

      Renders but does NOT close the given rg.RoseWindow.

    Type hints:
      :type window: rg.RoseWindow
      :type points: [rg.Point]
      :type radius: int | float
      :type color: str
    """
    # -------------------------------------------------------------------------
    # TODO: 6. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
