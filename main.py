from fuzzy_interfaces import fuzzy_keywords, FuzzyModule

@fuzzy_keywords
def testFunction(title, data):
    print("Received %r %r" % (title, data))

if __name__ == "__main__":
    testFunction(Title="hello", content="world")

    fuzzy_json = FuzzyModule("json")

    print(fuzzy_json.dumpss(object="hello world"))
