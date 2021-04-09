"""Let's describe alowed rules!"""

__version__ = "0.1.1"

from .baserule import Rule
from .regexp import RegexpRule
from .substring import SubstringRule
from .symbol import SymbolRule
from .levenstein import LevensteinRule
from .numbers import NumbersRule
from .greendomain import GreenDomainRule
from .reddomin import RedDomainRule
from .subdomain import SubdomainRule
from .domainemul import DomainEmulRule

_ = [
    Rule,
    RegexpRule,
    SubstringRule,
    SymbolRule,
    LevensteinRule,
    NumbersRule,
    GreenDomainRule,
    RedDomainRule,
    SubdomainRule,
    DomainEmulRule,
]


class Domain:
    name: str = ""

    def __init__(self, name: str):
        self.name = name

    @property
    def weight(self):
        return 0

    def __repr__(self):
        return f"<Domain> {self.name}"


class NewRule:
    @classmethod
    def build(cls, domain: Domain, data: dict) -> Rule:
        """Create rule from received dict
        {"type": "LevensteinRule", "bal": 100,
            "possible": 3, "base_name": "alphabank"}
        {"type": "RegexpRule", "bal": 5, "regexp": "al.*bank"}
        {"type": "SubstringRule", "bal": 25,
            "subwords": ["alpha", "abank", "alpha-support"]}
        """
        if data.get("type") in globals():
            # Есть такой класс или переменная
            obj = globals()[data["type"]]
            if issubclass(obj, Rule):
                data.pop("type")
                if obj.validate(**data):
                    return obj(domain).set_rules(**data)

        return Rule(domain).set_rules(bal=0)
