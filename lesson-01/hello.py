print("Hello, Python!")

from datetime import timedelta, datetime

now = datetime.now()
print(now)
twenty_two_may = datetime(2017, 5, 22)
period = twenty_two_may - now
print("{} дней  {} секунд   {} микросекунд".format(period.days, period.seconds , period.microseconds))
# 18 дней  17537 секунд   72765 микросекунд

print("Всего: {} секунд".format(period.total_seconds()))

