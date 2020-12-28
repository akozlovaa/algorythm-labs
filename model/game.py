class Game:
    def __init__(self, name="", num_of_characters=0, avg_rate=0):
        self.name = name
        self.num_of_characters = num_of_characters
        self.avg_rate = avg_rate

    def __str__(self):
        return f"GAME: name: {self.name}, number of characters: {self.num_of_characters}, " \
               f"average IMDb rate: {self.avg_rate} "
