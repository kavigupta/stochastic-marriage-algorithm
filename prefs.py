class Preferences:
    def __init__(self, prefs):
        self.__prefs = {}
        for rank, person in enumerate(reversed(prefs)):
            self.__prefs[person] = rank
    def prefers(self, x, y):
        if x not in self.__prefs or y not in self.__prefs:
            return False
        return self.__prefs[y] < self.__prefs[x]
    def __iter__(self):
        rank_person = [(person, rank) for rank, person in self.__prefs.items()]
        return reversed([person for _, person in sorted(rank_person)])
    def __repr__(self):
        return "Preferences(%r)" % list(self)