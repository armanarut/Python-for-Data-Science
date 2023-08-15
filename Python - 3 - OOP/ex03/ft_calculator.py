class calculator:
    """A simple calculator class"""
    def __init__(self, vector) -> None:
        """Constructor"""
        self.vector = vector

    def __add__(self, object) -> None:
        """Addition"""
        self.vector = [vec + object for vec in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiplication"""
        self.vector = [vec * object for vec in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtraction"""
        self.vector = [vec - object for vec in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Division"""
        if object == 0:
            print("Division by zero is not allowed")
            return
        self.vector = [vec / object for vec in self.vector]
        print(self.vector)
