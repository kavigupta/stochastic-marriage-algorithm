class Preferences:
    def __init__(self, prefs):
        self.__prefs = {}
        for rank, person in enumerate(prefs):
            self.__prefs[rank] = person
    def prefers(self, x, y):
        print(x, y, "ASDF", self.__prefs[y] < self.__prefs[x])
        return self.__prefs[y] < self.__prefs[x]
    def __repr__(self):
        return "Preferences(%r)" % [y for _, y in sorted(self.__prefs.items())]