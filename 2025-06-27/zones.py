from datetime import datetime
from zoneinfo import ZoneInfo

now_time_here = datetime.now()
print("Now:", now_time_here)

now_utc = datetime.now(tz=ZoneInfo("UTC"))
print("UTC time:", now_utc)

now_ny = now_utc.astimezone(ZoneInfo("America/New_York"))
print("New York time:", now_ny)