from .regexp import RegexpRule
from .substring import SubstringRule
from .symbol import SymbolRule
from .levenstein import LevensteinRule
from .numbers import NumbersRule
from .greendomain import GreenDomainRule
from .reddomin import RedDomainRule
from .subdomain import SubdomainRule
from .domainemul import DomainEmulRule

_ = [RegexpRule, SubstringRule, SymbolRule, LevensteinRule, NumbersRule, GreenDomainRule, RedDomainRule, SubdomainRule,
     DomainEmulRule]


class NewRule:

    @classmethod
    def build(cls, domain: Domain, data: dict) -> Rule:
        '''Создает конкретное правило на основании полученного словаря
        {"type": "LevensteinRule", "bal": 100, "possible": 3, "base_name": "alphabank"}
        {"type": "RegexpRule", "bal": 5, "regexp": "al.*bank"}
        {"type": "SubstringRule", "bal": 25, "subwords": ["alpha", "abank", "alpha-support"]}
        '''
        if data.get('type') in globals():
            # Есть такой класс или переменная
            obj = globals()[data['type']]
            if issubclass(obj, Rule):
                data.pop('type')
                if obj.validate(**data):
                    return obj(domain).set_rules(**data)
