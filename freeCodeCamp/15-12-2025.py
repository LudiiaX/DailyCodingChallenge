def speed_check(speed_mph, speed_limit_kph):
    kph = speed_mph * 1.60934

    if kph <= speed_limit_kph:
        return 'Not Speeding'
    elif kph <= speed_limit_kph+5:
        return "Warning"
    else :
        return "Ticket"



print(speed_check(30, 70))
print(speed_check(40, 60))
print(speed_check(40, 65))
print(speed_check(60, 90))
print(speed_check(65, 100))
print(speed_check(88, 40))