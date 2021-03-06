""""
This module returns list of colleagues who will celebrate birthday on next
weekend or next week.
"""
from datetime import date, timedelta, datetime
from util import NameBirthGenerator

FILE = 'firstnames_f.json'

WEEK_DAYS = ('Monday', 'Thuesday', 'Wednesday', 'Thuersday', 'Friday',
             'Saturday', 'Sunday')
DAYS = {day: None for day in range(0, 7)}
B_DAY = {day: [] for day in range(0, 7)}


def main():
    """
    Main function that forms list of birthday dicts and calls function for
    congratulation
    """
    users = []
    for item in NameBirthGenerator(FILE, 1980, 2000, 500):
        users.append(item)
    # for user in users:
    #     print(user)
    calc_dates()
    scan(users)
    congratulate()


def calc_dates():
    """
    Calculate all dates for next weekend and week, puts them to the dict DAYS
    """
    now = date.today()
    day_delta = 5 - now.weekday()
    delta = timedelta(days=day_delta if day_delta >= 0 else 0)
    for _ in range(7):
        day = now + delta
        DAYS[day.weekday()] = day.strftime('%d %m')
        delta += timedelta(days=1)


def scan(lst_users):
    """
    Scans the list of colleagues and checks if their birthday on the DAYS list
    :param lst_users: [dict]
    """
    for item in lst_users:
        if item['birthday'].strftime('%d %m') in DAYS.values():
            B_DAY[item['birthday'].weekday()].append(item['name'])
    B_DAY[0] += B_DAY[5]
    B_DAY[0] += B_DAY[6]
    del B_DAY[6]
    del B_DAY[5]


def congratulate():
    """
    Goes thought the list with colleagues which have birthday next week or next
    weekend and print them
    """
    counter = 0
    for weekday, persons in B_DAY.items():
        if persons:
            print(f'{WEEK_DAYS[weekday]}: {", ".join(persons)}')
            counter += 1
    if counter == 0:
        print('No birthdays next week')


if __name__ == '__main__':
    main()


