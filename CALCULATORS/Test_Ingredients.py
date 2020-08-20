import unittest

from .Ingredients import *


class TestIngredients(unittest.TestCase):
    """
    Testing the magic methods of the ingredients
    """

    def setUp(self):
        """

        Initializing the testing variables
        """
        self.test_1 = [
            Ingredients(10, "IceCream"),
            Ingredients(2.5, "IceCream")
        ]

        self.test_2 = [
            Ingredients(20, "Pizza"),
            Ingredients(2.5, "Pizza")
        ]

    def test_init(self):
        """

        :Test: Testing if initialization of ingredients is is done with proper values
        """

        # List of testing variables
        testers = [
            (Ingredients(5, 5), "5.0 5"),
            (Ingredients("5", "food"), "5.0 food")
        ]

        # Testing if errors are raised when negative values is used for ingredients
        self.assertRaises(ValueError, Ingredients, value=-5, unit="Food")

        # Testing if error is raised if value is not an float or integer
        self.assertRaises(ValueError, Ingredients, value="five", unit="Food")

        # Testing if ingredients come out as expected
        for test_var in testers:
            test = str(test_var[0])
            self.assertEqual(test, test_var[1])

    def test_str(self):
        """

        :Test: Testing string conversion
        """

        # Testing if proper string is returned
        self.assertEqual(str(self.test_1[0]), "10.0 IceCream")

    def test_add(self):
        """

        :Test: Testing if ingredients are adding properly
        """

        # Testing if ingredients of similar values add up properly
        self.assertEqual(str(self.test_2[0] + self.test_2[1]), str(Ingredients(22.5, "Pizza")))

        # Testing if ingredients of different value raises proper errors
        self.assertRaises(TypeError, lambda x, y: x + y, self.test_1[0], self.test_2[1])

        # Testing if sum creates a new object
        add = (self.test_2[0] + self.test_2[1])
        self.assertNotEqual(self.test_2[0].__repr__(), add.__repr__())
        self.assertNotEqual(self.test_2[1].__repr__(), add.__repr__())

    def test_subtract(self):
        """

        :Test: Testing if ingredients are adding properly
        """

        # Testing if ingredients of similar values add up properly
        self.assertEqual(str(self.test_2[0] - self.test_2[1]), "17.5 Pizza")

        # Testing if ingredients of different value raises proper errors
        self.assertRaises(TypeError, lambda x, y: x - y, self.test_1[0], self.test_2[1])

        # Testing if sum creates a new object
        add = (self.test_2[0] - self.test_2[1])
        self.assertNotEqual(self.test_2[0].__repr__(), add.__repr__())
        self.assertNotEqual(self.test_2[1].__repr__(), add.__repr__())

    def test_multiplication(self):
        """

        :Test: Testing if ingredients multiply properly against values
        """

        # Testing if error is raised when negative multiplication is attempted
        self.assertRaises(ValueError, lambda x, y: x * y, self.test_2[0], -1)

        # Testing if new object is formed when multiplication is performed
        mul = self.test_2[0] * 2
        self.assertNotEqual(self.test_2[0].__repr__(), mul.__repr__())

        # Testing if multiplication is correct
        self.assertEqual(str(self.test_2[0] * 2), "40.0 Pizza")

        # Testing multiplication if same units
        self.assertEqual(str(self.test_1[0] * self.test_1[1]), "25.0 IceCream")

    def test_division(self):
        """

        :Test: Testing if ingredients multiply properly against values
        """

        # Testing if error is raised when negative division is attempted
        self.assertRaises(ValueError, lambda x, y: x / y, self.test_2[0], -1)

        # Testing if new object is formed when division is performed
        mul = self.test_2[0] / 2
        self.assertNotEqual(self.test_2[0].__repr__(), mul.__repr__())

        # Testing if division is correct
        self.assertEqual(str(self.test_2[0] / 2), "10.0 Pizza")

        # Testing division if same units
        self.assertEqual(str(self.test_1[0] / self.test_1[1]), "4.0 IceCream")

    def test_len(self):
        # Testing if len always returns 2
        self.assertEqual(len(self.test_1[0]), 2)

    def test_eq(self):
        """

        :Testing if equal to operators operate properly:
        """
        # Testing if error is raised for value other int float
        self.assertRaises(TypeError, lambda x, y: x == y, self.test_1[0], "hello")
        self.assertRaises(TypeError, lambda x, y: x == y, self.test_1[0], True)

        # Testing if operator can handle int or float type
        self.assertTrue(self.test_1[0] == 10)
        self.assertTrue(self.test_1[0] == 10.0)

        # Testing bool for equal to
        self.assertTrue(self.test_1[0] == self.test_1[0])

    def test_lt(self):
        """

        :Testing if less than operators operates properly:
        """
        # Testing if error is raised for value other int float
        self.assertRaises(TypeError, lambda x, y: x < y, self.test_1[0], "hello")
        self.assertRaises(TypeError, lambda x, y: x < y, self.test_1[0], True)

        # Testing if operator can handle int or float type
        self.assertTrue(self.test_1[0] < 100)
        self.assertTrue(self.test_1[0] < 100.0)

        # Testing bool for less than
        self.assertTrue(self.test_1[1] < self.test_1[0])

    def test_le(self):
        """

        :Testing if less than or equal to operators operates properly:
        """
        # Testing if error is raised for value other int float
        self.assertRaises(TypeError, lambda x, y: x <= y, self.test_1[0], "hello")
        self.assertRaises(TypeError, lambda x, y: x <= y, self.test_1[0], True)

        # Testing if operator can handle int or float type
        self.assertTrue(self.test_1[0] <= 100)
        self.assertTrue(self.test_1[0] <= 10.0)

        # Testing bool for less than or equal to
        self.assertTrue(self.test_1[1] <= self.test_1[0])

    def test_gt(self):
        """

        :Testing if greater than operators operates properly:
        """
        # Testing if error is raised for value other int float
        self.assertRaises(TypeError, lambda x, y: x > y, self.test_1[0], "hello")
        self.assertRaises(TypeError, lambda x, y: x > y, self.test_1[0], True)

        # Testing if operator can handle int or float type
        self.assertTrue(self.test_1[0] > 1)
        self.assertTrue(self.test_1[0] > 1.0)

        # Testing bool for greater than
        self.assertTrue(self.test_1[0] > self.test_1[1])

    def test_ge(self):
        """

        :Testing if greater than or equal to operators operates properly:
        """
        # Testing if error is raised for value other int float
        self.assertRaises(TypeError, lambda x, y: x >= y, self.test_1[0], "hello")
        self.assertRaises(TypeError, lambda x, y: x >= y, self.test_1[0], True)

        # Testing if operator can handle int or float type
        self.assertTrue(self.test_1[0] >= 1)
        self.assertTrue(self.test_1[0] >= 10.0)

        # Testing bool for greater than or equal to
        self.assertTrue(self.test_1[0] >= self.test_1[1])

    def test_round(self):
        """

        :Test: Testing if rounding of of values is done properly
        """

        # Testing rounding off
        float_ing = self.test_1[0] / 3.1445
        self.assertEqual(str(round(float_ing, 4)), "3.1802 IceCream")
        self.assertEqual(str(round(float_ing)), "3.0 IceCream")

        # Testing if new object is created
        self.assertNotEqual(round(float_ing, 4).__repr__(), float_ing.__repr__())
        self.assertNotEqual(round(float_ing).__repr__(), float_ing.__repr__())


class TestEgg(unittest.TestCase):
    def setUp(self):
        self.mass_ingredients = [
            Egg(10, "g"),
            Egg(10, "kg")
        ]

        self.egg_ingredients = [
            Egg(10, "S-egg"),
            Egg(10, "M-egg"),
            Egg(10, "L-egg"),
            Egg(10, "XL-egg"),
            Egg(10, "J-egg")
        ]

    def test_init(self):
        """

        :Test: Testing if initialization of egg is done properly
        """

        # Testing if error is raised when invalid unit is used
        self.assertRaises(TypeError, lambda x: Egg(10, "Poultry"))
        self.assertRaises(TypeError, lambda x: Egg(10, 'l'))
        self.assertRaises(TypeError, lambda x: Egg(10, 'ml'))
        self.assertRaises(TypeError, lambda x: Egg(10, 'kl'))

        # Testing if error is raised when values are not int or string
        self.assertRaises(TypeError, lambda x: Egg("Egg", "S-egg"))
        self.assertRaises(TypeError, lambda x: Egg(True, "L-egg"))

    def test_to_g(self):
        """

        :Test: Testing if converters convert value of egg to grams properly
        """

        # Testing if conversion to grams of mass units is done correct
        correct_mass = [
            "10.0 g",
            "10000.0 g"
        ]
        for egg, correct_egg_mass in zip(self.mass_ingredients, correct_mass):
            self.assertEqual(str(egg.unit_convert()), correct_egg_mass)

        # Testing if conversion to grams of egg sizes is done properly
        correct_size = [
            "420.0 g",
            "490.0 g",
            "530.0 g",
            "630.0 g",
            "700.0 g",
        ]
        for egg, correct_egg_size in zip(self.egg_ingredients, correct_size):
            self.assertEqual(str(egg.unit_convert()), correct_egg_size)

    def test_to_kg(self):
        """

        :Test: Testing if converters convert value of egg to kilograms properly
        """

        # Testing if conversion to kilograms of mass units is done correct
        correct_mass = [
            "0.01 kg",
            "10.0 kg"
        ]
        for egg, correct_egg_mass in zip(self.mass_ingredients, correct_mass):
            self.assertEqual(str(egg.unit_convert(unit_to="kg")), correct_egg_mass)

        # Testing if conversion to grams of egg sizes is done properly
        correct_size = [
            "0.42 kg",
            "0.49 kg",
            "0.53 kg",
            "0.63 kg",
            "0.7 kg",
        ]
        for egg, correct_egg_size in zip(self.egg_ingredients, correct_size):
            self.assertEqual(str(egg.unit_convert(unit_to="kg")), correct_egg_size)

    def test_to_S_egg(self):
        """

        :Test: Testing if converters convert value of egg to S-egg properly
        """

        # Testing if conversion to S-egg  of mass units is done correct
        correct_mass = [
            "0.238 S-egg",
            "238.095 S-egg"
        ]
        for egg, correct_egg_mass in zip(self.mass_ingredients, correct_mass):
            self.assertEqual(str(round(egg.unit_convert(unit_to="S-egg"), 3)), correct_egg_mass)

        # Testing if conversion to S-egg  of egg sizes is done properly
        correct_size = [
            "10.0 S-egg",
            "11.667 S-egg",
            "12.619 S-egg",
            "15.0 S-egg",
            "16.667 S-egg",
        ]
        for egg, correct_egg_size in zip(self.egg_ingredients, correct_size):
            self.assertEqual(str(round(egg.unit_convert(unit_to="S-egg"), 3)), correct_egg_size)

    def test_to_M_egg(self):
        """

        :Test: Testing if converters convert value of egg to M-egg properly
        """

        # Testing if conversion to grams of M-egg units is done correct
        correct_mass = [
            "0.204 M-egg",
            "204.082 M-egg"
        ]
        for egg, correct_egg_mass in zip(self.mass_ingredients, correct_mass):
            self.assertEqual(str(round(egg.unit_convert(unit_to="M-egg"), 3)), correct_egg_mass)

        # Testing if conversion to M-egg of egg sizes is done properly
        correct_size = [
            "8.571 M-egg",
            "10.0 M-egg",
            "10.816 M-egg",
            "12.857 M-egg",
            "14.286 M-egg",
        ]
        for egg, correct_egg_size in zip(self.egg_ingredients, correct_size):
            self.assertEqual(str(round(egg.unit_convert(unit_to="M-egg"), 3)), correct_egg_size)

    def test_to_L_egg(self):
        """

        :Test: Testing if converters convert value of egg to L-egg properly
        """

        # Testing if conversion to grams of L-egg units is done correct
        correct_mass = [
            "0.189 L-egg",
            "188.679 L-egg"
        ]
        for egg, correct_egg_mass in zip(self.mass_ingredients, correct_mass):
            self.assertEqual(str(round(egg.unit_convert(unit_to="L-egg"), 3)), correct_egg_mass)

        # Testing if conversion to L-egg of egg sizes is done properly
        correct_size = [
            "7.925 L-egg",
            "9.245 L-egg",
            "10.0 L-egg",
            "11.887 L-egg",
            "13.208 L-egg",
        ]
        for egg, correct_egg_size in zip(self.egg_ingredients, correct_size):
            self.assertEqual(str(round(egg.unit_convert(unit_to="L-egg"), 3)), correct_egg_size)

    def test_to_XL_egg(self):
        """

        :Test: Testing if converters convert value of egg to XL-egg properly
        """

        # Testing if conversion to XL-egg of mass units is done correct
        correct_mass = [
            "0.159 XL-egg",
            "158.73 XL-egg"
        ]
        for egg, correct_egg_mass in zip(self.mass_ingredients, correct_mass):
            self.assertEqual(str(round(egg.unit_convert(unit_to="XL-egg"), 3)), correct_egg_mass)

        # Testing if conversion to Xl-egg of egg sizes is done properly
        correct_size = [
            "6.667 XL-egg",
            "7.778 XL-egg",
            "8.413 XL-egg",
            "10.0 XL-egg",
            "11.111 XL-egg",
        ]
        for egg, correct_egg_size in zip(self.egg_ingredients, correct_size):
            self.assertEqual(str(round(egg.unit_convert(unit_to="XL-egg"), 3)), correct_egg_size)

    def test_to_J_egg(self):
        """

        :Test: Testing if converters convert value of egg to J-egg properly
        """

        # Testing if conversion to J-egg  of mass units is done correct
        correct_mass = [
            "0.143 J-egg",
            "142.857 J-egg"
        ]
        for egg, correct_egg_mass in zip(self.mass_ingredients, correct_mass):
            self.assertEqual(str(round(egg.unit_convert(unit_to="J-egg"), 3)), correct_egg_mass)

        # Testing if conversion to J-egg  of egg sizes is done properly
        correct_size = [
            "6.0 J-egg",
            "7.0 J-egg",
            "7.571 J-egg",
            "9.0 J-egg",
            "10.0 J-egg",
        ]
        for egg, correct_egg_size in zip(self.egg_ingredients, correct_size):
            self.assertEqual(str(round(egg.unit_convert(unit_to="J-egg"), 3)), correct_egg_size)

    def test_conversion_errors(self):
        """

        :Test: Testing if error are raised for invalid conversion
        """
        # Testing if error is raised attempting to convert to not (egg size, mass)
        for egg in self.mass_ingredients:
            self.assertRaises(TypeError, lambda x: x.unit_convert(unit_to="l"), egg)

        # Testing if error is raised attempting to convert to no existing unit
        for egg in self.egg_ingredients:
            self.assertRaises(TypeError, lambda x: x.unit_convert(unit_to="pound"), egg)

    def test_new_obj(self):

        """

        :Test: Testing if new object is created when converting
        """
        # Testing if new objects are created when converting to mass
        for dry in self.mass_ingredients:
            self.assertNotEqual(dry.__repr__(), dry.unit_convert().__repr__())

        for dry in self.egg_ingredients:
            self.assertNotEqual(dry.__repr__(), dry.unit_convert(unit_to="kg").__repr__())

    # Testing if new objects are created when converting to egg size
        # S-egg
        for dry in self.mass_ingredients:
            self.assertNotEqual(dry.__repr__(), dry.unit_convert(unit_to="S-egg").__repr__())

        for dry in self.egg_ingredients:
            self.assertNotEqual(dry.__repr__(), dry.unit_convert(unit_to="S-egg").__repr__())

        # M-egg
        for dry in self.mass_ingredients:
            self.assertNotEqual(dry.__repr__(), dry.unit_convert(unit_to="M-egg").__repr__())

        for dry in self.egg_ingredients:
            self.assertNotEqual(dry.__repr__(), dry.unit_convert(unit_to="M-egg").__repr__())

        # L-egg
        for dry in self.mass_ingredients:
            self.assertNotEqual(dry.__repr__(), dry.unit_convert(unit_to="L-egg").__repr__())

        for dry in self.egg_ingredients:
            self.assertNotEqual(dry.__repr__(), dry.unit_convert(unit_to="L-egg").__repr__())

        # XL-egg
        for dry in self.mass_ingredients:
            self.assertNotEqual(dry.__repr__(), dry.unit_convert(unit_to="XL-egg").__repr__())

        for dry in self.egg_ingredients:
            self.assertNotEqual(dry.__repr__(), dry.unit_convert(unit_to="XL-egg").__repr__())

        # J-egg
        for dry in self.mass_ingredients:
            self.assertNotEqual(dry.__repr__(), dry.unit_convert(unit_to="J-egg").__repr__())

        for dry in self.egg_ingredients:
            self.assertNotEqual(dry.__repr__(), dry.unit_convert(unit_to="J-egg").__repr__())


class TestDry(unittest.TestCase):
    def setUp(self):
        self.mass_ingredients = [
            Dry(10, "g"),
            Dry(10, "kg")
        ]

    def test_init(self):
        # Testing if error is raised when unit is not mass
        self.assertRaises(TypeError, lambda x: Dry(10, "S-egg"))
        self.assertRaises(TypeError, lambda x: Dry(10, "ml"))
        self.assertRaises(TypeError, lambda x: Dry(10, "Flour"))

        # Testing value not being a float or int
        self.assertRaises(TypeError, lambda x: Dry("Fifity", "S-egg"))

    def test_conversion_errors(self):
        """

        :Test: Testing if error are raised for invalid conversion
        """
        # Testing if error is raised attempting to convert to volume or egg size
        for dry in self.mass_ingredients:
            # Egg sizes
            self.assertRaises(TypeError, lambda x: x.unit_convert(unit_to="S-egg"), dry)
            self.assertRaises(TypeError, lambda x: x.unit_convert(unit_to="M-egg"), dry)
            self.assertRaises(TypeError, lambda x: x.unit_convert(unit_to="L-egg"), dry)
            self.assertRaises(TypeError, lambda x: x.unit_convert(unit_to="XL-egg"), dry)
            self.assertRaises(TypeError, lambda x: x.unit_convert(unit_to="J-egg"), dry)

            # Volume
            self.assertRaises(TypeError, lambda x: x.unit_convert(unit_to="l"), dry)
            self.assertRaises(TypeError, lambda x: x.unit_convert(unit_to="ml"), dry)
            self.assertRaises(TypeError, lambda x: x.unit_convert(unit_to="kl"), dry)

        # Testing if error is raised attempting to convert to no existing unit
        for dry in self.mass_ingredients:
            self.assertRaises(TypeError, lambda x: x.unit_convert(unit_to="pound"), dry)

    def test_to_g(self):
        # Testing if gram conversion is done properly
        correct_mass = [
            "10.0 g",
            "10000.0 g"
        ]
        for dry, correct_dry in zip(self.mass_ingredients, correct_mass):
            self.assertEqual(str(dry.unit_convert()), correct_dry)

    def test_to_kg(self):
        # Testing kilogram conversion
        correct_mass = [
            "0.01 kg",
            "10.0 kg"
        ]
        for dry, correct_dry in zip(self.mass_ingredients, correct_mass):
            self.assertEqual(str(dry.unit_convert(unit_to="kg")), correct_dry)

    def test_new_obj(self):
        # Testing if new objects are created when converting to grams
        for dry in self.mass_ingredients:
            self.assertNotEqual(dry.__repr__(), dry.unit_convert().__repr__())

        # Testing if new objects are created when converting to kilograms
        for dry in self.mass_ingredients:
            self.assertNotEqual(dry.__repr__(), dry.unit_convert(unit_to="kg").__repr__())


class TestWet(unittest.TestCase):
    def setUp(self):
        self.mass_ingredients = [
            Wet(10, "l"),
            Wet(10, "ml"),
            Wet(10, "kl")
        ]

    def test_init(self):
        # Testing if error is raised when unit is not volume
        self.assertRaises(TypeError, lambda x: Wet(10, "S-egg"))
        self.assertRaises(TypeError, lambda x: Wet(10, "kg"))
        self.assertRaises(TypeError, lambda x: Wet(10, "Water"))

        # Testing value not being a float or int
        self.assertRaises(TypeError, lambda x: Wet("Fifity", "S-egg"))

    def test_conversion_errors(self):
        """

        :Test: Testing if error are raised for invalid conversion
        """
        # Testing if error is raised attempting to convert to mass or egg size
        for wet in self.mass_ingredients:
            # Egg sizes
            self.assertRaises(TypeError, lambda x: x.unit_convert(unit_to="S-egg"), wet)
            self.assertRaises(TypeError, lambda x: x.unit_convert(unit_to="M-egg"), wet)
            self.assertRaises(TypeError, lambda x: x.unit_convert(unit_to="L-egg"), wet)
            self.assertRaises(TypeError, lambda x: x.unit_convert(unit_to="XL-egg"), wet)
            self.assertRaises(TypeError, lambda x: x.unit_convert(unit_to="J-egg"), wet)

            # Mass
            self.assertRaises(TypeError, lambda x: x.unit_convert(unit_to="g"), wet)
            self.assertRaises(TypeError, lambda x: x.unit_convert(unit_to="kg"), wet)

        # Testing if error is raised attempting to convert to no existing unit
        for wet in self.mass_ingredients:
            self.assertRaises(TypeError, lambda x: x.unit_convert(unit_to="Water"), wet)

    def test_to_l(self):
        # Testing if litre conversion is done properly
        correct_volume = [
            "10.0 l",
            "0.01 l",
            "10000.0 l"
        ]
        for dry, correct_wet in zip(self.mass_ingredients, correct_volume):
            self.assertEqual(str(dry.unit_convert()), correct_wet)

    def test_to_ml(self):
        # Testing if millilitre conversion is done properly
        correct_volume = [
            "10000.0 ml",
            "10.0 ml",
            "10000000.0 ml"
        ]
        for dry, correct_wet in zip(self.mass_ingredients, correct_volume):
            self.assertEqual(str(dry.unit_convert(unit_to="ml")), correct_wet)

    def test_to_kl(self):
        # Testing if kilolitre conversion is done properly
        correct_volume = [
            "0.01 kl",
            "1e-05 kl",
            "10.0 kl"
        ]
        for dry, correct_wet in zip(self.mass_ingredients, correct_volume):
            self.assertEqual(str(dry.unit_convert(unit_to="kl")), correct_wet)