from datetime import datetime
from datetime import time

t_s = input("Enter time (HH:MM): ")

current_time = datetime.strptime(t_s, "%H:%M").time()

if time(7, 59) < current_time < time(11, 40):
    print(f"Currently it`s {current_time} so it is breakfast time.")
elif time(11, 59) < current_time < time(3, 0):
    print(f"Currently it`s {current_time} so it is lunch time.")
elif time(19, 59) < current_time < time(23, 0):
    print(f"Currently it`s {current_time} so it is dinner time.")
else:
    print("Free time havesome snacks!!")