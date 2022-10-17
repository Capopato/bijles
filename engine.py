class Engine:
    def __init__(self, id_number: int, brand: str):
        self.id_number = id_number
        self.brand = brand

    def __repr__ (self):
        return f"Engine(ID_number: {self.id_number}, Brand: {self.brand})"