import unittest

from Ingredients import *
from Ingrediant_calculator import calculate_product, calculate_ingredients


class TestCalculatorsProduct(unittest.TestCase):
    def setUp(self):
        self.ingredient_set = [
            # Null value ingredients
            ({"Product": Ingredients(24, "Scones"),
              "Egg": Egg(252, "g"),
              "Milk": Wet(320, "ml"),
              "Oil": Wet(200, "ml")
              },

             {"Egg": Egg(5, "XL-egg"),
              "Milk": Wet(320, "ml"),
              "Oil": Wet(0, "ml")
              }),

            # Large value ingredients
            ({"Product": Ingredients(24, "Scones"),
              "Egg": Egg(252, "g"),
              "Milk": Wet(320, "ml"),
              "Oil": Wet(200, "ml")
              },

             {"Egg": Egg(20, "J-egg"),
              "Milk": Wet(600, "l"),
              "Oil": Wet(80000, "ml")
              }),

            # Small value ingredients
            ({"Product": Ingredients(24, "Scones"),
              "Egg": Egg(252, "g"),
              "Milk": Wet(320, "ml"),
              "Oil": Wet(200, "ml")
              },

             {"Egg": Egg(5, "XL-egg"),
              "Milk": Wet(32, "ml"),
              "Oil": Wet(600, "ml")
              }),

            # Long ingredients
            ({"Product": Ingredients(24, "Muffins"),
              "Egg": Egg(252, "g"),
              "Milk": Wet(320, "ml"),
              "Oil": Wet(200, "ml"),
              "Water": Wet(170, "ml"),
              "Sugar": Dry(250, "g")
              },

             {"Egg": Egg(5, "XL-egg"),
              "Milk": Wet(3200, "ml"),
              "Oil": Wet(6300, "ml"),
              "Water": Wet(70000, "ml"),
              "Sugar": Dry(250, "kg")
              }),

            # Short ingredients
            ({"Product": Ingredients(24, "Scones"),
              "Egg": Egg(252, "g"),
              "Milk": Wet(320, "ml"),
              },

             {"Egg": Egg(10, "L-egg"),
              "Milk": Wet(3500, "ml"),
              })
        ]

    def test_errors(self):
        """

        :Test: Testing if proper errors are raised
        """

        # Testing if error is raised for non relatable ingredients
        self.assertRaises(ValueError, calculate_product, self.ingredient_set[0][0], self.ingredient_set[4][1])

    def test_calculations(self):
        """

        :Test: Testing if function return correct amount of ingredients relative to the original ingredients
        """

        # Testing if results are as expected
        results = [] # A list of dictionaries containing calculated ingredients
        for org_ing, new_ing in self.ingredient_set:
            outcome = calculate_product(org_ing, new_ing)
            results.append(outcome)

        # Converting the results to strings for testing
        str_results = []  # List of containing list that have string value of the results
        for dict_ing in results:
            value_tuple = [] # List of str ingredients
            for ing in dict_ing:
                value_tuple.append(str(dict_ing[ing]))
            else:
                str_results.append(value_tuple)

        # Testing results with expected values
        correct_results = [
            [
                "1.0 XL-egg",
                "0.0 ml",
                "0.0 ml",
                "0.0 Scones"
            ],
            [
                "20.0 J-egg",
                "1.78 l",
                "1111.11 ml",
                "133.0 Scones"
            ],
            [
                "1.0 XL-egg",
                "32.0 ml",
                "20.0 ml",
                "2.0 Scones"
            ],
            [
                "5.0 XL-egg",
                "400.0 ml",
                "250.0 ml",
                "212.5 ml",
                "0.31 kg",
                "30.0 Muffins"
            ],
            [
                "10.0 L-egg",
                "673.02 ml",
                "50.0 Scones"
            ]
        ]

        # Comparing values to expected values
        for result, correct in zip(str_results, correct_results):
            self.assertEqual(result, correct)


class TestCalculateIngredients(unittest.TestCase):
    def setUp(self):
        self.ingredient_set = [
            # Double product
            ({"Product": Ingredients(24, "Scones"),
              "Egg": Egg(4, "XL-egg"),
              "Milk": Wet(320, "ml"),
              "Oil": Wet(200, "ml")
              },

             48),

            # half product
            ({"Product": Ingredients(24, "Scones"),
              "Egg": Egg(4, "XL-egg"),
              "Milk": Wet(320, "ml"),
              "Oil": Wet(200, "ml")
              },

             12),

            # quarter of product
            ({"Product": Ingredients(24, "Scones"),
              "Egg": Egg(4, "XL-egg"),
              "Milk": Wet(320, "ml"),
              "Oil": Wet(200, "ml")
              },

             18),

            # 1/4 of product
            ({"Product": Ingredients(24, "Muffins"),
              "Egg": Egg(4, "XL-egg"),
              "Milk": Wet(320, "ml"),
              "Oil": Wet(200, "ml"),
              "Water": Wet(170, "ml"),
              "Sugar": Dry(250, "g")
              },

             6),

            # one product
            ({"Product": Ingredients(24, "Scones"),
              "Egg": Egg(4, "XL-egg"),
              "Milk": Wet(320, "ml"),
              },

             1)
        ]

    def test_error(self):
        """

        :Test: Testing that proper errors are raised
        """

        # Testing errors being raised for no int or float values
        self.assertRaises(ValueError, lambda x,y: calculate_ingredients(x, y), self.ingredient_set[0][0], "number")

        # Testing errors being raised for negative values
        self.assertRaises(ValueError, lambda x,y: calculate_ingredients(x, y), self.ingredient_set[0][0], -5)

    def test_calculation(self):

        # Testing if results are as expected
        results = []  # A list of dictionaries containing calculated ingredients
        for org_ing, new_prod in self.ingredient_set:
            outcome = calculate_ingredients(org_ing, new_prod)
            results.append(outcome)

        # Converting the results to strings for testing
        str_results = []  # List of containing list that have string value of the results
        for dict_ing in results:
            value_tuple = []  # List of str ingredients
            for ing in dict_ing:
                value_tuple.append(str(dict_ing[ing]))
            else:
                str_results.append(value_tuple)

        # Testing results with expected values
        correct_results = [
            [
                "48.0 Scones",
                "8.0 XL-egg",
                "640.0 ml",
                "400.0 ml"
            ],
            [
                "12.0 Scones",
                "2.0 XL-egg",
                "160.0 ml",
                "100.0 ml"
            ],
            [
                "18.0 Scones",
                "3.0 XL-egg",
                "240.0 ml",
                "150.0 ml"
            ],
            [
                "6.0 Muffins",
                "1.0 XL-egg",
                "80.0 ml",
                "50.0 ml",
                "42.5 ml",
                "62.5 g"
            ],
            [
                "1.0 Scones",
                "1.0 XL-egg",
                "13.33 ml"
            ]
        ]

        # Comparing values to expected values
        for result, correct in zip(str_results, correct_results):
            self.assertEqual(result, correct)
