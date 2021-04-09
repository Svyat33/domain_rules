'''
6.GreenDomain  удаляет все записи с субдоменами от указаного в парметрах
домена второго уровня. тоесть Greendomain amazon.com удалит server2.amazon.com
 и любые другие субдомены из списка до начала проверки на синтаксис.
'''
from rules import NullRule, Rule


class Fields(NullRule):
    domain_part: str # "com"


class DomainEmulRule(Rule):
    fields = Fields

    @property
    def calc_weight(self):
        variants = ['-<PART>.','.<PART>.','-<PART>-',]
        return self.bal if any([ p in self.domain.name for p in map(lambda m: m.replace("<PART>", self.domain_part), variants )  ]) else 0

