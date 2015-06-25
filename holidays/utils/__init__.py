import inspect
from . import rules
# import full module because of circular import in models
import holidays


def list_rules():
    f = inspect.getmembers(rules, predicate=inspect.isfunction)
    return map(
        lambda x: (x[0], inspect.getcomments(x[1])[1:].strip()),
        f
    )


def is_holiday(group, date):
    g = holidays.models.Group.objects.get(pk=group)
    while g is not None:
        for r in g.rule_set.all():
            f = getattr(rules, r.method, None)
            if f is None:
                continue
            if f(date, *r.parameters.split(',')):
                return True
        g = g.parent

    return False
