class Vector3:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"Vector3({self.x}, {self.y}, {self.z})"


class Vector3Configuration(Vector3):
    def __init__(self, x: float, y: float, z: float) -> None:
        super().__init__(x, y, z)

    def __str__(self) -> str:
        return f"Vector3Configuration({self.x}, {self.y}, {self.z})"


class Vector3Cartesian(Vector3):
    def __init__(self, x: float, y: float, z: float) -> None:
        super().__init__(x, y, z)

    def __str__(self) -> str:
        return f"Vector3Cartesian({self.x}, {self.y}, {self.z})"
