from properties import fill_properties

class Game:
    properties: []

    def __init__(self):
        self.properties = fill_properties()

    def print_all_properties(self):
        print("All properties:")
        for prop in self.properties:
            print(f"  {prop}")

    def print_avail_properties(self):
        print("Properties still available:")
        for prop in self.properties:
            if prop.owner == 0:
                print(f"  {prop}")

    def get_property(self, space):
        for prop in self.properties:
            if prop.space == space:
                return prop
        return None

    def purchase_property(self, prop, plyr):
        prop.owner = plyr.id
        plyr.balance -= prop.cost
        plyr.properties.append(prop)