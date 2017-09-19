"""
This module shows how to ITERATE (i.e. loop) through a SEQUENCE:
  -- list
  -- string
  -- tuple

It shows two ways to do so:
  -- using RANGE
  -- using just IN (no RANGE)

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         and their colleagues.
"""

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_abs_of_all()
    run_test_sum_abs_of_all_without_range()
    run_test_fill_from_colors()
    run_test_print_letters()

# ----------------------------------------------------------------------
# The TEST functions are further down in the file,
# so that you can focus on the following examples.
# ----------------------------------------------------------------------


def sum_abs_of_all(sequence):
    """
    What comes in:
      -- A sequence of numbers.
    What goes out:
      Returns the sum of the absolute values of the numbers.
    Side effects:   None.
    Examples:
      sum_all([5, -1, 10, 4, -33])
         would return 5 + 1 + 10 + 4 + 33, which is 53

      sum_all([10, -30, -20])  would return 10 + 30 + 20, which is 60
    Type hints:
      :type sequence: list or tuple (of numbers)
    """
    # ------------------------------------------------------------------
    # EXAMPLE 1.  Iterates through a sequence of numbers, summing them.
    # ------------------------------------------------------------------
    total = 0
    for k in range(len(sequence)):
        total = total + abs(sequence[k])

    return total


def sum_abs_of_all_without_range(sequence):
    """
    Same specification as  sum_abs_of_all  above,
    but with a different implementation.
    """
    # ------------------------------------------------------------------
    # EXAMPLE 2.  Iterates through a sequence of numbers, summing them.
    #   Same as Example 1 above, but uses the "no range" form.
    # ------------------------------------------------------------------
    total = 0
    for number in sequence:
        total = total + abs(number)

    return total

    # ------------------------------------------------------------------
    # The above example shows how you can iterate through a sequence
    # WITHOUT using a RANGE expression.  This works ONLY
    #   ** IF you do NOT need the index variable. **
    #
    # You can ALWAYS use the form in Example 1 that uses RANGE;
    # this form in Example 2 is just "syntactic sugar."
    # Use this form if you like, but:
    #   -- Don't let it keep you from understanding the critical
    #        concept of an INDEX.
    #   -- Be aware of the limitation of this form.
    #   -- Don't confuse the two forms!
    # ------------------------------------------------------------------


def fill_from_colors(window, graphics_object, colors):
    """
    What comes in:
      -- An rg.RoseWindow
      -- A rosegraphics object that can be attached to a RoseWindow
         and has a fill color (e.g. an rg.Circle or rg.Rectangle)
      -- A sequence of rosegraphics colors.
    What goes out: Nothing (i.e., None).
    Side effects: 
      -- Attaches the given graphics object to the given RoseWindow.
      -- Then iterates through the given sequence of colors, using
           those colors to set the given graphics object's fill color.
      -- At each iteration, renders the window with a brief pause
           after doing so, to create a "flashing" display.    
    Type hints:
      :type window: rg.RoseWindow
      :type graphics_object: rg._Shape
      :type colors: list or tuple str
    """
    # ------------------------------------------------------------------
    # EXAMPLE 3.  Iterates through a sequence of colors.
    # ------------------------------------------------------------------
    graphics_object.attach_to(window)

    for k in range(len(colors)):
        graphics_object.fill_color = colors[k]
        window.render(0.5)


def print_letters(string):
    """
    Prints the characters in the given string, one character per line.
    """
    # ------------------------------------------------------------------
    # EXAMPLE 4.  Iterates through a STRING.
    # ------------------------------------------------------------------
    for k in range(len(string)):
        print(string[k])

# ----------------------------------------------------------------------
# Just TEST functions below here.
# ----------------------------------------------------------------------


def run_test_sum_abs_of_all():
    """ Tests the   sum_abs_of_all   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_abs_of_all   function:')
    print('--------------------------------------------------')

    total1 = sum_abs_of_all([8, 13, 7, 5])
    print('Returned, expected:', total1, 33)

    total2 = sum_abs_of_all([10, -30, -20])
    print('Returned, expected:', total2, 60)

    total3 = sum_abs_of_all([])
    print('Returned, expected:', total3, 0)


def run_test_sum_abs_of_all_without_range():
    """ Tests the   sum_abs_of_all_without_range   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_abs_of_all_without_range   function:')
    print('--------------------------------------------------')

    total1 = sum_abs_of_all_without_range([8, 13, 7, 5])
    print('Returned, expected:', total1, 33)

    total2 = sum_abs_of_all_without_range([10, -30, -20])
    print('Returned, expected:', total2, 60)

    total3 = sum_abs_of_all_without_range([])
    print('Returned, expected:', total3, 0)


def run_test_fill_from_colors():
    """ Tests the   fill_from_colors   function. """
    print('--------------------------------------------------')
    print('Testing the   fill_from_colors   function:')
    print('See the two graphics windows that pop up.')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # Test 1: Flashes red, white, blue -- 5 times.
    # ------------------------------------------------------------------
    title = 'Red, white and blue, repeated 5 times!'
    window = rg.RoseWindow(400, 180, title, canvas_color='dark gray')

    circle = rg.Circle(rg.Point(150, 100), 40)
    circle.attach_to(window.initial_canvas)

    number_of_cycles = 5
    window.continue_on_mouse_click('Click anywhere in here to start')

    for _ in range(number_of_cycles):
        fill_from_colors(window, circle, ['red', 'white', 'blue'])

    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # Test 2: Flashes through a bunch of colors, looping through the
    # list forwards in a rectangle, then backwards in an ellipse.
    # ------------------------------------------------------------------
    colors = ['red', 'white', 'blue', 'chartreuse', 'chocolate',
              'DodgerBlue', 'LightPink', 'maroon', 'yellow', 'green',
              'SteelBlue', 'black']

    title = 'Loop through 12 colors, forwards then backwards!'
    window = rg.RoseWindow(450, 250, title, canvas_color='yellow')

    rect_width = 100
    rect_height = 40
    rect_center = rg.Point(125, 100)
    rectangle = rg.Rectangle(rg.Point(rect_center.x - (rect_width / 2),
                                      rect_center.y - (rect_height / 2)),
                             rg.Point(rect_center.x + (rect_width / 2),
                                      rect_center.y + (rect_height / 2)))

    oval_width = 70
    oval_height = 160
    oval_center = rg.Point(300, 100)
    ellipse = rg.Ellipse(rg.Point(oval_center.x - (oval_width / 2),
                                  oval_center.y - (oval_height / 2)),
                         rg.Point(oval_center.x + (oval_width / 2),
                                  oval_center.y + (oval_height / 2)))

    rectangle.attach_to(window)
    ellipse.attach_to(window)
    window.render()
    window.continue_on_mouse_click('Click anywhere in here to start')

    # This function call iterates through the colors,
    # filling the rectangle with those colors:
    fill_from_colors(window, rectangle, colors)

    # The  reverse  method reverses its list IN PLACE
    # (i.e., it "mutates" its list -- more on that in future sessions).
    colors.reverse()

    window.continue_on_mouse_click()

    # This function call iterates through the colors,
    # filling the ellipse (oval) with those colors:
    fill_from_colors(window, ellipse, colors)

    window.close_on_mouse_click()


def run_test_print_letters():
    """ Tests the   print_letters   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   print_letters   function:')
    print('--------------------------------------------------')

    print()
    print('Test 1: Print the letters in "Eric Clapton"')
    print_letters('Eric Clapton')

    print()
    print('Test 2: Print the letters in "Layla"')
    print_letters('Layla')


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
