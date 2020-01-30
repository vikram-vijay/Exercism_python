class Allergies:
    def __init__(self, score):
        self.score = score
        self.all_allergens_dict = {'eggs': 1, 'peanuts': 2, 'shellfish': 4, 'strawberries': 8, 'tomatoes': 16,
                                   'chocolate': 32,
                     'pollen': 64, 'cats': 128}

    def allergic_to(self, allergen):
        return bool(self.score & self.all_allergens_dict[allergen])

    @property
    def lst(self):
        return [allergen for allergen, value in self.all_allergens_dict.items()
                if self.score & value]