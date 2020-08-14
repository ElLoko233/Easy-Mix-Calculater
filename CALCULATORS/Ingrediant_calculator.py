from Ingredients import Wet, Dry, Egg, Ingredients

"""
Performing the maths that involves the ingredients and product
"""


# Tools for calculating the number of products can be produce with given ingredients
def get_key(val, my_dict):
    # function to return key for any value
    for key, value in my_dict.items():
        if val == value.value:
            return key

    return "key doesn't exist"


def product_ratio(exclude_product, new_ingredients):
    # Creating a list of values from new_ingredients in order to determine smallest value
    min_val = [value.value for value in new_ingredients.values()]
    min_key = get_key(min(min_val), new_ingredients)

    ratio = new_ingredients[min_key].value / exclude_product[min_key].value
    return ratio


def calculate_product(org_ingredient: dict, new_ingredient: dict):
    """

    :param org_ingredient: original ingredients
    :param new_ingredient: new ingredients
    :return: return ingredients values of ingredients that can be used and the product they will produce
    """
    exclude_product = org_ingredient  # Excluding the 'Product' item// This line doesnt create a copy of the dict
    Product = exclude_product.pop('Product')

    # Testing if keys on both ingredients are the similar
    if list(exclude_product.keys()) == list(new_ingredient.keys()):

        # Converting values of new_ingredient to units of org_ingredients
        converted_ingredients = {ing: new_ingredient[ing].unit_convert(org_ingredient[ing].unit) for ing in
                                 new_ingredient}

        # Calculating the ratio of ingredients
        ratio = product_ratio(exclude_product, converted_ingredients)

        # Results of the ingredients
        org_ingredient['Product'] = Product  # Returning product value
        converted_ingredients = {ing: org_ingredient[ing] * ratio for ing in org_ingredient}

        # Converting results into new_ingredient unit's
        for ing in new_ingredient:
            # Converting egg size
            if ing == "Egg":
                # Round it off
                converted_ingredients[ing] = round(converted_ingredients[ing].unit_convert(new_ingredient[ing].unit))

                # Egg value is to small default is 1
                if converted_ingredients[ing].value < 1:
                    converted_ingredients[ing].value = 1

            else:
                converted_ingredients[ing] = round(converted_ingredients[ing].unit_convert(new_ingredient[ing].unit), 2)


        else:
            # Converting egg to appropriate measurement
            converted_ingredients['Product'] = round(converted_ingredients['Product'])  # Rounding off products
            return converted_ingredients

    else:
        raise ValueError(f"{org_ingredient} and {new_ingredient} these are not related ingredients")


# ============================================================================


# Tools for calculating ingredients needed to get a number of ingredients
def calculate_ingredients(org_ingredients, new_product):
    """

    :param org_ingredients: orginal ingredients
    :param new_product: The number of product
    :return: will return the ingredients to make a certain number of product
    """

    # The ratio for determining the amounts
    ratio = (new_product/org_ingredients['Product']).value
    print(ratio)
    # Converting egg unit

    converted_ingredients = {}
    for ing in org_ingredients:
        # Testing of egg
        if ing == "Egg":
            converted_ingredients[ing] = round(org_ingredients[ing] * ratio)

            # If less than 1 default to 1
            if converted_ingredients[ing].value < 1:
                converted_ingredients[ing] = 1

        else:
            converted_ingredients[ing] = round(org_ingredients[ing] * ratio, 2)
    else:
        return converted_ingredients



# Testing the calculate product function
init = {
    'Product': Ingredients(24, 'Product'),
    'Egg': Egg(252, 'g'),
    'Oil': Wet(200, 'ml'),
    'Milk': Wet(320, 'ml'),
    'Mix': Dry(1000, 'g')
}

new = {

    'Egg': Egg(1, 'J-egg'),
    'Oil': Wet(400, 'ml'),
    'Milk': Wet(400, 'ml'),
    'Mix': Dry(2000, 'g')
}
