
from rogues import Rogues

def stochastic_marriage(rankings, pairing):
    rogues = Rogues(pairing, rankings)
    count = 0
    while rogues.not_empty():
        count += 1
        a, b = rogues.select()
        a2, b2 = pairing.pair(a, b)
        rogues.add_if_rogue(a2, b2)
    return pairing, count