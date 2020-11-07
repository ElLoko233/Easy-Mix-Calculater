from CALCULATORS.Ingredients import Wet, Dry, Egg, Ingredients

Base_Ingredients = {'Muffins': {'Eggs:': Egg(2, 'XL-egg'),
                                'Oil:': Wet(125, 'ml'),
                                'Water:': Wet(200, 'ml'),
                                'Muffins:': Ingredients(12, '')},

                    'Scones': {'Eggs:': Egg(2, 'XL-egg'),
                               'Milk:': Wet(160, 'ml'),
                               'Scones:': Ingredients(12, '')}}
