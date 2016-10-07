
class Pairing:
    def __init__(self, *pairs):
        self.__pairing = {k:v for k, v in pairs}
        self.__pairing.update({v:k for k, v in pairs})
    def partner_of(self, p):
        return self.__pairing[p]
    @property
    def people(self):
        return self.__pairing.keys()