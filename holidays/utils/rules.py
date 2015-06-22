import sys
from datetime import timedelta
import holidays


# Fixed day in month
def fixed_date(date, day, month):
    return ((date.day == int(day)) and (date.month == int(month)))


# Easter sunday
def easter_sunday(date, calendar):
    # Calendar options: EASTER_JULIAN, EASTER_ORTHODOX, EASTER_WESTERN
    from dateutil import easter
    return date == easter.easter(date.year, getattr(easter, calendar))


# N days before rule X
def n_days_before_rule(date, days, rule):
    t = date + timedelta(days=int(days))
    r = holidays.models.Rule.objects.get(pk=int(rule))
    f = getattr(sys.modules[__name__], r.method, None)
    return f(t, *r.parameters.split(','))
