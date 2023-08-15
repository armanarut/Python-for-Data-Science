from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A class representing the King family."""

    def __init__(self, first_name, is_alive=True):
        """Constructor of the class King
    Parameters:
        first_name (str): the first name of the character
        is_alive (bool): True if the character is alive, False otherwise"""

        super().__init__(first_name, is_alive)

    def __str__(self):
        """Return the string to print with the print() function"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return the string to print with the print() function"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """Kill the character"""
        self.is_alive = False

    def set_eyes(self, eyes):
        """Set the color of the eyes"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Set the color of the hairs"""
        self.hairs = hairs

    def get_eyes(self):
        """Return the color of the eyes"""
        return self.eyes

    def get_hairs(self):
        """Return the color of the hairs"""
        return self.hairs
