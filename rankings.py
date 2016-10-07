
from prefs import Preferences

class Rankings:
    def __init__(self, prefs):
        prefs2 = {}
        for k, v in prefs.items():
            prefs2[k] = Preferences(v) if isinstance(v, list) else v
        self.__prefs = prefs2
    def prefers(self, person, other, other2):
        return self.__prefs[person].prefers(other, other2)
    def all_preferred(self, person, other):
        return self.__prefs[person].all_preferred_to(other)
    def __repr__(self):
        return "Rankings(%s)" % (self.__prefs)