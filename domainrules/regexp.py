import re

from pydantic import validator

from rules import Rule, NullRule


class RegexpFields(NullRule):
    regexp: str

    @validator('regexp')
    def reg_is_valid(cls, val):
        try:
            a = re.compile(val)
            return val
        except:
            raise ValueError("Incorrect regexp")


class RegexpRule(Rule):
    fields = RegexpFields

    def set_rules(self, **kwargs):
        super().set_rules(**kwargs)
        self.reg = re.compile(self.regexp)
        return self

    @property
    def calc_weight(self):
        return self.bal if re.match(self.reg, self.domain.name) else 0
