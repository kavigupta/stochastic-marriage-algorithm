
from prefs import Preferences

class Rankings:
    def __init__(self, prefs):
        prefs2 = {}
        for k, v in prefs.items():
            prefs2[k] = Preferences(v) if isinstance(v, list) else v
        self.__prefs = prefs2
    def prefers(self, person, other, other2):
        return self.__prefs[person].prefers(other, other2)
    def __repr__(self):
        return "StableMarriageInput(%s, %s)" % (self.__prefs)
