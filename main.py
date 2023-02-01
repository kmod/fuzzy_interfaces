from fuzzy_interfaces import fuzzy_keywords

@fuzzy_keywords
def testFunction(title, data):
    print("Received %r %r" % (title, data))

if __name__ == "__main__":
    testFunction(Title="hello", content="world")
