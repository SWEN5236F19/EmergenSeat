class Car:
    def __init__(self):
        self.make = ""
        self.model = ""
        self.year = ""
        self.vin = ""

    def set_car(self, make, model, year, vin):
        self.year = year
        self.make = make
        self.model = model
        self.vin = vin

    def to_json(self):
        json_text = {
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "VIN": self.vin
        }
        return json_text