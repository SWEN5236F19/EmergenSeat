class Car:
    def __init__(self):
        self.make = ""
        self.model = ""
        self.year = ""
        self.vin = ""

    def to_json(self):
        json_text = {
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "VIN": self.vin
        }