from datetime import date
from datetime import datetime
import os
import time

while True:
    x = 4
    if x == 4:
        os.system('clear')
    x = date.today()
    a = datetime.now()
    print(x.day, "/", x.month, "/", x.year, a.hour, ":", a.minute, ":", a.second, "GMT/UTC")
    time.sleep(1)
    os.system('clear')
    print(x.day, "/", x.month, "/", x.year, " ", a.hour, ":", a.minute, ":", a.second, "GMT/UTC")