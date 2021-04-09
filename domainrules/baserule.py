from pydantic import BaseModel, validator

from domainrules import gt0, Domain


class BaseRule(BaseModel):
    bal: int = 0
    _gt0_bal = validator('bal', allow_reuse=True)(gt0)


class Rule(Domain):
    fields: BaseModel = BaseRule

    def __init__(self, domain: Domain):
        self.domain = domain

    def __repr__(self):
        return f"<{self.__class__.__name__}> for {self.domain}"

    @property
    def name(self):
        return self.domain.name

    @classmethod
    def validate(cls, **kwargs):
        return cls.fields.validate(kwargs)

    def set_rules(self, **kwargs):
        for k in self.validate(**kwargs).dict():
            setattr(self, k, kwargs[k])
        return self

    @property
    def calc_weight(self):
        # Зная домен и правила можно рассчитать добавляемый штрафной вес
        return self.bal

    @property
    def weight(self):
        return self.domain.weight + self.calc_weight