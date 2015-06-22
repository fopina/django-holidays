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
    ret = False
    g = holidays.models.Group.objects.get(pk=group)
    for r in g.rule_set.all():
        f = getattr(rules, r.method, None)
        if f is None:
            continue
        ret = f(date, *r.parameters.split(','))
        if ret:
            break

    return ret
