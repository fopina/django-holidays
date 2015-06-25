from django.test import TestCase
from .utils import is_holiday
from datetime import date, timedelta


class HolidaysTests(TestCase):
    longMessage = True
    fixtures = ['demo']

    def fullYearTest(self, group, year, holidays):
        it = date(year, 1, 1)
        end = date(year, 12, 31)
        delta = timedelta(days=1)

        calc_holidays = []

        while it <= end:
            if is_holiday(group, it):
                calc_holidays.append(it)
            it += delta

        self.assertEquals(calc_holidays, holidays)

    def testPortugal2015(self):
        self.fullYearTest(
            'PT',
            2015,
            [
                date(2015, 1, 1),
                date(2015, 4, 3),
                date(2015, 4, 5),
                date(2015, 4, 25),
                date(2015, 5, 1),
                date(2015, 6, 10),
                date(2015, 8, 15),
                date(2015, 12, 8),
                date(2015, 12, 25),
            ],
        )

    def testPortugalPorto2015(self):
        self.fullYearTest(
            'PT-PRT',
            2015,
            [
                date(2015, 1, 1),
                date(2015, 4, 3),
                date(2015, 4, 5),
                date(2015, 4, 25),
                date(2015, 5, 1),
                date(2015, 6, 10),
                date(2015, 6, 24),
                date(2015, 8, 15),
                date(2015, 12, 8),
                date(2015, 12, 25),
            ],
        )
