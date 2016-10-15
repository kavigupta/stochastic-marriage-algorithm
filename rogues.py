
from random import randint

class Rogues:
    def __init__(self, pairing, ranking):
        self.__rogues = []
        self.__ranking = ranking
        self.__pairing = pairing
        used_ps = set()
        for p in pairing.first_group:
            used_ps.add(p)
            q = pairing.partner_of(p)
            for q_star in ranking.all_preferred(p, q):
                if q_star in used_ps:
                    continue
                p_star = pairing.partner_of(q_star)
                if ranking.prefers(q_star, p, p_star):
                    self.__rogues.append((p, q_star))
    def not_empty(self):
        return len(self) != 0
    def add_if_rogue(self, a, b):
        
        pass
    def __len__(self):
        return len(self.__rogues)
    def select(self):
        return self.__rogues.pop(randint(0, len(self) - 1))
    def __str__(self):
        return "<rogues object with elements: %s>" % (tuple(self.__rogues),)