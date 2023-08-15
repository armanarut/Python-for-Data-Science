from S1E9 import Character


class Baratheon(Character):
    """A class representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Constructor of the class Baratheon
    Parameters:
        first_name (str): the first name of the character
        is_alive (bool): True if the character is alive, False otherwise"""

        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Return the string to print with the print() function"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return the string to print with the print() function"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """Kill the character"""
        self.is_alive = False

    def create_baratheon(first_name, is_alive=True):
        """Create a Baratheon character
    Parameters:
        first_name (str): the first name of the character
        is_alive (bool): True if the character is alive, False otherwise
    Returns:
        Baratheon: the created character"""
        return Baratheon(first_name, is_alive)


class Lannister(Character):
    """A class representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """Constructor of the class Baratheon
    Parameters:
        first_name (str): the first name of the character
        is_alive (bool): True if the character is alive, False otherwise"""

        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Return the string to print with the print() function"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return the string to print with the print() function"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """Kill the character"""
        self.is_alive = False

    def create_lannister(first_name, is_alive=True):
        """Create a Lannister character
    Parameters:
        first_name (str): the first name of the character
        is_alive (bool): True if the character is alive, False otherwise
    Returns:
        Lannister: the created character"""
        return Lannister(first_name, is_alive)
