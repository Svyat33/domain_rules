'''
6.GreenDomain  удаляет все записи с субдоменами от указаного в парметрах
домена второго уровня. тоесть Greendomain amazon.com удалит server2.amazon.com
 и любые другие субдомены из списка до начала проверки на синтаксис.
'''
from rules import NullRule, Rule


class Fields(NullRule):
    domain_name: str


class GreenDomainRule(Rule):
    fields = Fields

    @property
    def calc_weight(self):
        return -1*self.bal if self.domain.name.endswith(self.domain_name) else 0
