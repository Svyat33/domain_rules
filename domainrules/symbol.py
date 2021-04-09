from rules import NullRule, Rule


class Fileds(NullRule):
    symbol: str
    min_qty: int

class SymbolRule(Rule):
    fields = Fileds

    @property
    def calc_weight(self):
        return self.bal if self.domain.name.count(self.symbol)>self.min_qty else 0
