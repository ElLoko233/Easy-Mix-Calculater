from .Ingredients import Ingredients

"""
Performing the maths that involves the ingredients and product
"""
if __name__ == '__main__':
    import logging

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
def product_ratio(exclude_product: dict, new_ingredients: dict):
    """
    this function gets the smallest ratio between the dictionary of ingredient objects
    ::exclude_products:  Dictionary of Ingredient objects, excluding the Product
    ::new_ingredients:  Dictionary of Ingredient objects
    """
    # creating a ratio list
    ratio_list = [
        new_ingredients.get(exclude_product_ingredient).value / exclude_product.get(exclude_product_ingredient).value
        for
        exclude_product_ingredient in exclude_product.keys()]

    ratio = min(ratio_list)
    return ratio


def calculate_product(org_ingredient: dict, new_ingredient: dict):
    # Note egg of original ingredients comes in as grams
    """
    :param org_ingredient: original ingredients, Dictionary of Ingredient objects
    :param new_ingredient: new ingredients, Dictionary of Ingredient objects excluding product
    :return: return an adjusted Dictioanary of Ingredient object,
    """
    if __name__ == '__main__':
        calculator_logger.info(f"Parsed values--Org_ing:{[str(org_ingredient[ing]) for ing in org_ingredient]}"
                               f"<--->new_ing:{[str(new_ingredient[ing]) for ing in new_ingredient]}")

    exclude_product = org_ingredient.copy()  # Excluding the 'Product' item// This line doesnt create a copy of the dict

    for ing in exclude_product:
        if type(exclude_product[ing]) == Ingredients:
            product_name = ing
            break

    Product = exclude_product.pop(product_name)

    # Testing if keys on both ingredients are the similar
    if list(exclude_product.keys()) == list(new_ingredient.keys()):

        # Converting values of new_ingredient to units of org_ingredients
        converted_ingredients = {ing: new_ingredient[ing].unit_convert(org_ingredient[ing].unit) for ing in
                                 new_ingredient}
        if __name__ == '__main__':
            calculator_logger.info("Converted values of new_ingredient to units of org_ingredients")

        # Calculating the ratio of ingredients
        ratio = product_ratio(exclude_product, converted_ingredients)

        if __name__ == '__main__':
            calculator_logger.info(f"ratio as calculated to be {ratio}")

        # Results of the ingredients
        org_ingredient[product_name] = Product  # Returning product value
        converted_ingredients = {ing: org_ingredient[ing] * ratio for ing in org_ingredient}

        # converting ingredients to units of new_ingredients
        for ing in new_ingredient:

            converted_ingredients[ing] = round(converted_ingredients[ing].unit_convert(new_ingredient[ing].unit), 2)

        else:
            # Rounding eggs and products to the whole number
            converted_ingredients[product_name] = round(converted_ingredients[product_name])  # Rounding off products

            if __name__ == '__main__':
                calculator_logger.info("Calculations completed!! \n\n")
            return converted_ingredients

    else:
        if __name__ == '__main__':
            calculator_logger.error("Ingredients did not match \n\n")
        raise ValueError(
            f"{list(org_ingredient.keys())} and {list(new_ingredient.keys())} these are not related ingredients")


# ============================================================================

# Tools for calculating ingredients needed to get a number of ingredients
def calculate_ingredients(org_ingredients: dict, new_product: int):
    """

    :param org_ingredients: original ingredients, Dictionary of Ingredient objects
    :param new_product: The number of product
    :return: will return the ingredients to make a certain number of product
    """
    if __name__ == '__main__':
        calculator_logger.info(f"Parsed values--org_ing:{[str(org_ingredients[ing]) for ing in org_ingredients]}"
                               f"<--->new_product:{new_product}")
    # Acquiring name of product
    for ing in org_ingredients:
        Product = ing if type(org_ingredients[ing]) == Ingredients else 'Product'
        break

    # Testing if product is positive value
    if float(new_product) or new_product > 0:
        # The ratio for determining the amounts
        ratio = (new_product / org_ingredients[Product]).value

        if __name__ == '__main__':
            calculator_logger.info(f"Calculated ratio  is:{ratio}")

        # Converting units
        converted_ingredients = {}
        for ing in org_ingredients:
            converted_ingredients[ing] = round(org_ingredients[ing] * ratio, 2)

        else:
            if __name__ == '__main__':
                calculator_logger.info("Calculations complete!! \n\n")
            return converted_ingredients

    else:
        if __name__ == '__main__':
            calculator_logger.error("new_product was not an integer or float \n\n")
        raise ValueError(f"Unable to calculate ingredients with '{new_product}' must be positive float or integer")


if __name__ == '__main__':
    from Ingredients import Ingredients, Wet, Dry, Egg

    org_ing = {'muffins': Ingredients(12, ''),
               'Milk': Wet(125, 'ml'),
               'Water': Wet(200, 'ml'),
               'Mix': Dry(500, 'g'),
               'Eggs': Egg(126, 'g')}

    new_ing = {'Milk': Wet(1008, 'ml'),
               'Water': Wet(5000, 'ml'),
               'Mix': Dry(70, 'kg'),
               'Eggs': Egg(10, 'J-egg')}

    test_results = calculate_product(org_ing, new_ing)
    for i in test_results:
        print(i, test_results[i])
