
from datetime import datetime, timedelta

def parse_time_range(start_str, end_str):
    """Converts time range strings like '5:30 PM' to 24-hour datetime.time objects"""
    start = datetime.strptime(start_str.strip().lower().replace('.', ''), "%I:%M %p")
    end = datetime.strptime(end_str.strip().lower().replace('.', ''), "%I:%M %p")
    return start, end

def format_time(dt):
    """Formats datetime object to something like 4:00p or 12:30a"""
    suffix = 'a' if dt.hour < 12 or dt.hour == 24 else 'p'
    hour = dt.hour % 12 or 12
    return f"{hour}:{dt.minute:02}{suffix}"

def calculate_call_times(start_time, end_time, role):
    """Returns formatted time range for given role"""
    if role in ['Server', 'Dishwasher']:
        call_in = start_time - timedelta(hours=1.5)
    elif role in ['Banquet Manager', 'Bartender', 'Greeter']:
        call_in = start_time - timedelta(hours=2)
    else:
        return None

    call_out = end_time + timedelta(hours=1)
    return f"{format_time(call_in)} - {format_time(call_out)}"
