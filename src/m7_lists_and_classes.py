"""
This module lets you practice
  -- IMPLEMENTING CLASSES and 
  -- the ITERATE-THROUGH-A-SEQUENCE pattern.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math
import time
from typing import List

import testing_helper


# -----------------------------------------------------------------------------
# TODO: 2. Watch the VIDEO for this module listed in the Follow-Me section
#  of the Preparation for this session.  It introduces the ConceptMap class
#  that you will implement in this module.
#    After you have watched that video, mark this _TODO_ as DONE.
# -----------------------------------------------------------------------------

###############################################################################
# The Point and Circle classes are already implemented.
###############################################################################
class Point:
    """ A Point in 2-space, with x and y-coordinates. """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        """
        Returns a new Point with the same x and y-coordinates as this Point. """
        return Point(self.x, self.y)

    def distance_from(self, another_point):
        """
        Returns the distance this Point is from the given Point.
          :type another_point: Point
          :rtype float
        """
        delta_x = self.x - another_point.x
        delta_y = self.y - another_point.y
        return math.sqrt((delta_x * delta_x) + (delta_y * delta_y))


class Circle:
    """ A circle with center and radius. """

    def __init__(self, center, radius):
        """
        Stores the given radius and a clone of the given center.
        Type hints:
          :type center: Point
          :type radius: float
        """
        self.center = center.clone()
        self.radius = radius


###############################################################################
# You implement the ConceptMap class.
###############################################################################
class ConceptMap:
    """
    This is the beginning of a class that might eventually model Concept Maps.
    Currently it contains only a sequence of Circle objects
    (that might eventually be augmented to model Concepts).
      ** This is an ARTIFICIAL example that exists solely to give you practice
      ** at implementing classes AND iterating through sequences.
    """

    def __init__(self, circles):
        """
        Stores the given sequence of Circle objects.
          :type circles: List[Circle]
        """
        self.circles = circles  # type: List[Circle]

    def sum_of_x_coordinates(self):
        """
        Examines each of the Circle objects that this ConceptMap has.
        Returns the sum of the x-coordinates of the centers of those Circles.
        For example:
            circles1 = [Circle(Point(11, 12), 10),
                        Circle(Point(14, 13), 8),
                        Circle(Point(10, 20), 5),
                        Circle(Point(30, 15), 12),
                        Circle(Point(50, 35), 33)]
            concept_map1 = ConceptMap(circles1)

            concept_map1.sum_of_x_coordinates()
               returns  11 + 14 + 10 + 30 + 50, which is 115.
        """
        # ---------------------------------------------------------------------
        # TODO: 3. Follow along with the video to implement and test this
        #   method.  Tests have been written for you (below) and include
        #   the example in the above doc-string.
        # ---------------------------------------------------------------------

    def number_of_small_circles(self, threshold):
        """
        Examines each of the Circle objects that this ConceptMap has.
        Returns the number of those Circle objects
        whose radius is less than the given threshold.
        For example:
            circles1 = [Circle(Point(11, 12), 10),
                        Circle(Point(14, 15), 8),
                        Circle(Point(10, 20), 5),
                        Circle(Point(30, 15), 12),
                        Circle(Point(50, 35), 33)]
            concept_map1 = ConceptMap(circles1)

            concept_map1.number_of_small_circles(15)  returns  4
            concept_map1.number_of_small_circles(10)  returns  2
            concept_map1.number_of_small_circles(80)  returns  5
            concept_map1.number_of_small_circles(4)   returns  0
        """
        # ---------------------------------------------------------------------
        # TODO: 4. Implement and test this method.  Tests have been written
        #   for you (below) and include the example in the above doc-string.
        # ---------------------------------------------------------------------

    def product_of_sums_of_x_and_y_coordinates(self):
        """
        Examines each of the Circle objects that this ConceptMap has.
        Computes, for each of those Circle objects,
        the sum of the x and y-coordinates of its center.
        Returns the product of those sums.
        For example:
            circles1 = [Circle(Point(11, 12), 10),
                        Circle(Point(14, 13), 8),
                        Circle(Point(10, 20), 5),
                        Circle(Point(30, 15), 12),
                        Circle(Point(50, 35), 33)]
            concept_map1 = ConceptMap(circles1)

            concept_map1.product_of_sums_of_x_and_y_coordinates()
               returns
                 (11 + 12) * (14 + 13) * (10 + 20) * (30 + 15) * (50 + 35),
               that is,
                    23 * 27 * 30 * 45 * 85,
               which is 71259750.
        """
        # ---------------------------------------------------------------------
        # TODO: 5. Implement and test this method.  Tests have been written
        #   for you (below) and include the example in the above doc-string.
        # ---------------------------------------------------------------------

    def sum_of_some_indices(self):
        """
        Examines each of the Circle objects that this ConceptMap has.
        Returns the sum of the INDICES of those Circle objects
        whose center has x-coordinate bigger than its y-coordinate.
        For example:
            circles1 = [Circle(Point(11, 12), 10),
                        Circle(Point(14, 13), 8),
                        Circle(Point(10, 20), 5),
                        Circle(Point(30, 15), 12),
                        Circle(Point(50, 35), 33)]
            concept_map1 = ConceptMap(circles1)

            concept_map1.sum_of_some_indices()
               returns  1 + 3 + 4,   which is 8
        """
        # ---------------------------------------------------------------------
        # TODO: 6. Follow along with the video to implement and test this
        #   method.  Tests have been written for you (below) and include
        #   the example in the above doc-string.
        # ---------------------------------------------------------------------

    def product_of_some_radii(self):
        """
        Examines the Circle objects that this ConceptMap has,
        but looking only at those at odd-numbered indices (1, 3, 5, ...)
        Returns the product of the radii of those Circles.
        For example:
            circles1 = [Circle(Point(11, 12), 10),
                        Circle(Point(14, 13), 8),
                        Circle(Point(10, 20), 5),
                        Circle(Point(30, 15), 12),
                        Circle(Point(50, 35), 33)]
            concept_map1 = ConceptMap(circles1)

            concept_map1.product_of_some_radii()
               returns  8 * 12, which is 96
        """
        # ---------------------------------------------------------------------
        # TODO: 7. Implement and test this method.  Tests have been written
        #   for you (below) and include the example in the above doc-string.
        # ---------------------------------------------------------------------

    def sum_of_distances(self, point):
        """
        Examines the Circle objects that this ConceptMap has.
        For each such Circle object, examines its center and computes
        the distance that that center is from the given point
            [USE THE Point distance_from METHOD TO DO SO!].
        Adds up all those distances, and returns the resulting sum.
        For example:
            circles1 = [Circle(Point(11, 12), 10),
                        Circle(Point(14, 13), 8),
                        Circle(Point(10, 20), 5),
                        Circle(Point(30, 15), 12),
                        Circle(Point(50, 35), 33)]
            concept_map1 = ConceptMap(circles1)

            concept_map1.sum_of_distances(Point(14, 12))
               returns
              [    distance from (11, 12) to (14, 12)
                +  distance from (14, 13) to (14, 12)
                +  distance from (10, 20) to (14, 12)
                +  distance from (30, 15) to (14, 12)
                +  distance from (50, 35) to (14, 12)]
               which is (approximately)
              [ 3  +  1  +  8.94  +  16.28  +  42.72], which is about 71.943111.
        """
        # ---------------------------------------------------------------------
        # TODO: 8. Implement and test this method.  Tests have been written
        #   for you (below) and include the example in the above doc-string.
        # ---------------------------------------------------------------------


###############################################################################
# Code for TESTING is below here.
###############################################################################
def main():
    """
    Tests the methods of the ConceptMap class defined above.
    Each test uses the same two ConceptMap examples as test cases.
    """
    circles1 = [Circle(Point(11, 12), 10),
                Circle(Point(14, 13), 8),
                Circle(Point(10, 20), 5),
                Circle(Point(30, 15), 12),
                Circle(Point(50, 35), 33)]
    concept_map1 = ConceptMap(circles1)

    circles2 = [Circle(Point(30, 20), 10),
                Circle(Point(100, 200), 40),
                Circle(Point(22, 10), 5)]
    concept_map2 = ConceptMap(circles2)

    print()
    print("The TESTS all use the same two ConceptMap examples as test cases:")
    testing_helper.print_colored("""
    circles1 = [Circle(Point(11, 12), 10),
                Circle(Point(14, 13), 8),
                Circle(Point(10, 20), 5),
                Circle(Point(30, 15), 12),
                Circle(Point(50, 35), 33)]
    concept_map1 = ConceptMap(circles1)

    circles2 = [Circle(Point(30, 20), 10),
                Circle(Point(100, 200), 40),
                Circle(Point(22, 10), 5)]
    concept_map2 = ConceptMap(circles2)
    """, color="blue")

    run_test_sum_of_x_coordinates(concept_map1, concept_map2)
    run_test_number_of_small_circles(concept_map1, concept_map2)
    run_test_product_of_sums_of_x_and_y_coordinates(concept_map1, concept_map2)
    run_test_sum_of_some_indices(concept_map1, concept_map2)
    run_test_product_of_some_radii(concept_map1, concept_map2)
    run_test_sum_of_distances(concept_map1, concept_map2)


def run_test_sum_of_x_coordinates(concept_map1, concept_map2):
    """
    What comes in: two ConceptMap objects.
    Side effects:  Tests the   sum_of_x_coordinates   method twice:
      once using the given concept_map1 and then using the given concept_map2.
    """
    print()
    print("--------------------------------------------------")
    print("Testing the  sum_of_x_coordinates   method:")
    print("--------------------------------------------------")

    # Test using concept_map1:
    expected = 115
    actual = concept_map1.sum_of_x_coordinates()
    print("Expected:", expected)
    print("Actual:  ", actual)
    if actual != expected:
        testing_helper.print_colored("FAILED the above test", color="red")

    # Test using concept_map2:
    expected = 152
    actual = concept_map2.sum_of_x_coordinates()
    print("Expected:", expected)
    print("Actual:  ", actual)
    if actual != expected:
        testing_helper.print_colored("FAILED the above test", color="red")


def run_test_number_of_small_circles(concept_map1, concept_map2):
    """
    What comes in: two ConceptMap objects.
    Side effects:  Tests the   number_of_small_circles   method twice:
      once using the given concept_map1 and then using the given concept_map2.
    """
    print()
    print("--------------------------------------------------")
    print("Testing the  number_of_small_circles   method:")
    print("--------------------------------------------------")

    # Test using concept_map1:
    expected = 4
    actual = concept_map1.number_of_small_circles(15)
    print("Expected:", expected)
    print("Actual:  ", actual)
    if actual != expected:
        testing_helper.print_colored("FAILED the above test", color="red")

    # Test using concept_map2:
    expected = 0
    actual = concept_map2.number_of_small_circles(5)
    print("Expected:", expected)
    print("Actual:  ", actual)
    if actual != expected:
        testing_helper.print_colored("FAILED the above test", color="red")


def run_test_product_of_sums_of_x_and_y_coordinates(concept_map1, concept_map2):
    """
    What comes in: two ConceptMap objects.
    Side effects:  Tests the   product_of_sums_of_x_and_y_coordinates   method
      twice: once using the given concept_map1
      and then again using the given concept_map2.
    """
    print()
    print("--------------------------------------------------")
    print("Testing the method:")
    print("   product_of_sums_of_x_and_y_coordinates")
    print("--------------------------------------------------")

    # Test using concept_map1:
    expected = 71259750
    actual = concept_map1.product_of_sums_of_x_and_y_coordinates()
    print("Expected:", expected)
    print("Actual:  ", actual)
    if actual != expected:
        testing_helper.print_colored("FAILED the above test", color="red")

    # Test using concept_map2:
    expected = 480000
    actual = concept_map2.product_of_sums_of_x_and_y_coordinates()
    print("Expected:", expected)
    print("Actual:  ", actual)
    if actual != expected:
        testing_helper.print_colored("FAILED the above test", color="red")


def run_test_sum_of_some_indices(concept_map1, concept_map2):
    """
    What comes in: two ConceptMap objects.
    Side effects:  Tests the   sum_of_some_indices   method twice:
      once using the given concept_map1 and then using the given concept_map2.
    """
    print()
    print("--------------------------------------------------")
    print("Testing the  sum_of_some_indices   method:")
    print("--------------------------------------------------")

    # Test using concept_map1:
    expected = 8
    actual = concept_map1.sum_of_some_indices()
    print("Expected:", expected)
    print("Actual:  ", actual)
    if actual != expected:
        testing_helper.print_colored("FAILED the above test", color="red")

    # Test using concept_map2:
    expected = 2
    actual = concept_map2.sum_of_some_indices()
    print("Expected:", expected)
    print("Actual:  ", actual)
    if actual != expected:
        testing_helper.print_colored("FAILED the above test", color="red")


def run_test_product_of_some_radii(concept_map1, concept_map2):
    """
    What comes in: two ConceptMap objects.
    Side effects:  Tests the   product_of_some_radii   method twice:
      once using the given concept_map1 and then using the given concept_map2.
    """
    print()
    print("--------------------------------------------------")
    print("Testing the  product_of_some_radii   method:")
    print("--------------------------------------------------")

    # Test using concept_map1:
    expected = 96
    actual = concept_map1.product_of_some_radii()
    print("Expected:", expected)
    print("Actual:  ", actual)
    if actual != expected:
        testing_helper.print_colored("FAILED the above test", color="red")

    # Test using concept_map2:
    expected = 40
    actual = concept_map2.product_of_some_radii()
    print("Expected:", expected)
    print("Actual:  ", actual)
    if actual != expected:
        testing_helper.print_colored("FAILED the above test", color="red")


def run_test_sum_of_distances(concept_map1, concept_map2):
    """
    What comes in: two ConceptMap objects.
    Side effects:  Tests the   sum_of_distances   method twice:
      once using the given concept_map1 and then using the given concept_map2.
    """
    print()
    print("--------------------------------------------------")
    print("Testing the  sum_of_distances   method:")
    print("--------------------------------------------------")

    # Test using concept_map1:
    expected = 71.943111
    actual = concept_map1.sum_of_distances(Point(14, 12))
    print("Expected:", expected, "(approximately)")
    print("Actual:  ", actual)
    if actual is None or abs(actual - expected) > 0.00001:
        testing_helper.print_colored("FAILED the above test", color="red")

    # Test using concept_map2:
    expected = 398.519518
    actual = concept_map2.sum_of_distances(Point(100, 200))
    print("Expected:", expected, "(approximately)")
    print("Actual:  ", actual)
    if actual is None or abs(actual - expected) > 0.00001:
        testing_helper.print_colored("FAILED the above test", color="red")


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    testing_helper.print_colored("ERROR - While running this test,",
                                 color="red")
    testing_helper.print_colored("your code raised the following exception:",
                                 color="red")
    print()
    time.sleep(1)
    raise
