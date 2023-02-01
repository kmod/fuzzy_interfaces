# fuzzy_interfaces

This is a **proof of concept** example of how we might include AI into a programming language. It is meant to be thought-provoking, not actually used.

## fuzzy keywords

The most basic feature offered is for fuzzy keyword matching in function calls. It's easiest shown with an example:

```python
from fuzzy_interfaces import fuzzy_keywords

@fuzzy_keywords
def myFunction(data):
    print("Was passed %r" % data)

# This works like normal:
myFunction(data="hello world")
# This works also works:
myFunction(content="foo bar")
```

This works by computing similarity scores for the passed keywords versus the accepted keywords.

> The currently-implemented algorithm is very naive, and will over-match.

This is a bit contrived, but makes a bit more sense in the following example.

## fuzzy modules

This same kind of idea can be used to implement fuzzy attribute lookup. In the case of modules, we can do the fuzzy attribute lookup and wrap any functions in a fuzzy keywords object.

```python
from fuzzy_interfaces import FuzzyModule

fuzzy_requests = FuzzyModule("requests")

fuzzy_requests.fetch(link="http://example.com")
# The actual API is requests.get(url)
```

While I wouldn't necessarily recommend doing this, it dramatically changes how we consume unknown APIs: instead of looking up documentation (or using something like Copilot that has memorized the documentation), we simply write out something semantically correct, and let the system map it to the actual arguments.

## fuzzy interfaces

The most interesting usage, in my opinion, is creating *fuzzy interfaces*. We can imagine the previous use cases being resolved statically and written out without any fuzziness. But with fuzzy interfaces we can actually support use cases that are not possible without fuzziness.

In particular, we can write a function that accepts objects of *similar shapes*. The interface-using code will (not so) intelligently determine how to map the semantic requests onto the shape of the actual object, and can do this differently based on the object provided.

```python
from fuzzy_interfaces import fuzzy_getattr

class Car:
    def drive(self):
        print("Car.drive()")

class Bike:
    def ride(self):
        print("Bike.ride()")

def driveVehicle(vehicle):
    func = fuzzy_getattr(vehicle, "drive")
    func()

driveVehicle(Car())  # prints "Car.drive()"
driveVehicle(Bike()) # prints "Bike.ride()"
```
