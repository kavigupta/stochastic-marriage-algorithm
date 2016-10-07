
from random import randint

class Rogues:
    def __init__(self, pairing, ranking):
        self.__rogues = []
        for p in pairing.people:
            q = pairing.partner_of(p)
            print(p, q, list(ranking.all_preferred(p, q)))
            for q_star in ranking.all_preferred(p, q):
                p_star = pairing.partner_of(q_star)
                print(p, q, q_star, p_star, ranking.prefers(q_star, p, p_star))
                if ranking.prefers(q_star, p, p_star):
                    self.__rogues.append((p, q_star))
    def __len__(self):
        return len(self.__rogues)
    def select(self):
        return self.__rogues.pop(randint(0, len(self) - 1))