import json

class Property:
    name = None
    color = None
    cost = None
    current_rent = None
    rent0 = None
    rentM = None
    rent1 = None
    rent2 = None
    rent3 = None
    rent4 = None
    rentH = None
    # mortgage = house_cost/2

    house_cost = None
    owner = 0
    space = None

    def __init__(self, name, values):
        self.name = name
        self.color = values["color"]
        self.cost = values["cost"]
        self.current_rent = values["rent0"]
        self.rent0 = values["rent0"]
        self.rentM = values["rentM"]
        self.rent1 = values["rent1"]
        self.rent2 = values["rent2"]
        self.rent3 = values["rent3"]
        self.rent4 = values["rent4"]
        self.rentH = values["rentH"]
        self.house_cost = values["house_cost"]
        self.space = values["space"]

    def __str__(self):
        return f"{self.name} \n\rColor: {self.color}\n  Cost: {self.cost}\n  Base Rent: {self.rent0}\n  Rent with Monopoly: {self.rentM}\n  Rent with 1 house: {self.rent1}\n  Rent with 2 houses: {self.rent2}\n  Rent with 3 houses: {self.rent3}\n  Rent with 4 houses: {self.rent4}\n  Rent with a hotel: {self.rentH}\n  Cost of each house: {self.house_cost}\n  Cost of a hotel: {self.house_cost} with 4 houses"


def fill_properties():
    properties = []
    with open("properties.json") as f:
        data = json.loads(f.read())
        for prop in data:
            properties.append(Property(prop, data[prop]))
    return properties
