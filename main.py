from fuzzy_interfaces import fuzzy_keywords, FuzzyModule, fuzzy_getattr

@fuzzy_keywords
def testFunction(title, data):
    print("Received %r %r" % (title, data))

class Car:
    def drive(self):
        print("Car.drive()")

class Bike:
    def ride(self):
        print("Bike.ride()")

def driveVehicle(vehicle):
    func = fuzzy_getattr(vehicle, "drive")
    func()

if __name__ == "__main__":
    testFunction(Title="hello", content="world")

    fuzzy_requests = FuzzyModule("requests")

    print(fuzzy_requests.fetch(URL="http://example.com/").content)

    driveVehicle(Car())
    driveVehicle(Bike())
