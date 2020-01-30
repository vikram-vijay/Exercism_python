class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.conversion_dict = {'earth': 1, 'mercury': 0.2408467, 'venus': 0.61519726, 'mars': 1.8808158,
                                'jupiter': 11.862615, 'saturn': 29.447498, 'uranus': 84.016846, 'neptune': 164.79132}

        for key, value in self.conversion_dict.items():
            setattr(self, 'on_' + key, lambda x=value: round(self.seconds / 31557600 / x, 2))