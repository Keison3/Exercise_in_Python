def time_of_today():
    '''
    calculate the time(hour:minute:second) of today from epoch (1970)
    :return:
    '''
    import time
    seconds_from_epoch = int(time.time())

    days = seconds_from_epoch // 3600 // 24
    seconds_of_days = days * 24 * 3600

    hour = (seconds_from_epoch - seconds_of_days) // 3600
    seconds_of_hour = hour * 3600

    minute = (seconds_from_epoch - seconds_of_days - seconds_of_hour) // 60
    seconds_of_minute = minute * 60

    second = seconds_from_epoch - seconds_of_days - seconds_of_hour - seconds_of_minute

    print("the number of days since the epoch: ", days)
    print("The current time is ", hour, ":", minute, ":", second)

