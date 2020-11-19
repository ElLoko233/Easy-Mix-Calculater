from CALCULATORS.Ingredients import Wet, Dry, Egg, Ingredients

Base_Ingredients = {'Muffins': {'Muffins': Ingredients(12, 'm'),
                                'Egg': Egg(2, 'XL-egg'),
                                'Oil': Wet(125, 'ml'),
                                'Water': Wet(200, 'ml'),
                                'mix': Dry(500, 'g')
                                },

                    'Scones': {'Scones': Ingredients(12, 's'),
                               'Egg': Egg(2, 'XL-egg'),
                               'Milk': Wet(160, 'ml'),
                                'mix': Dry(500, 'g')
                               }}
