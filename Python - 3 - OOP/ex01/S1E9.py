from abc import ABC, abstractmethod


class Character(ABC):
    """A class representing the Character family.

    Attributes:
        first_name (str): The first name of the character
        is_alive (bool): The status of the character"""

    def __init__(self, first_name, is_alive=True):
        """Constructor of the class

        Args:
            first_name (str): The first name of the character
            is_alive (bool): The status of the character"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Kill the character"""
        pass


class Stark(Character):
    """A class representing the Stark family.

    Attributes:
        first_name (str): The first name of the character
        is_alive (bool): The status of the character"""

    def die(self):
        """Kill the character in Stark"""
        self.is_alive = False
