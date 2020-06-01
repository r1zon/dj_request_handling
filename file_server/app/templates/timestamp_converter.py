import datetime

def timestamp_converter(date):
    dtime = datetime.datetime.fromtimestamp(date).strftime("%Y-%m-%d %H:%M")
    return dtime
