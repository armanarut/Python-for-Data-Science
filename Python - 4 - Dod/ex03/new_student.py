import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random string of fixed length"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A student class"""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """Create the login at the end of the init"""
        self.login = self.name[0] + self.surname
