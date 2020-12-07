import datetime

def round_time(dt=None, date_delta=datetime.timedelta(minutes=1), to='average'):
    """
    Round a datetime object to a multiple of a timedelta
    dt : datetime.datetime object, default now.
    dateDelta : timedelta object, we round to a multiple of this, default 1 minute.
    from:  http://stackoverflow.com/questions/3463930/how-to-round-the-minute-of-a-datetime-object-python
    """
    round_to = date_delta.total_seconds()
    if dt is None:
        dt = datetime.datetime.utcnow()
    seconds = (dt - dt.min).seconds
    if seconds % round_to == 0:
        rounding = (seconds + round_to / 2) // round_to * round_to
    else:
        if to == 'up':
            # // is a floor division, not a comment on following line (like in javascript):
            rounding = (seconds + round_to) // round_to * round_to
        elif to == 'down':
            rounding = seconds // round_to * round_to
        else:
            rounding = (seconds + round_to / 2) // round_to * round_to
    return dt + datetime.timedelta(0, rounding - seconds, -dt.microsecond)

###

seviriTime = round_time(datetime.datetime.utcnow(),date_delta=datetime.timedelta(minutes=15),to='down')
insatTime = round_time(datetime.datetime.utcnow(),date_delta=datetime.timedelta(minutes=30),to='down')
ahiTime = round_time(datetime.datetime.utcnow(),date_delta=datetime.timedelta(minutes=10),to='down')
modelAnalysisTime = round_time(datetime.datetime.utcnow(),date_delta=datetime.timedelta(hours=6),to='down')
