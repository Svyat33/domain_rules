from Levenshtein._levenshtein import distance
from pydantic import validator

from rules import NullRule, gt0, Rule


class Fields(NullRule):
    possible: int
    base_name: str
    _gt0_possible = validator('possible', allow_reuse=True)(gt0)



class LevensteinRule(Rule):
    fields = Fields

    @property
    def calc_weight(self):
        prepared_domain_name = self.domain.name.replace(".",'').replace("-",'')
        prepared_base_name = self.base_name.replace(".", '').replace("-", '')
        return self.bal if distance(prepared_domain_name, prepared_base_name) < self.possible else 0

