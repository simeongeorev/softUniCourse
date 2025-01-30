days_off = int(input())

work_days = 365 - days_off
playtime_minutes_total = work_days * 63 + days_off * 127
tom_playtime = 30000

available_time = playtime_minutes_total - tom_playtime
if available_time < 0:
    available_time *= -1

hours_available = available_time // 60
minutes_available = available_time % 60

if playtime_minutes_total > tom_playtime:
    print("Tom will run away")
    print(f"{hours_available} hours and {minutes_available} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours_available} hours and {minutes_available} minutes less for play")