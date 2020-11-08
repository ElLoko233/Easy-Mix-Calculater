from CALCULATORS.Ingredients import Wet, Dry, Egg, Ingredients

Base_Ingredients = {'Muffins': {'Product': Ingredients(12, 'Muffins'),
                                'Egg': Egg(2, 'XL-egg'),
                                'Oil': Wet(125, 'ml'),
                                'Water': Wet(200, 'ml')
                                },

                    'Scones': {'Product': Ingredients(12, 'Scones'),
                               'Egg': Egg(2, 'XL-egg'),
                               'Milk': Wet(160, 'ml')
                               }}
