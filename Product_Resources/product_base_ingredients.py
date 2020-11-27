from CALCULATORS.Ingredients import Wet, Dry, Egg, Ingredients

Base_Ingredients = {'Muffins': {'Muffins': Ingredients(12, ''),
                                'Egg': Egg(2, 'XL-egg'),
                                'Oil': Wet(125, 'ml'),
                                'Water': Wet(200, 'ml'),
                                'Muffin mix': Dry(500, 'g')
                                },

                    'Scones': {'Scones': Ingredients(12, ''),
                               'Egg': Egg(2, 'XL-egg'),
                                'Oil': Wet(100, 'ml'),
                               'Milk': Wet(160, 'ml'),
                                'Scone mix': Dry(500, 'g')
                               }}
