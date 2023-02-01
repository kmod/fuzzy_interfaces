import inspect
import types

import spacy

en = spacy.load("en_core_web_md")

def _findClosestMatch(word, options):
    best = None
    best_score = 0.0

    doc = en(word)

    for option in options:
        score = doc.similarity(en(option))
        print(word, option, score)
        if score > best_score:
            best_score = score
            best = option

    print(word, "->", best)
    return best

def fuzzy_keywords(f):
    argnames = inspect.getfullargspec(f).args

    def inner(*args, **kwargs):
        mapped_kw = {}
        for k, v in kwargs.items():
            mapped = _findClosestMatch(k, argnames)
            assert mapped not in mapped_kw, "duplicate keyword %r" % mapped
            assert mapped is not None
            mapped_kw[mapped] = v
        return f(*args, **mapped_kw)

    return inner

def fuzzy_getattr(obj, k):
    attrs = dir(obj)
    mapped = _findClosestMatch(k, attrs)
    assert mapped is not None

    return getattr(obj, mapped)


class FuzzyGetattr:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, k):
        return fuzzy_getattr(self._obj, k)

class FuzzyModule:
    def __init__(self, m):
        if isinstance(m, str):
            m = __import__(m)

        self._m = FuzzyGetattr(m)

    def __getattr__(self, k):
        v = getattr(self._m, k)
        if isinstance(v, types.FunctionType):
            return fuzzy_keywords(v)
        return v
