from .Ingredients import Wet, Dry, Egg, Ingredients
import logging

"""
Performing the maths that involves the ingredients and product
"""

# Creating logger objects ==============================================================================================
calculator_logger = logging.getLogger("Calculator Logger")
calculator_logger.setLevel(logging.INFO)

# Creating Formatter object
LOG_FORMAT = logging.Formatter(fmt="%(levelname)s:Function-%(funcName)s, In_line-%(lineno)d: Message-%(message)s")

# Creating the file handlers
calculator_log_file = logging.FileHandler(filename="Calculator_logs.log")
calculator_log_file.setFormatter(LOG_FORMAT)
calculator_log_file.setLevel(logging.INFO)

# Adding handlers to the respective logger objects
calculator_logger.addHandler(calculator_log_file)
calculator_logger
# ======================================================================================================================

# Tools for calculating the number of products can be produce with given ingredients
def get_key(val, my_dict: dict):
    """
    ::my_dict: Dictionary of Ingredient objects
    ::returns: Key to the Ingredient object with the smallest value
    """

    for key, value in my_dict.items():
        if val == value.value:
            return key

    return "key doesn't exist"


def product_ratio(exclude_product: dict, new_ingredients: dict):
    """
    ::exclude_products:  Dictionary of Ingredient objects, excluding the Products ingredient
    ::new_ingredients:  Dictionary of Ingredient objects
    """

    # Creating a list of values from new_ingredients in order to determine smallest value
    min_val = [value.value for value in new_ingredients.values()]
    min_key = get_key(min(min_val), new_ingredients)

    ratio = new_ingredients[min_key].value / exclude_product[min_key].value
    return ratio


def calculate_product(org_ingredient: dict, new_ingredient: dict):
    # Note egg of original ingredients comes in as grams
    """
    :param org_ingredient: original ingredients, Dictionary of Ingredient objects
    :param new_ingredient: new ingredients, Dictionary of Ingredient objects
    :return: return an adjusted Dictioanary of Ingredient object,
    """
    calculator_logger.info(f"Parsed values--Org_ing:{[str(org_ingredient[ing]) for ing in org_ingredient]}"
                           f"<--->new_ing:{[str(new_ingredient[ing]) for ing in new_ingredient]}")

    exclude_product = org_ingredient  # Excluding the 'Product' item// This line doesnt create a copy of the dict
    Product = exclude_product.pop('Product')

    # Testing if keys on both ingredients are the similar
    if list(exclude_product.keys()) == list(new_ingredient.keys()):

        # Converting values of new_ingredient to units of org_ingredients

        converted_ingredients = {ing: new_ingredient[ing].unit_convert(org_ingredient[ing].unit) for ing in
                                 new_ingredient}
        calculator_logger.info("Converted values of new_ingredient to units of org_ingredients")

        # Calculating the ratio of ingredients
        ratio = product_ratio(exclude_product, converted_ingredients)
        calculator_logger.info(f"ratio as calculated to be {ratio}")

        # Results of the ingredients
        org_ingredient['Product'] = Product  # Returning product value
        converted_ingredients = {ing: org_ingredient[ing] * ratio for ing in org_ingredient}

        # converting ingredients to units of new_ingredients
        for ing in new_ingredient:

            converted_ingredients[ing] = round(converted_ingredients[ing].unit_convert(new_ingredient[ing].unit), 2)

        else:
            # Testing if egg is less than one
            if converted_ingredients["Egg"] < 1:
                converted_ingredients["Egg"].value = 1.0

            # Rounding eggs and products to the whole number
            converted_ingredients['Product'] = round(converted_ingredients['Product'])  # Rounding off products
            converted_ingredients["Egg"] = round(converted_ingredients["Egg"])
            calculator_logger.info("Calculations completed!! \n\n")
            return converted_ingredients

    else:
        calculator_logger.error("Ingredients did not match \n\n")
        raise ValueError(f"{[str(org_ingredient[ing]) for ing in org_ingredient]} and {[str(new_ingredient[ing]) for ing in new_ingredient]} these are not related ingredients")


# ============================================================================

# Tools for calculating ingredients needed to get a number of ingredients
def calculate_ingredients(org_ingredients: dict, new_product: int):
    """

    :param org_ingredients: original ingredients, Dictionary of Ingredient objects
    :param new_product: The number of product
    :return: will return the ingredients to make a certain number of product
    """
    calculator_logger.info(f"Parsed values--org_ing:{[str(org_ingredients[ing]) for ing in org_ingredients]}"
                           f"<--->new_product:{new_product}")

    # Testing if product is positive value
    if float(new_product) or new_product > 0:
        # The ratio for determining the amounts
        ratio = (new_product / org_ingredients['Product']).value
        calculator_logger.info(f"Calculated ratio  is:{ratio}")

        # Converting egg unit
        converted_ingredients = {}
        for ing in org_ingredients:
            # Testing of egg
            if ing == "Egg":
                converted_ingredients[ing] = round(org_ingredients[ing] * ratio)

                # If less than 1 default to 1
                if converted_ingredients[ing].value < 1:
                    converted_ingredients[ing].value = 1.0

            else:
                converted_ingredients[ing] = round(org_ingredients[ing] * ratio, 2)
        else:
            calculator_logger.info("Calculations complete!! \n\n")
            return converted_ingredients

    else:
        calculator_logger.error("new_product was not an integer or float \n\n")
        raise ValueError(f"Unable to calculate ingredients with '{new_product}' must be positive float or integer")
