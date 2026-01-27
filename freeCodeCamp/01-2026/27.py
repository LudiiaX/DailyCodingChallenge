# 1 raw challenge:
from datetime import datetime, timezone

def odd_or_even_day(timestamp):
    return "even" if int(datetime.fromtimestamp(timestamp/1000, tz=timezone.utc).day) % 2 == 0 else "odd"

print(odd_or_even_day(1769472000000))
print(odd_or_even_day(1769444440000))
print(odd_or_even_day(6739456780000))
print(odd_or_even_day(1))
print(odd_or_even_day(86400000))
