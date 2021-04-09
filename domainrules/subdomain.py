from rules import NullRule, Rule


class Fileds(NullRule):
    min_qty: int

class SubdomainRule(Rule):
    fields = Fileds

    @property
    def calc_weight(self):
        return self.bal if self.domain.name.count('.')>self.min_qty else 0
