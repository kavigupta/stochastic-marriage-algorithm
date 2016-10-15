
class Pairing:
    def __init__(self, *pairs):
        self.__pairing = {k:v for k, v in pairs}
        self.__pairing.update({v:k for k, v in pairs})
        self.__one_group = tuple(x for x, y in pairs)
    def partner_of(self, p):
        return self.__pairing[p]
    @property
    def first_group(self):
        return self.__one_group
    def pair(self, a, b):
        astar = self.partner_of(b)
        bstar = self.partner_of(a)
        self.__pairing[a] = b
        self.__pairing[bstar] = astar
        self.__pairing[astar] = bstar
        self.__pairing[b] = a
        return astar, bstar
    def __eq__(self, other):
        return self.__pairing == other.__pairing # pylint: disable=W0212
    def __iter__(self):
        return iter((p, self.partner_of(p)) for p in self.first_group)
    def __repr__(self):
        return "Pairing%s" % (tuple(self),)