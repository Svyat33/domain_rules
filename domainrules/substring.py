from typing import List

from rules import NullRule, Rule


class Fields(NullRule):
    subwords: List[str]


class SubstringRule(Rule):
    '''Правило'''
    fields = Fields

    @property
    def calc_weight(self):
        return self.bal if not self.subwords is None and any(
            [word in self.domain.name for word in self.subwords]) else 0
