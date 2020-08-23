"""
Its a new data type, main class name is Ingredients and it inherits from tuple class
"""
import logging

# Creating logger objects ==============================================================================================
ingredients_logger = logging.getLogger("Ingredient logger")
ingredients_logger.setLevel(logging.INFO)

# Creating Formatter object
LOG_FORMAT = logging.Formatter(fmt="%(levelname)s:Function-%(funcName)s, In_line-%(lineno)d: Message-%(message)s")

# Creating the file handlers
ingredients_log_file = logging.FileHandler(filename="Ingredients_logs.log")
ingredients_log_file.setFormatter(LOG_FORMAT)
ingredients_log_file.setLevel(logging.INFO)

# Adding handlers to the respective logger objects
ingredients_logger.addHandler(ingredients_log_file)


# ======================================================================================================================


class Ingredients:
    """
    This class is used to create ingredient object
    These objects contain essential data for perfroming calculation on ingredients
    ::Format: (value, unit)
    """

    def __init__(self, value: float, unit: str):
        self.value = float(value)
        self.unit = str(unit)

        # Testing if value is positive
        if self.value < 0:
            raise ValueError(f"{self.value}, ingredients can only be positive floats or int")

        # Units of conversion/ SI units
        self._volume_unit = {'ml': 10 ** -3, 'l': 10 ** 0, 'kl': 10 ** 3}
        self._mass_unit = {'g': 10 ** 0, 'kg': 10 ** 3}
        self._egg_size = {'S-egg': 42, 'M-egg': 49, 'L-egg': 53, 'XL-egg': 63, 'J-egg': 70}

    # Magic methods
    def __add__(self, other):

        # Test if object are the from the same class
        if type(self) == type(other):

            # Testing if instances have the same unit value
            if self.unit == other.unit:
                return self.__class__(self.value + other.value, self.unit)

            else:
                raise TypeError(f"Unable to add value of different units, {self.unit} + {other.unit}")

        else:
            raise TypeError(f"Unable to handle operator with {type(self)} and {type(other)}")

    def __sub__(self, other):

        # Test if object are the from the same class
        if type(self) == type(other):

            # Testing if instances have the same unit value
            if self.unit == other.unit:
                return self.__class__(self.value - other.value, self.unit)

            else:
                raise TypeError(f"Unable to add value of different units, {self.unit} + {other.unit}")

        else:
            raise TypeError(f"Unable to handle operator with {type(self)} and {type(other)}")

    def __str__(self):
        return f"{self.value} {self.unit}"

    def __lt__(self, other):
        # Testing if objects are same class
        if type(self) == type(other):
            return self.value < other.value

        elif type(other) == float or type(other) == int:
            return self.value < other

        else:
            raise TypeError(f"cannot test objects of {type(self)} with {type(other)}")

    def __gt__(self, other):
        # Testing if objects are same class
        if type(self) == type(other):
            return self.value > other.value

        elif type(other) == float or type(other) == int:
            return self.value > other

        else:
            raise TypeError(f"cannot test objects of {type(self)} with {type(other)}")

    def __le__(self, other):
        # Testing if objects are same class
        if type(self) == type(other):
            return self.value <= other.value

        elif type(other) == float or type(other) == int:
            return self.value <= other

        else:
            raise TypeError(f"cannot test objects of {type(self)} with {type(other)}")

    def __eq__(self, other):

        # Testing if objects are same class
        if type(self) == type(other):
            return self.value == other.value and self.unit == other.unit

        elif type(other) == float or type(other) == int:
            return self.value == other

        else:
            raise TypeError(f"cannot test objects of {self.__class__} with {other.__class__}")

    def __ne__(self, other):
        # Testing if objects are same class
        if type(self) == type(other):
            return self.value != other.value and self.unit != other.unit

        elif type(other) == float or type(other) == int:
            return self.value != other

        else:
            raise TypeError(f"cannot test objects of {type(self)} with {type(other)}")

    def __ge__(self, other):
        # Testing if objects are same class
        if type(self) == type(other):
            return self.value >= other.value

        elif type(other) == float or type(other) == int:
            return self.value >= other

        else:
            raise TypeError(f"cannot test objects of {type(self)} with {type(other)}")

    def __mul__(self, other):
        # Test if object are  from the same class
        if type(self) == type(other):

            # Testing if instances have the same unit value
            if self.unit == other.unit:
                return self.__class__(self.value * other.value, self.unit)

            else:
                raise TypeError(f"Unable to handle value of different units, {self.unit} * {other.unit}")
        # operation is between __class__ and float
        elif type(float(other)) == float:
            return self.__class__(self.value * other, self.unit)

        else:
            raise TypeError(f"Unable to handle operator with {type(self)} and {type(other)}")

    def __rmul__(self, other):
        # Test if object are  from the same class
        if type(self) == type(other):

            # Testing if instances have the same unit value
            if self.unit == other.unit:
                return self.__class__(other.value * self.value, self.unit)

            else:
                raise TypeError(f"Unable to handle value of different units, {self.unit} + {other.unit}")
        # operation is between __class__ and float
        elif type(float(other)) == float:
            return self.__class__(other * self.value, self.unit)

        else:
            raise TypeError(f"Unable to handle operator with {type(self)} and {type(other)}")

    def __truediv__(self, other):
        # Test if object are  from the same class
        if type(self) == type(other):

            # Testing if instances have the same unit value
            if self.unit == other.unit:
                return self.__class__(self.value / other.value, self.unit)

            else:
                raise TypeError(f"Unable to handle value of different units, {self.unit} + {other.unit}")
        # operation is between __class__ and float
        elif type(float(other)) == float:
            return self.__class__(self.value / other, self.unit)

        else:
            raise TypeError(f"Unable to handle operator with {type(self)} and {type(other)}")

    def __rtruediv__(self, other):
        # Test if object are  from the same class
        if type(self) == type(other):

            # Testing if instances have the same unit value
            if self.unit == other.unit:
                return self.__class__(other.value / self.value, self.unit)

            else:
                raise TypeError(f"Unable to handle value of different units, {self.unit} + {other.unit}")
        # operation is between __class__ and float
        elif type(float(other)) == float:
            return self.__class__(other / self.value, self.unit)

        else:
            raise TypeError(f"Unable to handle operator with {type(self)} and {type(other)}")

    def __len__(self):
        return 2

    def __round__(self, n=None):
        return self.__class__(round(self.value, n), self.unit)


class Wet(Ingredients):
    """
    Manages the calculation partaining to ingredients that have volume
    """

    def __init__(self, value, unit):
        super(Wet, self).__init__(value, unit)
        self.size = self._volume_unit

        # Testing if unit is a volume measurement
        if not (self._volume_unit.get(self.unit)):
            raise TypeError(f"{self.unit} is not valid volume measurement unit")

    # Unit conversion method
    def unit_convert(self, unit_to=None):
        """

        :param unit_to: The unit to convert values into
        :return: It will convert values to the unit_to unit ,if it's not provided it will convert values to litres
        """

        # Converting value into litres
        new_value = self.value * self._volume_unit.get(self.unit)
        new_unit = 'l'
        ingredients_logger.info(f"{self.__class__}:{str(self)}-- Converted to litres")

        # Testing if value conversion is specified
        if unit_to != None:
            # Converting value to specified unit_to
            if self._volume_unit.get(unit_to):
                new_value /= self._volume_unit.get(unit_to)
                new_unit = unit_to
                ingredients_logger.info(f"{self.__class__}:{str(new_value) + new_unit}-- Converted to {unit_to} \n\n")
                return self.__class__(new_value, new_unit)
            else:
                ingredients_logger.error(f"{self.__class__}:{str(new_value) + new_unit}-- Unit_to:{unit_to} is not valid measurement \n\n")
                raise TypeError(f"Unit to convert to is not valid {unit_to}")
        else:
            ingredients_logger.info(f"{self.__class__}:{str(new_value) + new_unit}-- Returned {new_unit} measurement \n\n")
            return self.__class__(new_value, new_unit)


class Dry(Ingredients):
    """
    Manages calculation of ingredients that have mass
    """

    def __init__(self, value, unit):
        super(Dry, self).__init__(value, unit)
        self.size = self._mass_unit

        # Testing if unit is a mass measurement/ egg size is also tested because Egg class values are also tested here
        if not (self._egg_size.get(self.unit)) and not (self._mass_unit.get(self.unit)):
            raise TypeError(f"{self.unit} is not valid mass measurement unit")

    # Unit conversion method
    def unit_convert(self, unit_to=None):
        """

        :param unit_to: The unit to convert values into
        :return: It will convert values to the unit_to unit ,if it's not provided it will convert values to grams
        """

        # Converting value into grams
        new_value = self.value * self._mass_unit.get(self.unit)
        new_unit = 'g'
        ingredients_logger.info(f"{self.__class__}:{str(self)}-- Converted to grams")

        # Testing if value conversion is specified
        if unit_to != None:
            # Converting value to specified unit_to
            if self._mass_unit.get(unit_to):
                new_value /= self._mass_unit.get(unit_to)
                new_unit = unit_to
                ingredients_logger.info(f"{self.__class__}:{str(new_value) + new_unit}-- Converted to {unit_to} \n\n")
                return self.__class__(new_value, new_unit)
            else:
                ingredients_logger.error(f"{self.__class__}:{str(new_value) + new_unit}-- Unit_to:{unit_to} is not valid measurement \n\n")
                raise TypeError(f"Unit to convert to is not valid {unit_to}")
        else:
            ingredients_logger.info(f"{self.__class__}:{str(new_value) + new_unit}-- Returned {new_unit} measurement \n\n")
            return self.__class__(new_value, new_unit)


class Egg(Dry):
    """
    Manages calculation of Egg like ingredients
    """

    def __init__(self, value, unit):
        super(Egg, self).__init__(value, unit)
        self.size = self._egg_size

        # Testing if unit is a egg size
        if not (self._egg_size.get(self.unit)) and not (self._mass_unit.get(self.unit)):
            raise TypeError(f"{self.unit} is not valid egg size")

    # Unit conversion method
    def unit_convert(self, unit_to=None):
        """

        :param unit_to: The unit to convert values into
        :return: It will convert values to the unit_to unit ,if it's not provided it will convert values to grams
        """

        # Testing if unit is mass measurement
        if self._mass_unit.get(self.unit):
            # Converting mass into grams
            new = super(Egg, self).unit_convert()
            new_value = new.value
            new_unit = new.unit
            ingredients_logger.info(f"{self.__class__}:{str(self)}-- Converted to grams")

        # If unit is egg size
        else:
            # Converting mass into grams
            new_value = self.value * self._egg_size.get(self.unit)
            new_unit = 'g'
            ingredients_logger.info(f"{self.__class__}:{str(self)}-- Converted to grams")

        # Testing if value conversion is specified
        if unit_to != None:

            # Converting value to specified unit_to
            if self._egg_size.get(unit_to):  # Testing if convert unit is egg size
                new_value /= self._egg_size.get(unit_to)
                new_unit = unit_to
                ingredients_logger.info(f"{self.__class__}:{str(new_value) + new_unit}-- Converted to {unit_to} \n\n")
                return self.__class__(new_value, new_unit)

            elif self._mass_unit.get(unit_to):  # Testing if convert unit is mass unit
                new_value /= self._mass_unit.get(unit_to)
                new_unit = unit_to
                ingredients_logger.info(f"{self.__class__}:{str(new_value) + new_unit}-- Converted to {unit_to} \n\n")
                return self.__class__(new_value, new_unit)
            else:
                ingredients_logger.error(f"{self.__class__}:{str(new_value) + new_unit}-- Unit_to:{unit_to} is not valid measurement \n\n")
                raise TypeError(f"Unit to convert to is not valid {unit_to}")
        else:
            ingredients_logger.info(f"{self.__class__}:{str(new_value) + new_unit}-- Returned {new_unit} measurement \n\n")
            return self.__class__(new_value, new_unit)
