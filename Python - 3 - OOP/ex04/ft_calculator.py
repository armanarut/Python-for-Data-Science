class calculator:
    """A simple calculator class"""

    # decorator
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Dot product"""
        result = sum([vec1 * vec2 for vec1, vec2 in zip(V1, V2)])
        print("Dot product is:", result)
        return result

    # decorator
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add Vector"""
        result = [float(vec1 + vec2) for vec1, vec2 in zip(V1, V2)]
        print("Add Vector is:", result)
        return result

    # decorator
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Sous Vector"""
        result = [float(vec1 - vec2) for vec1, vec2 in zip(V1, V2)]
        print("Sous Vector is:", result)
        return result
